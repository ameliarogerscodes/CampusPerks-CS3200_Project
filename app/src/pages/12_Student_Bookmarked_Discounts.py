# pages/12_Student_Bookmarked_Discounts.py
import streamlit as st
from modules.nav import SideBarLinks

if "discounts" not in st.session_state:
    st.error("Go to Browse first to load discounts.")
    st.stop()
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

st.set_page_config(page_title="My Bookmarked Discounts", layout="wide")
SideBarLinks(show_home=True)

st.title("📚 My Saved Discounts")

# --- Sidebar store filter ---
stores = sorted({d["store"] for d in st.session_state.discounts})
choice_store = st.sidebar.selectbox("Store", ["All"] + stores)

saved = [d for d in st.session_state.discounts if d["id"] in st.session_state.bookmarks]
if choice_store != "All":
    saved = [d for d in saved if d["store"] == choice_store]

st.markdown(f"### ⭐ {len(saved)} Bookmarked")
for d in saved:
    with st.expander(f"{d['store']} — {d['percent']}% off {d['item']}"):
        st.write(f"**Category:** {d['category']}")
        st.write(f"**Expires:** {d['endDate']}")
        key = f"rm_{d['id']}"
        if st.button("🗑️ Remove Bookmark", key=key):
            st.session_state.bookmarks.remove(d["id"])
            st.success("Removed — refresh to see updates")

st.markdown("---")
st.caption("CampusPerks • Your personal deals library.")
