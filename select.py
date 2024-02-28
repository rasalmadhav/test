import pandas as pd
import streamlit as st

data = {}
for i in range(20):
    col = f'col{i}'
    data[col]= range(10)
df = pd.DataFrame(data)

columns = st.multiselect("Columns:",df.columns)
filter = st.radio("Choose by:", ("inclusion","exclusion"))

if filter == "exclusion":
    columns = [col for col in df.columns if col not in columns]

df[columns]