from hal import hal_input_switch as switch
from hal import hal_led as led
from time import sleep, time

def main():
    switch.init()
    led.init()
    while(1):
        if switch.read_slide_switch():
            led.set_output(0,1)
            sleep(0.1)
            led.set_output(0,0)
            sleep(0.1)
        else:
            time_finish = time() + 5
            while time() < time_finish:
             led.set_output(0,1)
             sleep(0.05)
             led.set_output(0,0)
             sleep(0.05)

if __name__ == "__main__":
    main()
