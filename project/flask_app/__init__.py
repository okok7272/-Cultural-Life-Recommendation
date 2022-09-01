#__init__.py
import pandas as pd
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

dbpath = 'project\exfes.db'

conn = sqlite3.connect(dbpath)
cur = conn.cursor()

culture = pd.read_sql("SELECT * FROM outdoor;",conn, index_col=None)

@app.route('/')
def startpage():
    #해당 축제 선택
    culture =culture

    return render_template('project\flask_app\main.html')



@app.route('/select')
def MonthrecommandPage():
    return 0