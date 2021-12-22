from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)
red = 4
blue = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)

@app.route("/")
def home():
    return'''
        <p>Hello, Flask!!</p>
        <a href="/led/r/on">RED LED ON</a>
        <a href="/led/r/off">RED LED OFF</a>
        <a href="/led/b/on">BLUE LED ON</a>
        <a href="/led/b/off">BLUE LED OFF</a>
        '''
@app.route("/led/<cmd>/<op>")
def led(cmd,op):
    if cmd == "r":
        if op == "on":
            GPIO.output(red, GPIO.HIGH)
            return'''
                <p>RED LED ON</p>
                <a href="/">Go home</a>
            '''
        elif op == "off":
            GPIO.output(red, GPIO.LOW)
            return'''
                <p>RED LED OFF</p>
                <a href="/">Go home</a>
            '''
    elif cmd == "b":
        if op == "on":
            GPIO.output(blue, GPIO.HIGH)
            return'''
                <p>BLUE LED ON</p>
                <a href="/">Go home</a>
            '''
        elif op == "off":
            GPIO.output(blue, GPIO.LOW)
            return'''
                <p>BLUE LED OFF</p>
                <a href="/">Go home</a>
            '''

if __name__=="__main__":
    try:
        app.run(host='0.0.0.0')
    finally:
        GPIO.cleanup()