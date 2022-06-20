#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 13:17:43 2022

@author: user
"""

# imporrting libraries to be used
import streamlit as st
from serpapi import GoogleSearch

# set page url, icon etc
st.set_page_config(
     page_title="Get Equity Data BAnk",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={

 'About': '''Objective of this prototype is to provide robust data aggregation and statistics to bolster decision making and trend analysis for seasoned investors or VC and even retail investors on the platform.
         https://www.getequity.io
         '''     }
 )

# set page format         
st.title('GetEquity Databank')
st.write('Objective of this prototype is to provide robust data aggregation and statistics to bolster decision making and trend analysis for seasoned investors or VC and even retail investors on the platform. ')

st.header('Search Mining')

sub_industry = st.selectbox("Select  Fintech Sub-Industry", ("Payment", "Savings", "Lending", "Investech"))

metric_type = st.selectbox("Select  Metrics Type", ("Quantitative", "Qualitative"))

if metric_type == "Quantitative" : 
    metrics = st.multiselect("Select  Quantitative Metrics", ("Revenue", "Traction", "Market size", "Growth", "Funding", "Volume", "Competition", "Sales"))
else : 
    metrics = st.multiselect("Select  Qualitative Metrics", ("Quantitative", "Qualitative"))  


search = st.button("Search")

def get_results(query):
    
    params = {
      "q": query,
      "location": "Lagos, Lagos, Nigeria",
      "hl": "en",
      "gl": "ng",
      "google_domain": "google.com",
      "api_key": "7f7342e8d4bfe676ef4d77880ef14d70e2d7cad3c9059ec57ab8e62baf1c5123"
    }

    search = GoogleSearch(params)
    response = search.get_dict()
    return response

if search:
    metrics = ', '.join(metrics) 
    search_query = f'{metrics} {metric_type} metrics on {sub_industry} Fintech industry in Nigeria'
    
    st.write(search_query)
    
    try: 
        response = get_results(search_query)
        response = response['organic_results']
        for result in response:
            st.write(result)
    
    except Exception as e:
        st.write("An exception occurred")
        st.write(e)
    