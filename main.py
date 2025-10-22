import streamlit as st
import os

# ✅ Set Google API key from Streamlit secrets
API_KEY = st.secrets["google"]["api_key"]
os.environ["GOOGLE_API_KEY"] = API_KEY

# Now import the rest
from web_functions import load_data
from Tabs import diagnosis, home, result, kc, talk2doc

# Configure the app
st.set_page_config(
    page_title='Diabetes Prediction System',
    page_icon='🥯',
    layout='wide',
    initial_sidebar_state='auto'
)

Tabs = {
    "Home": home,
    "Ask Queries": talk2doc,
    "Diagnosis": diagnosis,
    "Result": result,
    "Knowledge Center": kc
}

st.sidebar.title('Navigation')
page = st.sidebar.radio("Page", list(Tabs.keys()))
st.sidebar.info('Made BY Divya')

df, X, y = load_data()

if page in ["Diagnosis"]:
    Tabs[page].app(df, X, y)
else:
    Tabs[page].app()
