# Import necessary librariries
import streamlit as st
import pandas as pd
import numpy as np
import hydralit_components as hc
import requests
import inspect
from streamlit_lottie import st_lottie
from numerize import numerize
from itertools import chain
import plotly.graph_objects as go
import plotly.express as px
import joblib
import statsmodels.api as sm
import sklearn
from PIL import Image
import matplotlib.pyplot as plt


# data = pd.read_csv("/data/Data_HA.csv")

# Set Page Icon,Title, and Layout
st.set_page_config(layout="wide",  page_title = "The Impact of Antidepressants")

# Load css style file from local disk
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
# Load css style from url
def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">',unsafe_allow_html = True)

# Display lottie animations
def load_lottieurl(url):
    # get the url
    r = requests.get(url)
    # if error 200 raised return Nothing
    if r.status_code !=200:
        return None
    return r.json()
# Navigation Bar Design
menu_data = [
{'label':"Home", 'icon': "bi bi-house"},
{'label':"EDA", 'icon': "bi bi-clipboard-data"},
{'label':'Overview', 'icon' : "bi bi-graph-up-arrow"},
{'label':'Analysis', 'icon' : "bi bi-file-person"},
{'label':'Application', 'icon' : "fa fa-brain"}]

over_theme = {'txc_inactive': 'white','menu_background':'#87CEFA', 'option_active':'white'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    hide_streamlit_markers=True,
    sticky_nav=True,
    sticky_mode='sticky',
)
# Home Page
if menu_id == "Home":
    st.markdown("<h2 style='text-align: center; color: #87CEFA;'>The Impact of Antidepressants <i class='bi bi-heart-fill' style='color: #87CEFA;'></i></h2>", unsafe_allow_html=True)
   
    # Display Introduction
    st.image('image.png')
    st.markdown("""
    <article>
    <div class="container">
        <div class="column">
        </div>
        <div class="column">
        <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;">
            Depression is a widespread mental health condition characterized by persistent sadness and loss of interest. Antidepressants have transformed the treatment landscape by targeting brain chemicals to alleviate symptoms. These medications aim to restore balance and enhance mood, providing hope for those affected. However, their effectiveness varies, and finding the right medication and dosage may take time. Antidepressants are most effective when used alongside therapy and lifestyle adjustments. Together, these approaches offer a comprehensive path towards recovery and improved mental well-being for individuals with depression.
        </p>
        </div>
    </div>
    </article>
    """, unsafe_allow_html=True)

if menu_id == "EDA":
    st.markdown("<h2 style='text-align: center; color: #87CEFA;'> Data Exploration <i class='bi bi-heart-fill' style='color: #87CEFA;'></i></h2>", unsafe_allow_html=True)
   
#    # Display EDA
#     st.image('image1.png', width=400, use_column_width=False, clamp=False)
#     st.markdown("""
#     <article>
#     <div class="container">
#         <div class="column">
#         </div>
#         <div class="column">
#         <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;">
#             It is a good practice to understand the data first and try gather as many insights from it. 
#             EDA is all about making sense of data in hand,before getting them dirty with it.
#         </p>
#         </div>
#     </div>
#     </article>
#     """, unsafe_allow_html=True)
# Display EDA
    st.markdown("""
    <article>
    <div style="display: flex; flex-direction: row-reverse; align-items: center;">
        <div>
        <p class="f5 f4-ns lh-copy measure mb4" style="text-align: justify;">
            It is a good practice to understand the data first and try gather as many insights from it. 
            EDA is all about making sense of data in hand, before getting them dirty with it.
        </p>
        </div>
        <div>
        <img src="/Users/macpro/Desktop/Roula/HealthCare Analytics/streamlit/image1.png" alt="Image" width="400" style="margin-right: 20px;">
        </div>
    </div>
    </article>
    """, unsafe_allow_html=True)


