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

col3, empty_col,  col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv('data.csv', sep=';')

with col3:
    for idx, row in df[:10].iterrows():
        st.header(row['Title'])
        st.write(row['Descriptions'])
        st.image('images/' + row['Image'])
        st.write(f"[Source code]({row['Url']})")

with col4:
    for idx, row in df[10:].iterrows():
        st.header(row['Title'])
        st.write(row['Descriptions'])
        st.image('images/' + row['Image'])
        st.write(f"[Source code]({row['Url']})")

content = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content)
