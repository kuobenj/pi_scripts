import RPi.GPIO
import os

#can put this in /etc/rc.local

# Pin Definitons:
switchPin    = 7


def lights_on(switchPin):
    print 'Lights On'
    os.system('curl -X POST https://maker.ifttt.com/trigger/bed_lamp_on/with/key/b1SgHiGpXqazCsnAuVwLi')

def lights_off(switchPin):
    print 'Lights Off'
    os.system('curl -X POST https://maker.ifttt.com/trigger/bed_lamp_off/with/key/b1SgHiGpXqazCsnAuVwLi')

# Initial Pin Setup:
RPi.GPIO.setmode(RPi.GPIO.BOARD) # Broadcom pin-numbering scheme

# Switch Setup:
RPi.GPIO.setup(switchPin, RPi.GPIO.IN, pull_up_down = RPi.GPIO.PUD_UP)
RPi.GPIO.add_event_detect(switchPin, RPi.GPIO.FALLING, callback=lights_on, bouncetime=200)  # add falling edge detection on a channel
RPi.GPIO.add_event_detect(switchPin, RPi.GPIO.RISING, callback=lights_off, bouncetime=200)  # add falling edge detection on a channel

# Main loop is only event drivent for this script
print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        pass
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    RPi.GPIO.cleanup() # cleanup all RPi.GPIO