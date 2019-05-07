import RPi.GPIO
import os
import time

#can put this in /etc/rc.local

# Pin Definitons:
switchPin    = 7

# Initial Pin Setup:
RPi.GPIO.setmode(RPi.GPIO.BOARD) # Broadcom pin-numbering scheme

# Switch Setup:
RPi.GPIO.setup(switchPin, RPi.GPIO.IN, pull_up_down = RPi.GPIO.PUD_UP)

# Main loop is only event drivent for this script
print("Here we go! Press CTRL+C to exit")
try:
    switch_state = RPi.GPIO.input(switchPin)
    while 1:
        read_val = RPi.GPIO.input(switchPin)
        if read_val == switch_state:
            pass
        else:
            switch_state = read_val
            if switch_state:
                print 'Lights On'
                os.system('curl -X POST https://maker.ifttt.com/trigger/bed_lamp_on/with/key/b1SgHiGpXqazCsnAuVwLi')
            else:
                print 'Lights Off'
                os.system('curl -X POST https://maker.ifttt.com/trigger/bed_lamp_off/with/key/b1SgHiGpXqazCsnAuVwLi')
        time.sleep(1)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    RPi.GPIO.cleanup() # cleanup all RPi.GPIO