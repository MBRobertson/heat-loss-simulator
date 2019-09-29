class Controller:
    def __init__(self, running=False):
        self.running = False

    def work(self, current_temp, target_temp):
        return current_temp < target_temp
        # if current_temp > target_temp - 1:
        #     self.running = False
        # elif current_temp < target_temp + 1:
        #     self.running = True
        #
        # return self.running
