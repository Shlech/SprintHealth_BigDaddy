import streamlit as st

import page_configuration
import data_processor


PAGE_NAME = 'Load_Data'


def construct_page():
    construct_sidebar()

    st.title('Loading data file')
    data_processor.DATA_FILE = st.file_uploader('Upload data file', type=['.csv'])
    data_processor.upload_file_handler()

    if data_processor.DATA_FRAME is not None:
        st.header('Preview file', divider='gray')
        st.dataframe(data_processor.DATA_FRAME.head(100))


def construct_sidebar():
    st.sidebar.header('Load Data', divider='gray')
    st.sidebar.markdown('''
        - Download and preview the data file here.

        - We are expecting pre-processed data

        - After downloading the file, 
        make sure that you are using the data you intended 
        and proceed to view statistics in other sections.
        ''')


page_configuration.load_page_configs(PAGE_NAME)
page_configuration.configure_page()

construct_page()
