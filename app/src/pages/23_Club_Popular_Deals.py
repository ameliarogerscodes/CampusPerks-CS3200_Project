import streamlit as st
from modules.nav import SideBarLinks

# Simulated popular‑saves data
if "club_popular" not in st.session_state:
    st.session_state.club_popular = [
        {"id": 201, "store": "Cafe 123",    "item": "Coffee",    "percent": 15, "saves": 12},
        {"id": 205, "store": "Spirit Wear", "item": "T-Shirt",   "percent": 30, "saves":  9},
        {"id": 202, "store": "Uni Books",   "item": "Textbook",  "percent": 25, "saves":  7},
    ]

st.set_page_config(page_title="Popular Deals", layout="wide")
SideBarLinks(show_home=True)

st.title("🔥 Popular Deals Among Students")

# Sort by saves descending
pop = sorted(st.session_state.club_popular, key=lambda x: x["saves"], reverse=True)

st.markdown(f"### ⭐ Top {len(pop)} Saved Discounts")
for d in pop:
    with st.expander(f"{d['store']} — {d['percent']}% off {d['item']}"):
        st.write(f"Saved **{d['saves']}** times by students")

st.markdown("---")
st.caption("CampusPerks • Know what students love")
