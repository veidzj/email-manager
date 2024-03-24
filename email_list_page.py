import streamlit as st
from utils import *

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
