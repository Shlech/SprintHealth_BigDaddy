import streamlit as st

import page_configuration

PAGE_NAME = 'stat_page'


def construct_page():
    st.button('Some')


page_configuration.load_page_configs(PAGE_NAME)
page_configuration.configure_page()
construct_page()
