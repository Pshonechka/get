import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

foto_trans = 6
GPIO.setup(foto_trans, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(foto_trans))