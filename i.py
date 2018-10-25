import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

p = GPIO.PWM(12,50)
p.start(7.5)

from Adafruit_IO import MQTTClient
import requests

ADAFRUIT_IO_KEY = "c382351ed6b348c4b8633b0247a43e68"
ADAFRUIT_IO_USERNAME = "surajkose007"

def connected(client):
        print('Connectecd. Listening changes..')
        client.subscribe('led')
		client.subscribe('fan')
def disconnected(client):
        print("Disconnected")
        sys.exit(1)

def message(client,feed_id,status):
        if feed_id=='led':
                if status=='ON':
                        print("LED ON")
                        GPIO.output(18,True)
				else:
                        print("LED OFF")
                        GPIO.output(18,False)
        if feed_id=='fan':
                if status=='ON':
                        print("FAN ON")
                        p.ChangeDutyCycle(12.5)
                        time.sleep(3)
                        p.ChangeDutyCycle(2.5)
                        time.sleep(3)
				else:
                        print("FAN OFF")
                        GPIO.output(12,False)

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.connect()
client.loop_blocking()
