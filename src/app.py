import streamlit as st
import pandas as pd
from visualization import plot_distribution, plot_heatmap, plot_interactions
from summary import detect_column_types, data_summary
from column_selector import create_select_box, create_statistics
from preprocessing import fill_missing_data, replace_outliers, one_hot_encode

def load_data(uploaded_file) -> tuple:
    df = pd.read_csv(uploaded_file)
    summary_dict = data_summary(df)
    var_types = detect_column_types(df)

    return df, summary_dict, var_types

def display_dataset(df: pd.DataFrame, summary_dict: dict):
    st.write('## Dataset Preview')
    st.dataframe(df)
    st.write('### Overview')
    st.write(f'Number of rows: {summary_dict['Shape'][0]}')
    st.write(f'Number of columns: {summary_dict['Shape'][1]}')

def print_col_types(var_types: dict):
    def _print(col_names: list, col):
        if len(col_names) == 0:
            col.write('No columns found')
        else:
            col.write(col_names)
    
    col1, col2 = st.columns(2)
    col1.write('#### Numeric Columns')
    _print(var_types['numeric'], col1)
    col2.write('#### Categorical Columns')
    _print(var_types['categorical'], col2)
    col1.write('#### Datetime Columns')
    _print(var_types['datetime'], col1)
    col2.write('#### Other Columns')
    _print(var_types['other'], col2)

def variable_analysis(df: pd.DataFrame, var_types: dict, summary_dict: dict):
    st.write('## Variables')
    col_name = create_select_box(var_types)
    col_type = 'numeric' if col_name in var_types['numeric'] else 'categorical'
    
    st.write(f'#### Variable: {col_name}')
    st.write(f'Type: {col_type}')
    col1, col2 = st.columns([0.65, 0.35])
    fig = plot_distribution(df, col_name, col_type)
    col1.plotly_chart(fig)

    statistics_df = create_statistics(summary_dict, col_name)
    col2.write("### Column Statistics")
    col2.dataframe(statistics_df)

def interaction_analysis(df: pd.DataFrame, var_types: dict):
    st.write('## Relation between variables')
    st.write('Numeric vs numeric will result in a scatter plot, numeric vs categorical in box plots.')
    col1 = st.selectbox('Select y-axis variable', options=var_types['numeric'], index=0)
    col2 = st.selectbox('Select x-axis variable', options=var_types['numeric'] + var_types['categorical'], index=5)
    if col1 and col2:
        col2_type = 'numeric' if col2 in var_types['numeric'] else 'categorical'
        plot_interactions(df, col1, col2, col2_type)

def perform_preprocessing(df: pd.DataFrame, var_types: dict):
    df_copy = df.copy()

    st.write('## Preprocessing')
    st.write('#### Fill missing values')
    columns = st.multiselect('Choose columns', options=df.columns)
    if st.button('Fill'):
        df_copy = fill_missing_data(df_copy, columns)
    
    st.write('#### Replace Outliers')
    columns = st.multiselect('Choose columns', options=var_types['numeric'])
    if st.button('Replace'):
        df_copy = replace_outliers(df_copy, columns)

    st.write('#### Encode Categorical Columns')
    columns = st.multiselect('Choose columns', options=var_types['categorical'])
    if st.button('Encode'):
        df_copy = one_hot_encode(df, columns)
    
    @st.cache_data
    def convert_df(df: pd.DataFrame):
        return df.to_csv().encode("utf-8")
    
    csv = convert_df(df_copy)

    st.download_button('Download preprocessed data as CSV',
                       data=csv,
                       file_name='data_preprocessed.csv',
                       mime='text/csv')

st.title('Automated EDA Tool')
uploaded_file = st.file_uploader("Upload a CSV", type=["csv"])
if st.checkbox("Use sample dataset"):
    uploaded_file = 'data/sample.csv'

if uploaded_file:
    df, summary_dict, var_types = load_data(uploaded_file)
    
    display_dataset(df, summary_dict)
    print_col_types(var_types)
    variable_analysis(df, var_types, summary_dict)
    plot_heatmap(df, var_types['numeric'])
    interaction_analysis(df, var_types)
    perform_preprocessing(df, var_types)