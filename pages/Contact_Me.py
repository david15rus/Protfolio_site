import streamlit as st
from send_email import send_email

st.header('Contact Me')

with st.form(key='my_form'):
    user_email = st.text_input('Your email address')
    user_text = st.text_area('Your message')
    message = f'''\
Subject: New email via Portfolio Website

From: {user_email}
{user_text}
'''
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info('Your message was send successfully')
