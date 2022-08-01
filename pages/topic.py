import streamlit as st

st.write('# topics')

import sqlite3
con = sqlite3.connect('opentutorials.db')
cur = con.cursor()
result = cur.execute('SELECT * FROM topics')
rows = result.fetchall()


rows

st.sidebar.write('# Welcome')

import pandas as pd
view = str(st.slider('view', 0, 200, 10))
view
topic_db = pd.read_sql('SELECT * FROM topics WHERE view > '+view, con)
topic_db

con.close()