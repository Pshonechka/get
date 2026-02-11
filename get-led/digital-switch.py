import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
button = 13
GPIO.setup(button, GPIO.IN)

GPIO.setup(led, GPIO.OUT)
state = 0
while True:
    if GPIO.input(button):

        GPIO.output(led, state)
        state = not state
        time.sleep(0.2)
