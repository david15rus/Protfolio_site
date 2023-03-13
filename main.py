import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpg')

with col2:
    st.title("David Avdonin")
    content = """
    Something about me 
    """
    st.info(content)

col3, col4 = st.columns(2)

df = pandas.read_csv('data.csv', sep=';')
with col3:
    for idx, row in df[:10].iterrows():
        st.header(row['Title'])
        st.text(row['Descriptions'])

with col4:
    for idx, row in df[10:].iterrows():
        st.header(row['Title'])
        st.text(row['Descriptions'])

content = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content)
