import RPi.GPIO as GPIO
import time

LED_PIN_R = 4
LED_PIN_Y = 5 
LED_PIN_G = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_R, GPIO.OUT)
GPIO.setup(LED_PIN_Y, GPIO.OUT)
GPIO.setup(LED_PIN_G, GPIO.OUT)

GPIO.output(LED_PIN_R, GPIO.HIGH)
print("red led on")
time.sleep(2)
GPIO.output(LED_PIN_R, GPIO.LOW)
print("red led off")

GPIO.output(LED_PIN_Y, GPIO.HIGH)
print("yellow led on")
time.sleep(2)
GPIO.output(LED_PIN_Y, GPIO.LOW)
print("yellow led off")

GPIO.output(LED_PIN_G, GPIO.HIGH)
print("green led on")
time.sleep(2)
GPIO.output(LED_PIN_G, GPIO.LOW)
print("green led off")


GPIO.cleanup()