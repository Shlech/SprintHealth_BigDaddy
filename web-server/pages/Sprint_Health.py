import streamlit as st
from datetime import datetime

import page_configuration
import data_processor

PAGE_NAME = 'Sprint_Health'


def construct_page():
    construct_sidebar()

    st.title('Sprints statistics')
    st.header('Select the desired sprint')

    sprint_name = st.selectbox(label='Available sprints',
                              placeholder='Select sprint',
                              options=data_processor.get_sprints_names())

    #if data_processor.DATA_FRAME is not None: # TODO потом все что ниже должно уйти под if
    st.divider()
    display_sprint_name(sprint_name)
    display_sprint_period(sprint_name)
    st.divider()

    st.header('General summary', divider='gray')

    display_entire_sprint_statistics('qwer')
    display_general_criteria(sprint_name)
    st.divider()

    st.header('Sprint segment', divider='gray')
    display_sprint_section_slider(sprint_name)


def display_sprint_name(sprint_name):
    if sprint_name is None:
        sprint_name = ''

    st.markdown('### Sprint: ' + sprint_name)


def display_sprint_period(sprint_name):
    st.markdown('### Period: ' + data_processor.get_string_sprint_period(sprint_name))


def display_entire_sprint_statistics(sprint: str):
    sprint_stat = data_processor.get_entire_sprint_statistic(sprint)

    display_stacked_bar_plot(sprint_stat)


def display_stacked_bar_plot(sprint_stat):
    st.bar_chart(sprint_stat, y="value", x='sprint',
                 y_label='', x_label='',
                 color='category', horizontal=True, stack='normalize', height=250)


def construct_sidebar():
    st.sidebar.header('Sprint Health', divider='gray')
    st.sidebar.markdown('''
        - Select the desired sprint and get a summary of it
        ''')


def display_general_criteria(sprint_name: str):
    st.markdown('#### Backlog changes: ' + data_processor.get_backlog_change_percentage(sprint_name))
    st.markdown('#### Blocked tasks: ' + data_processor.get_blocked_tasks_percentage(sprint_name))


def display_sprint_section_slider(sprint_name):
    sprint_period = data_processor.get_sprint_period(sprint_name)

    period = st.slider(
        'Select a period for analysis',
        min_value=sprint_period[0],
        max_value=sprint_period[1],
        value=sprint_period,
        format='MM/DD/YY - hh:mm',
    )



page_configuration.load_page_configs(PAGE_NAME)
page_configuration.configure_page()
construct_page()
