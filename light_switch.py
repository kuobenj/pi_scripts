import RPi.GPIO
import os
import time
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

#can put this in /etc/rc.local

# Pin Definitons:
switchPin1    = 7
switchPin2    = 32

LEDPin1 = 33 # BLUE
LEDPin2 = 35 # GREEN
LEDPin3 = 37 # RED

# LED Color Definitions
LED_OFF      = 0
LED_WHITE    = 1
LED_BLUE     = 2
LED_GREEN    = 3
LED_RED      = 4
LED_CYAN     = 5
LED_YELLOW   = 6
LED_MAGENTA  = 7

# Party mode global
party = False

def write_color(color):
    if color == LED_OFF:
        RPi.GPIO.output(LEDPin1, False)
        RPi.GPIO.output(LEDPin2, False)
        RPi.GPIO.output(LEDPin3, False)
    elif color == LED_WHITE:
        RPi.GPIO.output(LEDPin1, True)
        RPi.GPIO.output(LEDPin2, True)
        RPi.GPIO.output(LEDPin3, True)
    elif color == LED_BLUE:
        RPi.GPIO.output(LEDPin1, True)
        RPi.GPIO.output(LEDPin2, False)
        RPi.GPIO.output(LEDPin3, False)
    elif color == LED_GREEN:
        RPi.GPIO.output(LEDPin1, False)
        RPi.GPIO.output(LEDPin2, True)
        RPi.GPIO.output(LEDPin3, False)
    elif color == LED_RED:
        RPi.GPIO.output(LEDPin1, False)
        RPi.GPIO.output(LEDPin2, False)
        RPi.GPIO.output(LEDPin3, True)
    elif color == LED_CYAN:
        RPi.GPIO.output(LEDPin1, True)
        RPi.GPIO.output(LEDPin2, True)
        RPi.GPIO.output(LEDPin3, False)
    elif color == LED_YELLOW:
        RPi.GPIO.output(LEDPin1, False)
        RPi.GPIO.output(LEDPin2, True)
        RPi.GPIO.output(LEDPin3, True)
    elif color == LED_MAGENTA:
        RPi.GPIO.output(LEDPin1, True)
        RPi.GPIO.output(LEDPin2, False)
        RPi.GPIO.output(LEDPin3, True)
    else:
        RPi.GPIO.output(LEDPin1, False)
        RPi.GPIO.output(LEDPin2, False)
        RPi.GPIO.output(LEDPin3, False)



