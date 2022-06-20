import streamlit as st
import pandas as pd
import numpy as np

import urllib.parse
import urllib.request
import ssl
import json
ssl._create_default_https_context = ssl._create_unverified_context

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

def get_results(query) :
    # Urlencode the query string
    q = urllib.parse.quote_plus(query)

    # Create the query URL.
    query = "https://api.scraperbox.com/google"
    query += "?token=%s" % "D370BCDF7D5F8E66BFC5ABC9F8A33E14"
    query += "&q=%s" % q
    query += "&proxy_location=ng"

    # Call the API.
    request = urllib.request.Request(query)

    raw_response = urllib.request.urlopen(request).read()
    raw_json = raw_response.decode("utf-8")
    response = json.loads(raw_json)

    # Print the first result title
    return response

if search :
    search_query = f'{metric_type} metrics on {sub_industry} Fintech industry in Nigeria '

    for metric in metrics:
        search_query += search_query + " , " + metric 

    print(search_query)
    
    try:
      response = get_results(search_query)

      for result in response['organic_results']:
        st.write(result)
        print(response)
    except Exception as e:
      print('An exception occurred')
      print(e)
    

    
