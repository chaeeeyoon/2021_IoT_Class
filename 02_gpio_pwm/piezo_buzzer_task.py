import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN,262)
pwm.start(10)

melody = [392, 392, 440, 440, 392, 392, 330, 392, 392, 330, 330, 294]


melody_two = [392, 392, 440, 440, 392, 392, 330, 392, 330, 294, 330, 262]

try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.5)

    time.sleep(1)

    for j in melody:
        pwm.ChangeFrequency(j)
        time.sleep(0.5)

finally:
    pwm.stop()
    GPIO.cleanup()