# pages/11_Student_Browse_Discounts.py
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(page_title="Browse Discounts", layout="wide")
SideBarLinks(show_home=True)

# --- sample data ---
if "student_discounts" not in st.session_state:
    st.session_state.student_discounts = [
        {"discountId": 1, "storeName": "Cafe 123",    "item": "Coffee",    "percentOff": 15, "category": "Food",     "endDate": "2025-04-30"},
        {"discountId": 2, "storeName": "Uni Books",    "item": "Textbook",  "percentOff": 25, "category": "Books",    "endDate": "2025-05-05"},
        {"discountId": 3, "storeName": "Tech Store",   "item": "USB Drive", "percentOff": 20, "category": "Tech",     "endDate": "2025-04-25"},
        {"discountId": 4, "storeName": "Cloth Corner", "item": "Jeans",     "percentOff": 30, "category": "Clothing", "endDate": "2025-04-28"},
    ]

# --- bookmarks storage ---
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

# --- UI ---
st.title("🔍 Find the Best Student Discounts")

all_ds = st.session_state.student_discounts
cats = ["All"] + sorted({d["category"] for d in all_ds})
choice = st.selectbox("Filter by Category", cats)

filtered = all_ds if choice == "All" else [d for d in all_ds if d["category"] == choice]

st.markdown(f"### 🎯 {len(filtered)} Discounts Found")

for d in filtered:
    did = d["discountId"]
    with st.expander(f"{d['storeName']} — {d['percentOff']}% off {d['item']} ({d['category']})"):
        st.write(f"**Valid until:** {d['endDate']}")
        if did in st.session_state.bookmarks:
            st.success("✅ Bookmarked")
        else:
            if st.button("⭐ Bookmark this", key=f"b_{did}"):
                st.session_state.bookmarks.append(did)
                st.success("Saved!")

st.markdown("---")
st.caption("CampusPerks • Helping students save smarter.")
