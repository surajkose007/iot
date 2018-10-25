
from Adafruit_IO import MQTTClient
import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)  #pinout 12

ADAFRUIT_IO_KEY      = 'c382351ed6b348c4b8633b0247a43e68'      
ADAFRUIT_IO_USERNAME = 'surajkose007'
                                                    
def connected(client):                                                    
    print ('Connected.')
    client.subscribe('bulb')
 
 
def disconnected(client):
    print ('Disconnected.')
    sys.exit(1)
 
def message(client, feed_id, status):
    if feed_id == 'bulb':
      
        if status == '1':
            print('BULB ON')
            GPIO.output(18,GPIO.HIGH)
        else:
            print('BULB OFF')
            GPIO.output(18,GPIO.LOW)

       
       
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.connect()
client.loop_blocking()
