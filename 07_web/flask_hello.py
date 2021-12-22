from flask import Flask

app = Flask(__name__)

@app.route("/") #중요!
def hello():
    return'''
        <p>Hello, Flask!!</p>
        <a href="/first">Go first</a>
        <a href="/second">Go second</a>
    '''
@app.route("/first")
def first():
    return'''
        <p>First Page</p>
        <a href="/">Go home</a>
    '''
@app.route("/second")
def second():
    return'''
        <p>Second Page</p>
        <a href="/">Go home</a>
    '''

#터미널에서 직접 실행한 경우
if __name__=="__main__":
    app.run(host="0.0.0.0")
