
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
    fig = make_subplots(rows = 1, cols = 2, subplot_titles=('Rounds by Year', 'Rounds by Series'), horizontal_spacing=0.1)
    
    # create a bar charts
    barchart1 = px.bar(df, x = 'Date', y = 'Round_size_in_millions')
    barchart2 = px.bar(df, x = 'Series', y = 'Round_size_in_millions')
    
    # add to figure
    fig.add_trace(barchart1['data'][0], row = 1, col = 1)
    fig.add_trace(barchart2['data'][0], row =1, col = 2)
    
    fig.update_layout(height = 600, 
                     width = 1000, 
                     title_text = 'Round Size in Million $', 
                     title_font_color = 'white', 
                     title_font_family = 'Times New Roman',
                     title_font_size = 30,
                     title_pad_l = 100)
    
    # updating yaxis of subplots
    fig.update_yaxes(title_text = 'Round Size in Million $', row = 1, col = 1)
    fig.update_yaxes(title_text = 'Round Size in Million $', row = 1, col = 2)
    
    #updating xaxis of subplots
    fig.update_xaxes(title_text = 'Date', row = 1, col = 1)
    fig.update_xaxes(title_text = 'Series', row = 1, col = 2)
    
    #show charts
    st.write(fig)


    # card
    card = go.Figure()
    card.add_trace(go.Indicator(
        mode = "number",
        value = 16.4,
        number = {'prefix': "$"},
        domain = {'x': [0, 0.5], 'y': [0.8, 1]},
        title = {'text' : 'Flutterwave\'s Annual Revenue in M'}))
    
    card.add_trace(go.Indicator(
        mode = 'number',
        value = df['Round_size_in_millions'].sum(),
        number = {'prefix' : '$'},
        domain = {'x': [0.6, 1], 'y': [0.8, 1]},
        title = {'text': 'Total Round Size in M'}))
    

    st.write(card)
    #figure = make_subplots(rows = 2, cols = 1)
    
    
   

