from simulator import Simulator
from controller import Controller
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS, cross_origin
import datetime


# Setup flask web server
app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)


# Serve home page
@app.route('/', methods=['GET'])
def index():
    return send_file('static/index.html')


@app.route('/api/predict', methods=['POST'])
@cross_origin()
def run_simulation():
    record_interval = 30  # How often to record values to be send to the client

    # Extract the room data and setup a simulator and controller
    room = request.json
    sim = Simulator(room, start_date=datetime.datetime.fromtimestamp(room['from']) if 'from' in room else None)
    c = Controller(kp=2.2, kd=2.4*200, ki=2.4/10000, heater=sim.heater)

    target_temp = room['target_temp']
    interval = room['interval'] * 60 if 'interval' in room else 60
    last_interval = interval

    # Start some measurements for simulators data over time
    start_time = int(sim.time.timestamp())
    temp_hist = [sim.temp()]
    outside_temp_hist = [sim.weather.at_time(sim.time)]
    control_data = [
        {
            'time': int(sim.time.timestamp()),
            'heating': False
        }
    ]

    # Start state for the heater
    heating = False

    # Find how long to run the simulator for in seconds
    time = 4 * 3600
    if 'from' in room and 'to' in room:
        delta = room['to'] - room['from']
        time = delta if delta >= 0 else time

    # Run the simulation for the required number of seconds
    for i in range(time):
        # Only allow controller to adjust its output within specific time frames
        last_interval += 1
        if last_interval >= interval:
            new_heating = c.work(temp_hist[-1] - target_temp)
            if new_heating != heating:
                heating = new_heating
                last_interval = 0
        else:
            c.work(temp_hist[-1] - target_temp)
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

    # Send control output and statistics back to the client
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