# Class adapted from here: https://www.e-tinkers.com/2018/04/how-to-control-raspberry-pi-gpio-via-http-web-server/
class MyServer(BaseHTTPRequestHandler):
    def do_HEAD(self):
        """ do_HEAD() can be tested use curl command
            'curl -I http://server-ip-address:port'
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """ do_GET() can be tested using curl command
            'curl http://server-ip-address:port'
        """
        # We can add some status later about what color of the LEDs later
        html = '''
            <html>
            <body>
            <h1>Thanks For Your Request</h1>
            <button style="width: 24%; height: 50%; background-color: black; color: white;" onclick="document.location='/off'">OFF</button>
            <button style="width: 24%; height: 50%;"  onclick="document.location='/on'">ON</button>
            <button style="width: 24%; height: 50%; background-color: red;" onclick="document.location='/red'">RED</button>
            <button style="width: 24%; height: 50%; background-color: green;" onclick="document.location='/green'">GREEN</button>
            <button style="width: 24%; height: 50%; background-color: blue;" onclick="document.location='/blue'">BLUE</button>
            <button style="width: 24%; height: 50%; background-color: magenta;" onclick="document.location='/magenta'">MAGENTA</button>
            <button style="width: 24%; height: 50%; background-color: cyan;" onclick="document.location='/cyan'">CYAN</button>
            <button style="width: 24%; height: 50%; background-color: yellow;" onclick="document.location='/yellow'">YELLOW</button>
            </body>
            </html>
        '''
        self.do_HEAD()
        global party
        party = False
        status = ''
        if self.path=='/':
            pass
        elif self.path=='/on':
            status='LED is On'
            write_color(LED_WHITE);
            # https://github.com/tigoe/WeMoExamples
            os.system('curl -H \'Content-type:text/xml;  charset=utf-8\' -H \'SOAPACTION:"urn:Belkin:service:basicevent:1#SetBinaryState"\' -d \'<?xml version="1.0" encoding="utf-8"?> <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"> <s:Body><u:SetBinaryState xmlns:u="urn:Belkin:service:basicevent:1"> <BinaryState>1</BinaryState></u:SetBinaryState></s:Body></s:Envelope>\' \'http://192.168.1.4:49153/upnp/control/basicevent1\'')
        elif self.path=='/off':
            status='LED is Off'
            write_color(LED_OFF);
            # https://github.com/tigoe/WeMoExamples
            os.system('curl -H \'Content-type:text/xml;  charset=utf-8\' -H \'SOAPACTION:"urn:Belkin:service:basicevent:1#SetBinaryState"\' -d \'<?xml version="1.0" encoding="utf-8"?> <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"> <s:Body><u:SetBinaryState xmlns:u="urn:Belkin:service:basicevent:1"> <BinaryState>0</BinaryState></u:SetBinaryState></s:Body></s:Envelope>\' \'http://192.168.1.4:49153/upnp/control/basicevent1\'')
        elif self.path=='/black' or self.path=='/0':
            write_color(LED_OFF);
        elif self.path=='/white' or self.path=='/1':
            write_color(LED_WHITE);
        elif self.path=='/blue' or self.path=='/2':
            write_color(LED_BLUE);
        elif self.path=='/green' or self.path=='/3':
            write_color(LED_GREEN);
        elif self.path=='/red' or self.path=='/4':
            write_color(LED_RED);
        elif self.path=='/cyan' or self.path=='/5':
            write_color(LED_CYAN);
        elif self.path=='/yellow' or self.path=='/6':
            write_color(LED_YELLOW);
        elif self.path=='/magenta' or self.path=='/7':
            write_color(LED_MAGENTA);
        elif self.path=='/party':
            party = True
        else:
            pass
        self.wfile.write(html.encode("utf-8"))

if __name__ == '__main__':
    # Initial Pin Setup:
    RPi.GPIO.setmode(RPi.GPIO.BOARD) # Broadcom pin-numbering scheme

    # Switch Setup:
    RPi.GPIO.setup(switchPin1, RPi.GPIO .IN, pull_up_down = RPi.GPIO.PUD_UP)
    RPi.GPIO.setup(switchPin2, RPi.GPIO.IN, pull_up_down = RPi.GPIO.PUD_UP)

    RPi.GPIO.setup(LEDPin1, RPi.GPIO.OUT)
    RPi.GPIO.setup(LEDPin2, RPi.GPIO.OUT)
    RPi.GPIO.setup(LEDPin3, RPi.GPIO.OUT)

    # Grab IP
    local_ip_request = subprocess.Popen(['hostname', '-I'], stdout=subprocess.PIPE)
    my_local_ip_str, irrelevant = local_ip_request.communicate()
    print(my_local_ip_str)
    local_port = 1773
    http_server = HTTPServer((my_local_ip_str, local_port), MyServer)
    http_server.timeout = 0.01

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
                    print('\nLights Off\n')
                    # old IFTTT trigger, since IFTTT limited stuff I looked into other methods to communicate with Belkin stuff directly
                    # os.system('curl -X POST https://maker.ifttt.com/trigger/bed_lamp_off/with/key/b1SgHiGpXqazCsnAuVwLi')
                    # https://github.com/tigoe/WeMoExamples
                    os.system('curl -H \'Content-type:text/xml;  charset=utf-8\' -H \'SOAPACTION:"urn:Belkin:service:basicevent:1#SetBinaryState"\' -d \'<?xml version="1.0" encoding="utf-8"?> <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"> <s:Body><u:SetBinaryState xmlns:u="urn:Belkin:service:basicevent:1"> <BinaryState>0</BinaryState></u:SetBinaryState></s:Body></s:Envelope>\' \'http://192.168.1.4:49153/upnp/control/basicevent1\'')
                    write_color(LED_OFF)
                else:
                    print('\nLights On\n')
                    # old IFTTT trigger, since IFTTT limited stuff I looked into other methods to communicate with Belkin stuff directly
                    # os.system('curl -X POST https://maker.ifttt.com/trigger/bed_lamp_on/with/key/b1SgHiGpXqazCsnAuVwLi')
                    # https://github.com/tigoe/WeMoExamples
                    os.system('curl -H \'Content-type:text/xml;  charset=utf-8\' -H \'SOAPACTION:"urn:Belkin:service:basicevent:1#SetBinaryState"\' -d \'<?xml version="1.0" encoding="utf-8"?> <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"> <s:Body><u:SetBinaryState xmlns:u="urn:Belkin:service:basicevent:1"> <BinaryState>1</BinaryState></u:SetBinaryState></s:Body></s:Envelope>\' \'http://192.168.1.4:49153/upnp/control/basicevent1\'')
                    write_color(LED_WHITE)
            switch2_state = RPi.GPIO.input(switchPin2)
            if switch2_state:
                pass
            else:
                LED_val = LED_val + 1
                LED_val = LED_val % 8
                write_color(LED_val)

            http_server.handle_request()
            if not party:
                time.sleep(1)
            else: # still need to implement party mode
                print('PARTY')
                LED_val = (LED_val % 7) + 1
                write_color(LED_val)
                time.sleep(0.05)
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        RPi.GPIO.cleanup() # cleanup all RPi.GPIO
        http_server.server_close() # clean up server