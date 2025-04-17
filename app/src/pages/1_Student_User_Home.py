import logging
import streamlit as st
import requests
from modules.nav import SideBarLinks
from datetime import datetime, timedelta

# Setup
logger = logging.getLogger(__name__)
st.set_page_config(page_title="Student Dashboard", layout="wide")
SideBarLinks(show_home=True)

# Session fallback
username = st.session_state.get("username", "guest_user")
first_name = st.session_state.get("first_name", "Student")

st.title(f"Welcome, {first_name}! 🎓")
st.subheader("Maximize your savings with student-exclusive deals!")

# 🔧 Dashboard Action Buttons
st.markdown("### 🧭 Quick Actions")
col1, col2, col3 = st.columns(3)
with col1:
    st.page_link("pages/11_Student_Browse_Discounts.py", label="Browse Discounts", icon="🔍")
with col2:
    st.page_link("pages/12_Student_Bookmarked_Discounts.py", label="My Bookmarks", icon="📚")
with col3:
    st.page_link("pages/13_Student_Available_Discounts.py", label="Available", icon="⏳")

# 💡 Tip
st.info("Tip: Bookmark your favorite deals and check back before they expire!")

# 🗂️ Bookmark Snapshot
st.markdown("---")
st.markdown("### 📌 Recently Saved Discounts")

try:
    bm_response = requests.get(f"http://localhost:5000/api/savedDiscounts/{username}")
    bm_response.raise_for_status()
    saved = bm_response.json()
except Exception as e:
    st.warning("Could not load your saved discounts right now.")
    saved = []

if saved:
    for bd in saved[:5]:  # Show top 5
        st.markdown(f"- **{bd.get('storeName', 'Store')}** — {bd['percentOff']}% off *{bd.get('item', '')}* (`{bd.get('category', 'N/A')}`)")
else:
    st.caption("You haven't bookmarked any discounts yet.")

# ⌛ Expiring Soon Snapshot
st.markdown("---")
st.markdown("### ⏳ Expiring Soon (Next 7 Days)")

try:
    response = requests.get("http://localhost:5000/api/discounts")
    response.raise_for_status()
    discounts = response.json()
except:
    discounts = []

soon_threshold = datetime.today() + timedelta(days=7)

def parse_date_safe(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        return datetime.max

expiring = [
    d for d in discounts if "endDate" in d and parse_date_safe(d["endDate"]) < soon_threshold
]
expiring.sort(key=lambda d: parse_date_safe(d["endDate"]))

if expiring:
    for d in expiring[:5]:  # Show top 5
        st.markdown(f"- **{d.get('storeName', 'Store')}** — {d['percentOff']}% off *{d.get('item', '')}* until `{d['endDate']}`")
else:
    st.caption("No discounts expiring soon.")