# importing libraries to be used
from django.conf import settings
from settings import *
import streamlit as st
import pandas as pd
from util import *
from visuals import *


# set page url, icon etc
st.set_page_config(
     page_title="Get Equity Data BAnk",
     page_icon="🧊",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={

 'About': '''Objective of this prototype is to provide robust data aggregation and statistics to bolster decision making and trend analysis for seasoned investors or VC and even retail investors on the platform.
         https://www.getequity.io
         ''' }
 )



# set page format         
st.title('GetEquity Databank')
st.write('Objective of this prototype is to provide robust data aggregation and statistics to bolster decision making and trend analysis for seasoned investors or VC and even retail investors on the platform. ')


#Side bar
st.sidebar.header('Search Prompt')


sub_industry = st.sidebar.selectbox("Select Fintech Sub-Industry", SUB_INDUSTRIES_LIST)

# companies = {"Payment" : tuple([str(c) for c in PAYMENTS]), "Savings" : ("Piggyvest", "Cowrywise"), "Lending" : ("Carbon", "FairMoney") , "Investech" : ("GetEquity", "Trove")}

try :
    comps= tuple([str(c) for c in SUB_INDUSTRIES_COMPANIES[sub_industry]])
    
    if comps :
        company_selection = st.sidebar.selectbox(
            "Select company", comps+ ("Other",))
    else  :
        company_selection = st.sidebar.selectbox(
            "Select company", ('Other',))
except : 
    company_selection = st.sidebar.selectbox(
            "Select company", ('Other',))


if company_selection == "Other" : 
    custom_sel = st.sidebar.text_input("Input company")

metric_type = st.sidebar.selectbox("Select  Metrics Type", ("Quantitative", "Qualitative"))

show_viz = False

if metric_type == "Quantitative" : 
    metrics = st.sidebar.multiselect("Select  Quantitative Metrics", ("Revenue", "Traction", "Market size", "Growth", "Funding", "Volume", "Competition", "Sales"))

if metric_type == "Quantitative" :
    show_viz = st.sidebar.checkbox("Show visualizations")


search = st.sidebar.button("Search")



# Results

c = st.container()

if not company_selection == "Other" : 

    similar_companies = SUB_INDUSTRIES_COMPANIES[sub_industry]
    company = [com for com in similar_companies if str(com) == company_selection][0]
    
    c.header(company.name)
    c.write(company.overview)

    c.subheader(f"{metric_type} Information")
    for i, info in enumerate(company.infos) : 
        if info["metric_type"] == metric_type : 
            c.markdown(f"##### {info['title']}")
            c.write(f"{info['info']}")

    if metric_type == "Quantitative" and show_viz :  
        show_visuals()
else : 
    company_selection = custom_sel

if search:
    search_cont = st.container()
    search_cont.subheader("Search Reference")
    metrics = ', '.join(metrics) 
    search_query = f'{metrics} metrics on {company_selection}'
    print(search_query)
    try: 
        response = get_results(search_query)
        response = response['organic_results']
    
        res = pd.DataFrame(response)


        for result in response:
            result_cont = search_cont.container()
            result_cont.markdown(f"##### [{result['title']}]({result['link']})")
            result_cont.caption(result['snippet'])
            # result_cont.write(result)
    
    except Exception as e:
        search_cont.write("An exception occurred")
        search_cont.write(e)


