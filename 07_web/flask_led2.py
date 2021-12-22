from flask import Flask, render_template
import RPi.GPIO as GPIO 

app = Flask(__name__)
led = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)

@app.route("/") #중요!
def hello():
    return render_template("led.html")
@app.route("/led/<op>")
def led_op(op):
    if op == "on":
        GPIO.output(led, GPIO.HIGH)
        return "LED ON"
    elif op == "off":
        GPIO.output(led, GPIO.LOW)
        return "LED OFF"
    else:
        return "URL error"
     

#터미널에서 직접 실행한 경우
if __name__=="__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()

