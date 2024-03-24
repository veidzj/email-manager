import streamlit as st
from utils import *

def settings_page():
  st.markdown('# Settings')

  email = st.text_input('Write your email:')
  st.button('Save', key='save_email', on_click=save_email, args=(email,))
  key = st.text_input('Write your email key:')
  st.button('Save', key='save_keyl', on_click=save_email_key, args=(key,))

def save_email(email):
  settings_folder.mkdir(exist_ok=True)
  with open(settings_folder / 'user_email.txt', 'w') as file:
    file.write(email)

def save_email_key(key):
  settings_folder.mkdir(exist_ok=True)
  with open(settings_folder / 'user_email_key.txt', 'w') as file:
    file.write(key)

def read_email():
  settings_folder.mkdir(exist_ok=True)
  if (settings_folder / 'user_email.txt').exists():
    with open(settings_folder / 'user_email_key.txt', 'r') as file:
      return file.read()
  return ''

def read_email_key():
  settings_folder.mkdir(exist_ok=True)
  if (settings_folder / 'user_email_key.txt').exists():
    with open(settings_folder / 'user_email_key.txt', 'r') as file:
      return file.read()
  return ''
