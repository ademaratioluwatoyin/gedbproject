
# importing libraries
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show_visuals():
    # loading dataframe
    df = pd.read_csv('data.csv')
     
    # create subplots
    #fig = make_subplots(rows = 1, cols = 2)
    # create a bar chart
    barchart = px.bar(df, x = 'Date', y = 'Round_size_in_millions', title = 'Rounds by Year')
    # set axes
    barchart.update_yaxes(title_text = 'Round size in Million $')
    barchart.update_xaxes(title_text = 'Date')
    
    st.write(barchart)
    
    
    st.write('Flutterwave\'s Annual Revenue')
    st.write('$16.4 Million')
    
# =============================================================================
#     figure = make_subplots(rows = 2, cols = 1)
#     # annual revenue card
#     fig1 = go.Indicator(
#         mode = "number",
#         value = 16.4,
#         number = {'prefix': "$"},
#         domain = {'x': [0, 1], 'y': [0, 1]},
#         title = {'text' : 'Flutterwave\'s Annual Revenue in M'})
#     #fig1.update_layout(width = 400, height = 200)
#     
#     # total funding card
#     fig2 = go.Indicator(
#         mode = 'number',
#         value = df['Round_size_in_millions'].sum(),
#         domain = {'x': [0, 1], 'y': [0, 1]},
#         title = {'text': 'Total funding raised'})
#     #fig.update_layout(paper_bgcolor = "white")
#     #fig2.update_layout(width = 400, height = 200)
#     
#     figure.add_trace(fig1, row = 1, col = 1)
#     figure.add_trace(fig2, row = 2, col = 1)
#     
#     #fig.add_trace(barchart, row = 1, col = 1)
#     #fig.add_trace(figure, row = 1, col = 2)
#     # show cards
#     st.write(figure)
# =============================================================================
