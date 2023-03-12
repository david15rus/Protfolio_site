import streamlit as st

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

content = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content)
