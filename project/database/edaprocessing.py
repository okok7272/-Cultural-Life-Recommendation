import sqlite3

import pandas as pd

dbpath = "exfes.db"
conn = sqlite3.connect(dbpath)
cur = conn.cursor()

culture = pd.read_sql("SELECT * FROM outdoor;",conn, index_col='id')

culture=culture['start_period'].str.rstrip('.')

culture= culture['end_period'].str.rstrip('.')

def csvsave():
    culcsv= culture.copy()
    culcsv['start_period']= culture['start_period'].str.replace('.','')
    culcsv['end_period'] = culture['end_period'].str.replace('.','')
    culcsv['end_period']=pd.to_datetime(culture['end_period'])
    culcsv['start_period']=pd.to_datetime(culture['start_period'])
    return culcsv

def sqlitesave():
    culsql = culture.copy()
    culsql['start_period']= culsql['start_period'].str.replace('.','')
    culsql['end_period'] = culsql['end_period'].str.replace('.','')
    culsql['start_period']= culsql['start_period'].astype(int)
    culsql['end_period'] = culsql['end_period'].astype(int)
    return culsql


