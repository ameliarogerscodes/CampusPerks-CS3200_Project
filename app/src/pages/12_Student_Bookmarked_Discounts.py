# pages/12_Student_Bookmarked_Discounts.py
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(page_title="My Bookmarked Discounts", layout="wide")
SideBarLinks(show_home=True)

# --- ensure sample discounts exist ---
if "student_discounts" not in st.session_state:
    st.error("No discount data loaded. Go to Browse first.")
    st.stop()

if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

# --- UI ---
st.title("📚 My Saved Discounts")

if not st.session_state.bookmarks:
    st.info("You haven't bookmarked any discounts yet.")
else:
    saved = [d for d in st.session_state.student_discounts
             if d["discountId"] in st.session_state.bookmarks]
    st.markdown(f"### ⭐ {len(saved)} Bookmarked")
    for d in saved:
        did = d["discountId"]
        with st.expander(f"{d['storeName']} — {d['percentOff']}% off {d['item']} ({d['category']})"):
            st.write(f"**Valid until:** {d['endDate']}")
            if st.button("🗑️ Remove Bookmark", key=f"r_{did}"):
                st.session_state.bookmarks.remove(did)
                st.success("Removed. Refresh to update.")

st.markdown("---")
st.caption("CampusPerks • Your personal savings hub.")
