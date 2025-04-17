import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks

# Setup
logger = logging.getLogger(__name__)
st.set_page_config(page_title="Student Dashboard", layout="wide")
SideBarLinks(show_home=True)

# Session fallback for first name
username = st.session_state.get("username", "guest_user")
first_name = st.session_state.get("first_name", "Student")

st.title(f"Welcome back, {first_name}! 🎓")
st.subheader("Explore and bookmark discounts that match your needs.")

# --- Category Filter UI ---
category = st.selectbox("🔍 Filter by Category", options=["All", "Food", "Electronics", "Fitness", "Books", "Clothing"])

# --- Fetch discounts from backend ---
params = {}
if category != "All":
    params["category"] = category
params["location"] = "Boston"  # Optional: make dynamic

try:
    response = requests.get("http://localhost:4000/discount", params=params)
    response.raise_for_status()
    discount = response.json()
except Exception as e:
    st.error("⚠️ Could not load discounts from the server.")
    logger.error(f"Failed to fetch discounts: {e}")
    discount = []

# Initialize bookmarks in session_state
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

# --- Show Discount Results ---
st.markdown("### 📦 Available Discounts")
if discount:
    for discount in discount:
        disc_id = discount["discountId"]
        store = discount.get("storeName", f"Store {discount['storeId']}")
        percent = discount["percentOff"]
        item = discount.get("item", "")
        category_name = discount.get("category", "N/A")

        with st.expander(f"{store} — {percent}% Off {item} ({category_name})"):
            if disc_id in st.session_state.bookmarks:
                st.success("✅ Already Bookmarked")
            else:
                if st.button(f"⭐ Bookmark this", key=f"bookmark_{disc_id}"):
                    st.session_state.bookmarks.append(disc_id)
                    st.success("Bookmarked!")

else:
    st.info("No discounts found for this category.")

# --- Show Bookmarks Section ---
st.markdown("---")
st.markdown("### 📚 My Bookmarked Discounts")
bookmarked_discount = [d for d in discount if d["discountId"] in st.session_state.bookmarks]

if bookmarked_discount:
    for bd in bookmarked_discount:
        st.markdown(f"- **{bd.get('storeName', 'Store')}** ({bd['percentOff']}% off, *{bd.get('category', 'N/A')}*)")
else:
    st.info("You haven't bookmarked any discounts yet.")
