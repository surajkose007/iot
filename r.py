


import RPi.GPIO as GPIO
import time

sensor = 23
buzzer = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print ("Initialzing PIR Sensor......")
time.sleep(6)
print ("PIR Ready...")
print (" ")

try:
   while True:
      if GPIO.input(sensor):
          GPIO.output(buzzer,True)
          print ("Motion Detected")

      else:
          GPIO.output(buzzer,False)
          print ("Motion MMMMMMMMMMMMMMMMMMMMMM")

except KeyboardInterrupt:
    GPIO.cleanup()

