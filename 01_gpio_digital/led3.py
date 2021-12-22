import RPi.GPIO as GPIO

SWITCH_PIN_R = 8
SWITCH_PIN_B = 7
SWITCH_PIN_G = 12

LED_PIN_R = 17
LED_PIN_B = 27
LED_PIN_G= 22


GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN_R, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_B, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_G, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.setup(LED_PIN_R, GPIO.OUT)
GPIO.setup(LED_PIN_G, GPIO.OUT)
GPIO.setup(LED_PIN_B, GPIO.OUT)

try:
    while True:
        val = GPIO.input(SWITCH_PIN_R)
        print(val)
        GPIO.output(LED_PIN_R, val)

        val = GPIO.input(SWITCH_PIN_G)
        print(val)
        GPIO.output(LED_PIN_G, val)

        val = GPIO.input(SWITCH_PIN_B)
        print(val)
        GPIO.output(LED_PIN_B, val)
finally:
    GPIO.cleanup()
    print('clean up and exit')

