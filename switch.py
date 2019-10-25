from ouimeaux.environment import Environment
import threading
import time

def threadd(data):
    print(data)
    print(time.time())
    env = Environment()
    env.start()
    env.discover(5)
    switches = list(env.list_switches())
    if len(switches) == 0:
        print("no switches found")
        exit(0)
    switch = env.get_switch(switches[0])
    for sig in data:
        print(sig)
        if int(time.time()) > sig['time']:
            print("pass")
            pass
        else:
            print("waiting ", int(sig['time'] - int(time.time())))
            time.sleep(sig['time'] - int(time.time()))
            if sig['heating'] == True:
                print("on")
                #switch.on()
            else:
                print("off")
                #switch.off()

    

def times(data):
    x = threading.Thread(target=threadd, args=(data,))
    x.start()

