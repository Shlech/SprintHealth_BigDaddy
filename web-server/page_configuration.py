import streamlit as st
import json

INIT_CONFIG_FILE_PATH_TEMPLATE = 'cfg/{0}-init-cfg.json'
CSS_CONFIG_FILE_PATH_TEMPLATE = 'cfg/{0}-css-cfg.txt'

INIT_CFG = {}
CSS_CFG = ''


def load_page_configs(page_name: str):
    global INIT_CFG, CSS_CFG

    init_cfg_file = open(INIT_CONFIG_FILE_PATH_TEMPLATE.format(page_name), 'r')
    css_cfg_file = open(CSS_CONFIG_FILE_PATH_TEMPLATE.format(page_name), 'r')

    INIT_CFG = json.loads(init_cfg_file.read())
    CSS_CFG = css_cfg_file.read()


def configure_page():
    st.set_page_config(page_title=INIT_CFG.get('page_title'),
                       layout=INIT_CFG.get('layout'))

    st.markdown(CSS_CFG, unsafe_allow_html=True)
