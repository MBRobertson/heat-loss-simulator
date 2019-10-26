from ouimeaux.environment import Environment
import threading
import time

def threadd(data):
    #looks for wemo switch and checks it found one
    env = Environment()
    env.start()
    env.discover(5)
    switches = list(env.list_switches())
    if len(switches) == 0:
        print("no switches found")
        exit(0)
    switch = env.get_switch(switches[0])
    #llops through every on off signal
    for sig in data:
        #goes to next signal if past current signal time 
        if int(time.time()) > sig['time']:
            print("pass")
            pass
        else:
            #waites until end of current period
            time.sleep(sig['time'] - int(time.time()))
            if sig['heating'] == True:
                print("on")
                switch.on()
            else:
                print("off")
                switch.off()

    

def times(data):
    x = threading.Thread(target=threadd, args=(data,))
    x.start()

