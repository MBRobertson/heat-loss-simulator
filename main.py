from simulator import Simulator
from controller import Controller
import matplotlib.pyplot as plt
from flask import Flask, request, send_file, send_from_directory, jsonify

# A basic 5m x 5m room with two 1m x 1m windows, 2.75m tall
ROOM = {
    "A": {  # Areas of specific components of the room
        "ROOF": 25,
        "WALL": (20 * 2.75) - 4,
        "FLOOR": 25,
        "WINDOW_SINGLE_WOOD": 4
    },
    'volume': 5*5*2.75,  # Volume of air in the room
    'init_temp': 18,  # Initial temperature of the room in C
    'target_temp': 20,
    'location': 'Hamilton',  # Location to pull weather data from
    'heater': 1000  # Wattage of heater (J/s)
}


# Setup flask web server
app = Flask(__name__, static_url_path='', static_folder='static')


# Serve home page
@app.route('/', methods=['GET'])
def index():
    return send_file('static/index.html')


@app.route('/api/predict', methods=['POST'])
def run_simulation():
    record_interval = 30  # How often to record values to be send to the client

    room = request.json
    sim = Simulator(room)
    c = Controller()

    target_temp = room['target_temp']

    start_time = int(sim.time.timestamp())
    temp_hist = [sim.temp()]
    outside_temp_hist = [sim.weather.at_time(sim.time)]
    control_data = [
        {
            'time': int(sim.time.timestamp()),
            'heating': False
        }
    ]
    heating = c.work(temp_hist[-1], target_temp)

    for i in range(3600):
        heating = c.work(temp_hist[-1], target_temp)
        current_temp = sim.tick(heating=heating)
        # Record values to be graphed on the client
        if i % record_interval == 0:
            temp_hist.append(current_temp)
            outside_temp_hist.append(sim.weather.at_time(sim.time))
        # Log changes to controller output
        if heating != control_data[-1]['heating']:
            control_data.append({
                'time': int(sim.time.timestamp()),
                'heating': heating
            })

    return jsonify(
        {
            'init_time': start_time,
            'interval': record_interval,
            'temp_hist': temp_hist,
            'outdoor_temp_hist': outside_temp_hist,
            'control': control_data
        }
    )


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
