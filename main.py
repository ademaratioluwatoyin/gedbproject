# importing libraries to be used
from setup import PAYMENTS, SUB_INDUSTRIES
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


sub_industry = st.sidebar.selectbox("Select Fintech Sub-Industry", ("Payment", "Savings", "Lending", "Investech"))

# companies = {"Payment" : tuple([str(c) for c in PAYMENTS]), "Savings" : ("Piggyvest", "Cowrywise"), "Lending" : ("Carbon", "FairMoney") , "Investech" : ("GetEquity", "Trove")}

try :
    comps= tuple([str(c) for c in SUB_INDUSTRIES[sub_industry]])
    
    if comps :
        company_selection = st.sidebar.selectbox(
            "Select company", comps+ ("Others",))
    else  :
        company_selection = st.sidebar.selectbox(
            "Select company", ('Other',))
except : 
    company_selection = st.sidebar.selectbox(
            "Select company", ('Other',))


if company_selection == "Other" : 
    st.sidebar.text_input("Input company")

metric_type = st.sidebar.selectbox("Select  Metrics Type", ("Quantitative", "Qualitative"))

show_viz = st.sidebar.checkbox("Show visualizations")
st.sidebar.empty()
# if metric_type == "Quantitative" : 
#     metrics = st.sidebar.multiselect("Select  Quantitative Metrics", ("Revenue", "Traction", "Market size", "Growth", "Funding", "Volume", "Competition", "Sales"))
# else : 
#     metrics = st.sidebar.multiselect("Select  Qualitative Metrics", ("Quantitative", "Qualitative"))  


search = st.sidebar.button("Search")



# Results

c = st.container()

if company_selection != "Other" : 
    similar_companies = SUB_INDUSTRIES[sub_industry]
    company = [com for com in similar_companies if str(com) == company_selection][0]
    
    c.header(company.name)
    c.write(company.overview)

    c.subheader(f"{metric_type} Information")
    for i, info in enumerate(company.infos) : 
        if info.type == metric_type : 
            c.markdown(f"##### {info.title}")
            c.caption(f"{info.description}")
            

    show_visuals()

if search:
    search_cont = st.container()
    search_cont.subheader("Search Reference")
    # metrics = ', '.join(metrics) 
    search_query = f'{metric_type} metrics on {company_selection}'
    
    try: 
        response = get_results(search_query)
        response = response['organic_results']
    
        res = pd.DataFrame(response)
        # st.table(res)
        # st.dataframe(res)

        for result in response:
            result_cont = search_cont.container()
            result_cont.markdown(f"##### [{result['title']}]({result['link']})")
            result_cont.caption(result['snippet'])
            # result_cont.write(result)
    
    except Exception as e:
        search_cont.write("An exception occurred")
        search_cont.write(e)


