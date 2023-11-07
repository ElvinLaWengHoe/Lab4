from hal import hal_input_switch as switch
from hal import hal_led as led
from time import sleep

def main():
    switch.init()
    led.init()
    while():
        if switch.read_slide_switch() == 0:
            led.set_output(0,1)
            sleep(0.2)
            led.set_output(0,0)
            sleep(0.2)

if __name__ == "__main__":
    main()
