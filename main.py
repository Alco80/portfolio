import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/alicia.png")

with col2:
    st.title("Alicia Corke")
    content = """
I'm Alicia Corke and I'm a programmer from Ottawa Ontario, Canada.

""" 
st.info(content)

content2 = """
Enjoy my portfolio. Thank You!

""" 

st.info(content2)

col3, col4 = st.columns(2)


df = pd.read_csv('data_portfolio.csv', sep=";")

with col3:
    for index, row in df.iterrows():
        st.header(row["title"])
