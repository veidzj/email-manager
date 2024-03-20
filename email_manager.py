import streamlit as st


if not 'email_manager_page' in st.session_state:
  st.session_state.email_manager_page = 'home'

def change_page(page_name: str) -> None:
  st.session_state.email_manager_page = page_name

def home_page() -> None:
  st.markdown('# Email Manager')

def templates_page() -> None:
  st.markdown('# Templates')

  st.button('Add template', on_click=change_page, args=('add_template',))

def add_template_page() -> None:
  template_name = st.text_input('Template name:')
  template_text = st.text_area('Write the template text:', height=600)

def email_list_page() -> None:
  st.markdown('# Email List')

def settings_page() -> None:
  st.markdown('# Settings')



def main() -> None:
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
  elif st.session_state.email_manager_page == 'email_list':
    email_list_page()
  elif st.session_state.email_manager_page == 'settings':
    settings_page()

main()
