import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np

def plot_distribution(df: pd.DataFrame, col_name: str, col_type: str):
    if col_type == 'categorical':
        df_grouped = df.groupby(by=col_name).size().reset_index(name='counts')
        df_grouped[col_name] = df_grouped[col_name].astype('category')
        fig = px.bar(df_grouped, x=col_name, y='counts')
        fig.update_layout(xaxis_type='category')

    if col_type == 'numeric':
        plot_type = st.selectbox(label='Choose plot type', options=['Histogram', 'Box Plot'])
        match plot_type:
            case 'Histogram':
                fig = px.histogram(df, x=col_name, title=f'Histogram of {col_name}')
            case 'Box Plot':
                fig = px.box(df, x=col_name, title=f'Box plot of {col_name}')
             
    return fig

def plot_heatmap(df: pd.DataFrame, numerical_columns: list):
    st.write('### Correlation heatmap')
    df_numerical = df[numerical_columns]
    corr = df_numerical.corr().round(2)
    
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    
    corr_viz = corr.mask(mask).dropna(how='all').dropna(how='all', axis='columns')
    fig = px.imshow(corr_viz, text_auto=True, color_continuous_scale='Viridis')\
        .update_xaxes(showgrid=False)\
        .update_yaxes(showgrid=False)
    
    st.plotly_chart(fig)

def plot_interactions(df: pd.DataFrame, col1: str, col2: str, col2_type: str):
    if col2_type == 'numeric':
        fig = px.scatter(df, y=col1, x=col2)
    elif col2_type == 'categorical':
        fig = px.box(df, y=col1, x=col2,
                     title=f'Box plot of {col1} by {col2}')\
                     .update_layout(xaxis_type='category')
        
    
    st.plotly_chart(fig)