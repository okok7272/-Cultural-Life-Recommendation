#__init__.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def startpage():
    #해당 축제 선택
    return 0


@app.route('//')
def MonthrecommandPage():
    return 0