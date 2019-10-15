from ouimeaux.environment import Environment
import threading

def threadd():
    env = Environment()
    env.start()
    env.discover(5)
    switches = list(env.list_switches())
    switch = env.get_switch(switches[0])
    switch.on()

def on():
    x = threading.Thread(target=threadd, args=())
    x.start()

