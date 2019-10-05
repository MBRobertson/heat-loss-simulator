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
    room = request.json
    sim = Simulator(room)
    c = Controller()

    target_temp = room['target_temp']

    temp_hist = [sim.temp()]
    control_data = [
        {
            'time': sim.time.total_seconds(),
            'heating': False
        }
    ]
    heating = c.work(temp_hist[-1], target_temp)

    for i in range(3600 * 2):
        heating = c.work(temp_hist[-1], target_temp)
        temp_hist.append(sim.tick(heating=heating))
        control_data.append({
            'time': sim.time.total_seconds(),
            'heating': False
        })

    return jsonify({'preview': temp_hist, 'control': control_data})


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
