import streamlit as st
from modules.nav import SideBarLinks
import pandas as pd

# Page config and sidebar links
st.set_page_config(page_title="Business Owner Dashboard", layout="wide")
SideBarLinks(show_home=True)

# Page title
st.title("Welcome, Beth! 👋")
st.subheader("Your Business Dashboard")

# --- Quick Actions ---
st.markdown("### 📌 Quick Actions")
col1, col2, col3 = st.columns(3)
with col1:
    st.button("➕ Add New Discount")
with col2:
    st.button("✏️ Update Discount Terms")
with col3:
    st.button("🗑️ Deactivate Expired Discounts")

# --- Analytics Section ---
st.markdown("### 📊 Discount Performance")

# Simulated data from 32_Business_Analytics.py
discount_data = [
    {"Discount Code": "COFFEE20", "Item": "Latte", "Views": 124},
    {"Discount Code": "MUFFIN10", "Item": "Blueberry Muffin", "Views": 87},
    {"Discount Code": "ESPRESSO25", "Item": "Espresso", "Views": 193}
]

df = pd.DataFrame(discount_data)
st.dataframe(df, use_container_width=True)

# --- Targeting Insights ---
st.markdown("### 🎯 College Engagement Insights")
st.success("You have high interest from: Northeastern University and Boston University. Consider targeting new offers here!")

# --- Footer ---
st.markdown("---")
st.caption("CampusPerks • Empowering small businesses to connect with students")