from simulator import Simulator
from controller import Controller
import matplotlib.pyplot as plt

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
    'location': 'Hamilton',  # Location to pull weather data from
    'heater': 1000  # Wattage of heater (J/s)
}

if __name__ == '__main__':
    sim = Simulator(ROOM)
    c = Controller()

    TARGET_TEMP = 20

    temp_hist = [sim.temp()]
    heating = c.work(temp_hist[-1], TARGET_TEMP)

    for i in range(3600*2):
        heating = c.work(temp_hist[-1], TARGET_TEMP)
        temp_hist.append(sim.tick(heating=heating))

    print(sim.time)
    print(sim.weather.at_time(sim.time))

    plt.plot(temp_hist)
    plt.show()
