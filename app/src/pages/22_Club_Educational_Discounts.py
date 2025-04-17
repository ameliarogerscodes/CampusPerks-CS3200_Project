import streamlit as st
from modules.nav import SideBarLinks

# Ensure the same data is in session_state
if "club_discounts" not in st.session_state:
    st.session_state.club_discounts = [
        {"id": 201, "store": "Cafe 123",     "item": "Coffee",    "percent": 15, "category": "Food"},
        {"id": 202, "store": "Uni Books",     "item": "Textbook",  "percent": 25, "category": "Books"},
        {"id": 203, "store": "Club Shop",    "item": "Trophy",    "percent": 10, "category": "Merch"},
        {"id": 204, "store": "Tech Store",   "item": "USB Drive", "percent": 20, "category": "Tech"},
        {"id": 205, "store": "Spirit Wear",  "item": "T-Shirt",   "percent": 30, "category": "Merch"},
    ]

st.set_page_config(page_title="Educational Discounts", layout="wide")
SideBarLinks(show_home=True)

st.title("📚 Educational Discounts")

# Filter for category "Books" only
edu_discounts = [d for d in st.session_state.club_discounts if d["category"] == "Books"]

st.markdown(f"### 🎯 {len(edu_discounts)} Educational Discounts Found")
if edu_discounts:
    for d in edu_discounts:
        with st.expander(f"{d['store']} — {d['percent']}% off {d['item']}"):
            st.write(f"**Store:** {d['store']}")
            st.write(f"**Item:** {d['item']}")
            st.write(f"**Discount:** {d['percent']}%")
else:
    st.info("No educational discounts available.")

st.markdown("---")
st.caption("CampusPerks • Fueling your club’s learning")
