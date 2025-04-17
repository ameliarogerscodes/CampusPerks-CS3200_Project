# pages/11_Student_Browse_Discounts.py
import streamlit as st
from modules.nav import SideBarLinks

if "discounts" not in st.session_state:
    st.session_state.discounts = [
        {"id": 1, "store": "Farmers Horse Coffee", "item": "Latte",     "percent": 10, "category": "Food",  "endDate": "2025-05-01"},
        {"id": 2, "store": "BU Bookstore",         "item": "Textbook", "percent": 5,  "category": "Books", "endDate": "2025-06-01"},
        {"id": 3, "store": "Campus Cafe",         "item": "Sandwich","percent": 15, "category": "Food",  "endDate": "2025-04-25"},
        {"id": 4, "store": "Tech Shop",           "item": "USB Drive","percent": 20, "category": "Tech",  "endDate": "2025-05-10"},
        {"id": 5, "store": "Spirit Wear",         "item": "T-Shirt",  "percent": 30, "category": "Merch", "endDate": "2025-04-22"},
    ]
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

st.set_page_config(page_title="Browse Discounts", layout="wide")
SideBarLinks(show_home=True)

st.title("🔍 Browse Discounts")

# --- Sidebar controls ---
stores = sorted({d["store"] for d in st.session_state.discounts})
cats   = ["All"] + sorted({d["category"] for d in st.session_state.discounts})

choice_store    = st.sidebar.selectbox("Store", ["All"] + stores)
choice_category = st.sidebar.selectbox("Category", cats)

filtered = st.session_state.discounts
if choice_store != "All":
    filtered = [d for d in filtered if d["store"] == choice_store]
if choice_category != "All":
    filtered = [d for d in filtered if d["category"] == choice_category]

st.markdown(f"### 🎯 {len(filtered)} Discounts Found")
for d in filtered:
    with st.expander(f"{d['store']} — {d['percent']}% off {d['item']}"):
        st.write(f"**Category:** {d['category']}")
        st.write(f"**Expires:** {d['endDate']}")
        key = f"bm_{d['id']}"
        if d["id"] in st.session_state.bookmarks:
            st.success("✅ Bookmarked")
        else:
            if st.button("⭐ Bookmark this", key=key):
                st.session_state.bookmarks.append(d["id"])
                st.success("Bookmarked!")

st.markdown("---")
st.caption("CampusPerks • Helping students save smarter.")
