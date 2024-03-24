import streamlit as st
from utils import *

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
