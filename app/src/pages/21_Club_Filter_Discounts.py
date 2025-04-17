import streamlit as st
from modules.nav import SideBarLinks

if "club_discounts" not in st.session_state:
    st.session_state.club_discounts = [
        {"id": 201, "store": "Cafe 123",     "item": "Coffee",    "percent": 15, "category": "Food"},
        {"id": 202, "store": "Uni Books",     "item": "Textbook",  "percent": 25, "category": "Books"},
        {"id": 203, "store": "Club Shop",    "item": "Trophy",    "percent": 10, "category": "Merch"},
        {"id": 204, "store": "Tech Store",   "item": "USB Drive", "percent": 20, "category": "Tech"},
        {"id": 205, "store": "Spirit Wear",  "item": "T-Shirt",   "percent": 30, "category": "Merch"},
    ]

st.set_page_config(page_title="Filter Discounts", layout="wide")
SideBarLinks(show_home=True)

st.title("🔍 Filter Discounts by Category")

all_cats = ["All"] + sorted({d["category"] for d in st.session_state.club_discounts})
choice = st.selectbox("Category", all_cats)

if choice == "All":
    filtered = st.session_state.club_discounts
else:
    filtered = [d for d in st.session_state.club_discounts if d["category"] == choice]

st.markdown(f"### 🎯 {len(filtered)} Discounts Found")
if filtered:
    for d in filtered:
        with st.expander(f"{d['store']} — {d['percent']}% off {d['item']} ({d['category']})"):
            st.write(f"**Store:** {d['store']}")
            st.write(f"**Item:** {d['item']}")
            st.write(f"**Discount:** {d['percent']}%")
else:
    st.info("No discounts match this category.")

st.markdown("---")
st.caption("CampusPerks • Helping clubs save on event essentials")
