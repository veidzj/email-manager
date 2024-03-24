from pathlib import Path
import streamlit as st
from utils import *
from templates_page import templates_page, add_template_page
from email_list_page import email_list_page, add_list_page
from settings_page import settings_page, read_email, read_email_key

def home_page():
  st.markdown('# Email Manager')

  current_addressees = st.session_state.current_addressees
  current_title = st.session_state.current_title
  current_body = st.session_state.current_body

  addressees = st.text_input('Email addressees:', value=current_addressees)
  title = st.text_input('Email title:', value=current_title)
  body = st.text_area('Email body:', value=current_body, height=400)
  col1, _, col3 = st.columns(3)
  col1.button('Send email', use_container_width=True, on_click=send_email_home, args=(addressees, title, body))
  col3.button('Clear', use_container_width=True, on_click=clear_home)

  st.session_state.current_addressees = addressees
  st.session_state.current_title = title
  st.session_state.current_body = body

def clear_home():
  st.session_state.current_addressees = ''
  st.session_state.current_title = ''
  st.session_state.current_body = ''

def send_email_home(addressees, title, body):
  # user_email = st.secrets['USER_EMAIL']
  # app_password = st.secrets['APP_PASSWORD']
  addressees = addressees.replace(' ', '').split(',')
  user_email = read_email()
  app_password = read_email_key()
  if user_email == '':
    st.error('Add your email in the settings page')
  elif app_password == '':
    st.error('Add your email key in the settings page')
  else:
    send_email(user_email, addressees, title, body, app_password)

def main():
  init()

  st.sidebar.button('Email Manager', use_container_width=True, on_click=change_page, args=('home',))
  st.sidebar.button('Templates', use_container_width=True, on_click=change_page, args=('templates',))
  st.sidebar.button('Email List', use_container_width=True, on_click=change_page, args=('email_list',))
  st.sidebar.button('Settings', use_container_width=True, on_click=change_page, args=('settings',))

  if st.session_state.email_manager_page == 'home':
    home_page()
  elif st.session_state.email_manager_page == 'templates':
    templates_page()
  elif st.session_state.email_manager_page == 'add_template':
    add_template_page()
  elif st.session_state.email_manager_page == 'edit_template':
    template_name_edit = st.session_state.template_name_edit
    template_text_edit = st.session_state.template_text_edit
    add_template_page(template_name_edit, template_text_edit)
  elif st.session_state.email_manager_page == 'email_list':
    email_list_page()
  elif st.session_state.email_manager_page == 'add_list':
    add_list_page()
  elif st.session_state.email_manager_page == 'edit_list':
    list_name_edit = st.session_state.list_name_edit
    list_text_edit = st.session_state.list_text_edit
    add_list_page(list_name_edit, list_text_edit)
  elif st.session_state.email_manager_page == 'settings':
    settings_page()

if __name__ == '__main__':
  main()
