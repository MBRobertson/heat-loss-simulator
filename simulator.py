import datetime

import r_values as R
import weather
import glob
import thermometer
import switch

class Heater:
    def __init__(self, wattage, delay=60):
        self.wattage = wattage
        self.output = 0
        self.increment = wattage / delay

    def work(self, running=False, seconds=1):
        # Have basic linear hysteresis for the heater
        if running:
            self.output = min(self.wattage, self.output + (self.increment * seconds))
        else:
            self.output = max(0, self.output - (self.increment * seconds))
        return self.output * seconds


class Simulator:
    def __init__(self, room, start_date=None):
        self.room = room
        self.room['init_temp'] = thermometer.get_temp()
        if room['init_temp'] < room['target_temp']:
            switch.on()
        self.hl = R.compute_heat_loss(room['A'])  # Heat loss (W/C)
        # Default start date to the following day
        if start_date is None:
            start_date = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
            start_date = start_date + datetime.timedelta(days=1, hours=6)
        self.time = start_date
        self.weather = weather.defaultProvider(town=room['location'])
        self.heater = Heater(room['heater'])
        self.energy = R.compute_air_energy((room['init_temp'] if 'init_temp' in room else self.weather.at_time(self.time)) + 0.01, room['volume'])

    def temp(self):
        return R.compute_air_temp(self.energy, self.room['volume'])

    def tick(self, heating=True, seconds=1):
        room_temp = self.temp()
        delta_temp = room_temp - self.weather.at_time(self.time)

        q_gain = self.heater.work(running=heating, seconds=seconds)
        q_loss = self.hl * delta_temp * seconds
        delta_q = (q_gain - q_loss) / 1000  # Convert to kJ

        self.energy = self.energy + delta_q
        self.time = self.time + datetime.timedelta(seconds=seconds)

        return self.temp()

    
