class Controller:
    def __init__(self, kp=0, ki=0, kd=0, heater=None, running=False):
        self.running = False
        self.heater = heater
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.last_error = 0
        self.total_error = 0

    def work(self, error):
        if self.heater:
            ep = error
            ed = self.last_error - error
            self.last_error = error
            self.total_error += error
            ei = self.total_error

            return (self.kp * ep + self.ki * ei + self.kd * ed) < 0
        else:
            return error < 0
        # if current_temp > target_temp - 1:
        #     self.running = False
        # elif current_temp < target_temp + 1:
        #     self.running = True
        #
        # return self.running
