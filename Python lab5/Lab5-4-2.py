import random
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello World from Flask'

@app.route("/hi")
def who():
    return 'Who are you?'

@app.route("/hi/<someone>")
def greet(someone):
    return f'Hi there, {someone}!'

if __name__ == "__main__":
    app.run(debug=True,
            host='127.0.0.1',
            port=80)

#http://127.0.0.1/
#Hello World from Flask
#http://127.0.0.1/hi
#Who are you?
#http://127.0.0.1/hi/Gorgu
#Hi there, Gorgu!