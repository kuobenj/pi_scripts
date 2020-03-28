import RPi.GPIO
import os
import time

#can put this in /etc/rc.local

# Pin Definitons:
switchPin1    = 7
switchPin2    = 32

LEDPin1 = 33
LEDPin2 = 35
LEDPin3 = 37

# Initial Pin Setup:
RPi.GPIO.setmode(RPi.GPIO.BOARD) # Broadcom pin-numbering scheme

# Switch Setup:
RPi.GPIO.setup(switchPin1, RPi.GPIO.IN, pull_up_down = RPi.GPIO.PUD_UP)
RPi.GPIO.setup(switchPin2, RPi.GPIO.IN, pull_up_down = RPi.GPIO.PUD_UP)

RPi.GPIO.setup(LEDPin1, RPi.GPIO.OUT)
RPi.GPIO.setup(LEDPin2, RPi.GPIO.OUT)
RPi.GPIO.setup(LEDPin3, RPi.GPIO.OUT)

# Main loop is only event drivent for this script
print("Here we go! Press CTRL+C to exit")
try:
    LED_val = 0
    switch1_state = RPi.GPIO.input(switchPin1)
    while 1:
        read_val1 = RPi.GPIO.input(switchPin1)
        if read_val1 == switch1_state:
            pass
        else:
            switch1_state = read_val1
            if switch1_state:
                print '\nLights Off\n'
                os.system('curl -X POST https://maker.ifttt.com/trigger/bed_lamp_off/with/key/b1SgHiGpXqazCsnAuVwLi')
            else:
                print '\nLights On\n'
                os.system('curl -X POST https://maker.ifttt.com/trigger/bed_lamp_on/with/key/b1SgHiGpXqazCsnAuVwLi')
        switch2_state = RPi.GPIO.input(switchPin2)
        if switch2_state:
            pass
        else:
            LED_val = LED_val + 1
            LED_val = LED_val % 8
            if LED_val == 0:
                RPi.GPIO.output(LEDPin1, False)
                RPi.GPIO.output(LEDPin2, False)
                RPi.GPIO.output(LEDPin3, False)
            elif LED_val == 1:
                RPi.GPIO.output(LEDPin1, True)
                RPi.GPIO.output(LEDPin2, True)
                RPi.GPIO.output(LEDPin3, True)
            elif LED_val == 2:
                RPi.GPIO.output(LEDPin1, True)
                RPi.GPIO.output(LEDPin2, False)
                RPi.GPIO.output(LEDPin3, False)
            elif LED_val == 3:
                RPi.GPIO.output(LEDPin1, False)
                RPi.GPIO.output(LEDPin2, True)
                RPi.GPIO.output(LEDPin3, False)
            elif LED_val == 4:
                RPi.GPIO.output(LEDPin1, False)
                RPi.GPIO.output(LEDPin2, False)
                RPi.GPIO.output(LEDPin3, True)
            elif LED_val == 5:
                RPi.GPIO.output(LEDPin1, True)
                RPi.GPIO.output(LEDPin2, True)
                RPi.GPIO.output(LEDPin3, False)
            elif LED_val == 6:
                RPi.GPIO.output(LEDPin1, False)
                RPi.GPIO.output(LEDPin2, True)
                RPi.GPIO.output(LEDPin3, True)
            elif LED_val == 7:
                RPi.GPIO.output(LEDPin1, True)
                RPi.GPIO.output(LEDPin2, False)
                RPi.GPIO.output(LEDPin3, True)
            else:
                RPi.GPIO.output(LEDPin1, False)
                RPi.GPIO.output(LEDPin2, False)
                RPi.GPIO.output(LEDPin3, False)

        time.sleep(1)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    RPi.GPIO.cleanup() # cleanup all RPi.GPIO