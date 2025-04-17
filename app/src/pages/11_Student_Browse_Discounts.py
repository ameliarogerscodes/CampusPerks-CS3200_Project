import streamlit as st
from modules.nav import SideBarLinks

if "student_discounts" not in st.session_state:
    st.session_state.student_discounts = [
        {"id": 101, "store": "Cafe 123",     "item": "Coffee",   "percent": 15, "category": "Food"},
        {"id": 102, "store": "Book Nook",    "item": "Notebook", "percent": 20, "category": "Books"},
        {"id": 103, "store": "Tech Hub",     "item": "USB Drive","percent": 10, "category": "Tech"},
        {"id": 104, "store": "Style Corner", "item": "T-Shirt",  "percent": 25, "category": "Clothing"},
        {"id": 105, "store": "Fit Studio",   "item": "Yoga Mat", "percent": 30, "category": "Fitness"},
    ]

st.set_page_config(page_title="Browse Discounts", layout="wide")
SideBarLinks(show_home=True)

st.title("🔍 Browse Student Discounts")

all_cats = ["All"] + sorted({d["category"] for d in st.session_state.student_discounts})
choice = st.selectbox("Category", all_cats)

if choice == "All":
    filtered = st.session_state.student_discounts
else:
    filtered = [d for d in st.session_state.student_discounts if d["category"] == choice]

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
st.caption("CampusPerks • Helping students save smarter")
