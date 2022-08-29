#__init__.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def startpage():

    return 0


@app.route('//')
def recommandPage():

    return 0