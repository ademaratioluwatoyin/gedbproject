from email.policy import default
from settings import SUB_INDUSTRIES_LIST, dbms
import streamlit as st
import json
# set page format         
st.title('GetEquity Databank Ventures Dasboard')
st.write('A dashboard to onboard details of portfollioo companies into the databank repository ')


if 'metrics' not in st.session_state:
    st.session_state.metrics = []
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'overview' not in st.session_state:
    st.session_state.overview = ""
if 'sub' not in st.session_state:
    st.session_state.sub = 0

st.header("Company Information")

company_name = st.text_input("Company name", value = st.session_state.name)
st.session_state.name =company_name
company_overview = st.text_area("Overview", value = st.session_state.overview)
st.session_state.overview = company_overview
sub_industry = st.selectbox("Sub industry", SUB_INDUSTRIES_LIST, index = st.session_state.sub)
st.session_state.sub = SUB_INDUSTRIES_LIST.index(sub_industry)


metrics = st.session_state.metrics
button = st.button("New metric")

if button : 
    metrics.append({'title' : "", 'info' : "", 'metric_type_index' : 0, 'metric_type' : "", 'metric_tag' : []  })
    st.session_state.metrics = metrics

if len(metrics) > 0 : 
    cols = st.columns(len(metrics))

    for i, col in enumerate(cols) : 
        met = metrics[i]
        title = col.text_input("Title", key = col, value = met["title"])
        info = col.text_input("Information", key = col, value = met["info"])
        metric_type= col.selectbox("Metric type",   ("Quantitative", "Qualitative"), key = col,  index = met["metric_type_index"])

        type_map = {"Quantitative" : 0,  "Qualitative" : 1}
        metric_tag = ''
        if metric_type == "Quantitative" : 
            metric_tag= col.multiselect("Select  Quantitative Metrics", ("Revenue", "Traction", "Market size", "Growth", "Funding", "Volume", "Competition", "Sales"), key = col, default = met["metric_tag"])
        clear = col.button("x", key = col)
        metrics[i] = {'title' : title, 'info' : info, 'metric_type' : metric_type, 'metric_tag' : metric_tag , 'metric_type_index' : type_map[metric_type] }

        st.session_state.metrics = metrics
        if clear  :
          
            metrics.pop(i) 
            st.session_state.metrics = metrics
            st.experimental_rerun()
        
st.write('\n')
doc = st.file_uploader(label = 'Additional Document')

st.write("\n\n\n\n")
add_to_db = st.button("Add to databank")

if add_to_db :
    added = dbms.insert_company(company_name, company_overview,sub_industry,json.dumps(metrics))
    if added : 
        company_name = ""
        company_overview = ""
        sub_industry = 0
        metrics = []
    else : 
        st.error('Something went wrong')