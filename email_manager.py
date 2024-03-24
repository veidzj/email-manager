import os
from pathlib import Path
import streamlit as st
from utils import send_email

current_folder = Path(__file__).parent
templates_folder = current_folder / 'templates'
email_list_folder = current_folder / 'email_list'

def init():
  if not 'email_manager_page' in st.session_state:
    st.session_state.email_manager_page = 'home'
  if not 'current_addressees' in st.session_state:
    st.session_state.current_addressees = ''
  if not 'current_title' in st.session_state:
    st.session_state.current_title = ''
  if not 'current_body' in st.session_state:
    st.session_state.current_body = ''

def change_page(page_name: str):
  st.session_state.email_manager_page = page_name

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
  user_email = st.secrets['USER_EMAIL']
  app_password = st.secrets['APP_PASSWORD']
  print(user_email)
  print(app_password)
  send_email(user_email, addressees, title, body, app_password)

def templates_page():
  st.markdown('# Templates')
  st.divider()

  for file in templates_folder.glob('*.txt'):
    file_name = file.stem.replace('_', ' ').upper()
    col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
    col1.button(file_name, key=f'{file_name}', use_container_width=True, on_click=use_template, args=(file_name,))
    col2.button('EDIT', key=f'edit_{file_name}', use_container_width=True, on_click=edit_template, args=(file_name,))
    col3.button('DELETE', key=f'delete_{file_name}', use_container_width=True, on_click=delete_template, args=(file_name,))

  st.divider()
  st.button('Add template', on_click=change_page, args=('add_template',))

def add_template_page(template_name='', template_text=''):
  template_name = st.text_input('Template name:', value=template_name)
  template_text = st.text_area('Write the template text:', value=template_text, height=600)
  st.button('Save', on_click=save_template, args=(template_name, template_text))

def save_template(name, text):
  templates_folder.mkdir(exist_ok=True)
  file_name = name.replace(' ', '_').lower() + '.txt'
  with open(templates_folder / file_name, 'w', encoding='utf-8') as file:
    file.write(text)
  change_page('templates')

def use_template(name):
  file_name = name.replace(' ', '_').lower() + '.txt'
  with open(templates_folder / file_name) as file:
    file_text = file.read()
  st.session_state.current_body = file_text
  change_page('home')

def delete_template(name):
  file_name = name.replace(' ', '_').lower() + '.txt'
  (templates_folder / file_name).unlink()

def edit_template(name):
  file_name = name.replace(' ', '_').lower() + '.txt'
  with open(templates_folder / file_name) as file:
    file_text = file.read()
  st.session_state.template_name_edit = name
  st.session_state.template_text_edit = file_text
  change_page('edit_template')

def email_list_page():
  st.markdown('# Email List')
  st.divider()

  for file in email_list_folder.glob('*.txt'):
    file_name = file.stem.replace('_', ' ').upper()
    col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
    col1.button(file_name, key=f'{file_name}', use_container_width=True, on_click=use_list, args=(file_name,))
    col2.button('EDIT', key=f'edit_{file_name}', use_container_width=True, on_click=edit_list, args=(file_name,))
    col3.button('DELETE', key=f'delete_{file_name}', use_container_width=True, on_click=delete_list, args=(file_name,))

  st.divider()
  st.button('Add List', on_click=change_page, args=('add_list',))

def add_list_page(list_name='', list_emails=''):
  list_name = st.text_input('List name:', value=list_name)
  list_emails = st.text_area('Write the emails separated by commas:', value=list_emails, height=600)
  st.button('Save', on_click=save_list, args=(list_name, list_emails))

def use_list(name):
  file_name = name.replace(' ', '_').lower() + '.txt'
  with open(email_list_folder / file_name) as file:
      file_text = file.read()
  st.session_state.current_addressees = file_text
  change_page('home')

def save_list(name, text):
  email_list_folder.mkdir(exist_ok=True)
  file_name = name.replace(' ', '_').lower() + '.txt'
  with open(email_list_folder / file_name, 'w', encoding='utf-8') as file:
    file.write(text)
  change_page('email_list')

def delete_list(name):
  file_name = name.replace(' ', '_').lower() + '.txt'
  (email_list_folder / file_name).unlink()

def edit_list(name):
  file_name = name.replace(' ', '_').lower() + '.txt'
  with open(email_list_folder / file_name) as file:
    file_text = file.read()
  st.session_state.list_name_edit = name
  st.session_state.list_text_edit = file_text
  change_page('edit_list')

def settings_page():
  st.markdown('# Settings')



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

main()
