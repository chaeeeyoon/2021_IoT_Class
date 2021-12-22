from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
red = 4
blue = 14


GPIO.setmode(GPIO.BCM)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)



@app.route("/")----------------------------------------------------------------------------------------------------------------oute("/")
def home():
    return render_template("led2.html")
@app.route("/led/<cmd>/<op>")
def led(cmd,op):
    if cmd == "r":
        if op == "on":
            GPIO.output(red, GPIO.HIGH)
            return "RED LED ON"

        elif op == "off":
            GPIO.output(red, GPIO.LOW)
            return "RED LED OFF"
           
    elif cmd == "b":
        if op == "on":
            GPIO.output(blue, GPIO.HIGH)
            return "BLUE LED ON"
            
        elif op == "off":
            GPIO.output(blue, GPIO.LOW)
            return "BLUE LED OFF"
        
    else:
        return "URL error"

if __name__=="__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
