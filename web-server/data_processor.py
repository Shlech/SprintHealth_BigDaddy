import streamlit as st
import pandas as pd
from datetime import datetime

DATA_FILE = None
DATA_FRAME = None


def upload_file_handler():
    global DATA_FRAME

    if DATA_FILE is not None:
        DATA_FRAME = pd.read_csv(DATA_FILE, sep=';')


def get_sprints_names() -> list: # TODO Сделать возврат списка имен спринтов
    if DATA_FRAME is None:
        return []

    return ['sprint 1', 'sprint 2']


def get_string_sprint_period(sprint_name: str) -> str: # TODO Сделать возврат периода указанного спринта в строке
    return '01.01.2024 – 14.01.2024'

def get_sprint_period(sprint_name: str) -> tuple: # TODO Сделать возврат преиода в формате даты для указанного спринта
    return (datetime(2024, 1, 1),
            datetime(2024, 1, 14))

def get_entire_sprint_statistic(sprint_name: str):  # TODO Сделать возврат статистики по всему периоду спринта. Для стэковой гистограммы
    sprint_name = 'qwe'

    return pd.DataFrame([
        {'sprint': sprint_name, 'category': '1. В работе', 'value': 30},
        {'sprint': sprint_name, 'category': '2. Выполнено', 'value': 25},
        {'sprint': sprint_name, 'category': '3. Закрыто', 'value': 45}
    ])


def get_backlog_change_percentage(sprint_name):
    return '15.3%'


def get_blocked_tasks_percentage(sprint_name):
    return '0.1%'

