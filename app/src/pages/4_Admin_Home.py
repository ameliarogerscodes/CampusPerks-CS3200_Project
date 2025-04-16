import logging
import streamlit as st
from modules.nav import SideBarLinks

# Setup
logger = logging.getLogger(__name__)
st.set_page_config(page_title="Admin Homepage", layout="wide")
SideBarLinks(show_home=True)

# Welcome header
st.title(f"Welcome back, {st.session_state.get('first_name', 'Student')}! 🎓")
st.subheader("Explore and bookmark discounts that match your needs.")

# Sample discount data
discounts = [
    {"id": 101, "store": "Joe's Pizza", "category": "Food", "percent": 20},
    {"id": 102, "store": "TechMart", "category": "Electronics", "percent": 15},
    {"id": 103, "store": "FitLife Gym", "category": "Fitness", "percent": 10}
]

# Initialize bookmarks in session_state
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

# Filter options
category = st.selectbox("🔍 Filter by Category", options=["All", "Food", "Electronics", "Fitness"])
filtered_discounts = [d for d in discounts if category == "All" or d["category"] == category]

# Display available discounts
st.markdown("### 📦 Available Discounts")
for discount in filtered_discounts:
    with st.expander(f"{discount['store']} — {discount['percent']}% Off ({discount['category']})"):
        if discount["id"] in st.session_state.bookmarks:
            st.success("✅ Already Bookmarked")
        else:
            if st.button(f"⭐ Bookmark this", key=discount["id"]):
                st.session_state.bookmarks.append(discount["id"])
                st.success("Bookmarked!")

# Display bookmarked discounts
st.markdown("---")
st.markdown("### 📚 My Bookmarked Discounts")

bookmarked_discounts = [d for d in discounts if d["id"] in st.session_state.bookmarks]
if bookmarked_discounts:
    for bd in bookmarked_discounts:
        st.markdown(f"- **{bd['store']}** ({bd['percent']}% off, *{bd['category']}*)")
else:
    st.info("You haven't bookmarked any discounts yet.")