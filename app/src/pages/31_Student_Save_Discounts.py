'''
This page is for users, specifically: As a student, I want to save discounts to a personal bookmark list,
so that I can revisit them without re-searching.

The following page has these:
- Shows a dropdown to filter discounts by category.
- Displays a list of discounts.
- Lets the users bookmark them.
'''

import logging
import streamlit as st
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)
st.set_page_config(layout="wide")
SideBarLinks()

st.title("Save Your Favorite Discounts")

# Simulated discount data
discounts = [
    {"id": 101, "store": "Joe's Pizza", "category": "Food", "percent": 20},
    {"id": 102, "store": "TechMart", "category": "Electronics", "percent": 15},
    {"id": 103, "store": "FitLife Gym", "category": "Fitness", "percent": 10}
]

# Initialize bookmarks in session state
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

category = st.selectbox("Filter by Category", options=["All", "Food", "Electronics", "Fitness"])
filtered_discounts = [d for d in discounts if category == "All" or d["category"] == category]

st.subheader("Available Discounts")
for discount in filtered_discounts:
    with st.expander(f"{discount['store']} - {discount['percent']}% Off"):
        if discount["id"] in st.session_state.bookmarks:
            st.success("Already Bookmarked")
        else:
            if st.button(f"Bookmark - {discount['store']}", key=discount["id"]):
                st.session_state.bookmarks.append(discount["id"])
                st.success("Bookmarked!")