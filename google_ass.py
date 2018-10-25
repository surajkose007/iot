
from Adafruit_IO import MQTTClient
import requests
  
 

ADAFRUIT_IO_KEY      = 'c382351ed6b348c4b8633b0247a43e68'       # Set to your Adafruit IO key.
ADAFRUIT_IO_USERNAME = 'surajkose007'  # See https://accounts.adafruit.com
                                                    # to find your username
def connected(client):                                                    
    print ('Connected.')
    client.subscribe('bulb')
 
 
def disconnected(client):
    print ('Disconnected.')
    sys.exit(1)
 
def message(client, feed_id, status):
    if feed_id == 'bulb':
        #print(type(status),status)
        if status == '1':
            print('BULB ON')
        else:
            print('BULB OFF')

       
       
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.connect()
client.loop_blocking()
