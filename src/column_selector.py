import streamlit as st
import pandas as pd

def create_select_box(var_types: dict) -> str:
    options = var_types['numeric'] + var_types['categorical']
    col_name = st.selectbox("Select a column", options=options)

    return col_name

def clear_statistics(statistics_dict: dict) -> dict:
    for key, value in statistics_dict.items():
        if isinstance(value, float) and value.is_integer():
            statistics_dict[key] = int(value)
        
    return statistics_dict

def create_statistics(summary_dict: dict, col_name: str) -> dict:
    statistics_dict = summary_dict['Statistics'][col_name]
    number_of_missing = summary_dict['Missing Values'][col_name]
    statistics_dict['Missing'] = number_of_missing
    statistics_dict['Missing %'] = round(number_of_missing * 100 / statistics_dict['count'], 2)
    
    return pd.DataFrame(clear_statistics(statistics_dict).items(), columns=['Statistic', 'Value'])