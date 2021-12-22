from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)
led = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)

@app.route("/") #중요!
def hello():
    return'''
        <p>Hello, Flask!!</p>
        <a href="/led/on">LED ON</a>
        <a href="/led/off">LED OFF</a>
    '''
@app.route("/led/<op>")
def led_op(op):
    if op == "on":
        GPIO.output(led, GPIO.HIGH)
        return'''
            <p>LED ON</p>
            <a href="/">Go home</a>
    '''
    elif op == "off":
        GPIO.output(led, GPIO.LOW)
        return'''
        <p>LED OFF</p>
        <a href="/">Go home</a>
    '''

#터미널에서 직접 실행한 경우
if __name__=="__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()

