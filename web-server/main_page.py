import streamlit as st
import json

import page_configuration


PAGE_NAME = 'main_page'


def init_navigation():
    navigation = [st.Page(PAGE_NAME + '.py')]

    for page in page_configuration.INIT_CFG.get('subpages'):
        current_page = st.Page(page)
        navigation.append(current_page)

    st.navigation(navigation)


def construct_page():
    st.sidebar.title('Sprint Health')
    st.file_uploader('Upload data file')


page_configuration.load_page_configs(PAGE_NAME)
page_configuration.configure_page()

#init_navigation()
construct_page()
