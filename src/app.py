from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<html><body>This is a pull request!</body></html>'
