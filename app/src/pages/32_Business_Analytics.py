'''
This page is for business owners, specifically: As a business owner,
I want to view a count of how many students viewed my discounts,
so that I can identify which ones attract attention.

Features:
- Simulates discounts with "views".
- Shows a table with view counts.
'''

import logging
import streamlit as st
from modules.nav import SideBarLinks
import pandas as pd

logger = logging.getLogger(__name__)
st.set_page_config(layout="wide")
SideBarLinks()

st.title("Business Analytics Dashboard")
st.write("Below are the current stats for your posted discounts.")

# Simulated analytics data
discount_data = [
    {"Discount Code": "COFFEE20", "Item": "Latte", "Views": 124},
    {"Discount Code": "MUFFIN10", "Item": "Blueberry Muffin", "Views": 87},
    {"Discount Code": "ESPRESSO25", "Item": "Espresso", "Views": 193}
]

df = pd.DataFrame(discount_data)
st.dataframe(df, use_container_width=True)