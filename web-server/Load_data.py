import streamlit as st

import page_configuration
import data_processor


PAGE_NAME = 'Load_data'


def construct_page():
    st.sidebar.header('Sprint Health')
    st.title('Loading data file')
    data_processor.DATA_FILE = st.file_uploader('Upload data file', type=['.csv'])
    data_processor.upload_file_handler()

    if data_processor.DATA_FRAME is not None:
        st.header('Preview file', divider='gray')
        st.dataframe(data_processor.DATA_FRAME.head(100))


page_configuration.load_page_configs(PAGE_NAME)
page_configuration.configure_page()

construct_page()
