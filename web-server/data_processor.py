import streamlit as st
import pandas as pd


DATA_FILE = None
DATA_FRAME = None


def upload_file_handler():
    global DATA_FRAME

    if DATA_FILE is not None:
        DATA_FRAME = pd.read_csv(DATA_FILE, sep=';', header=1)
    else:
        DATA_FRAME = None
