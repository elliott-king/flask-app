from flask import Flask


app = Flask(__name__)

raise Exception('Boom!')

@app.route('/')
def hello_world():
    return 'This is a pull request!'
