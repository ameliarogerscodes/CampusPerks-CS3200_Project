import streamlit as st
from modules.nav import SideBarLinks

# Ensure we have discounts and bookmarks in session
if "student_discounts" not in st.session_state:
    st.session_state.student_discounts = [
        {"id": 101, "store": "Cafe 123",     "item": "Coffee",   "percent": 15, "category": "Food"},
        {"id": 102, "store": "Book Nook",    "item": "Notebook", "percent": 20, "category": "Books"},
        {"id": 103, "store": "Tech Hub",     "item": "USB Drive","percent": 10, "category": "Tech"},
        {"id": 104, "store": "Style Corner", "item": "T-Shirt",  "percent": 25, "category": "Clothing"},
        {"id": 105, "store": "Fit Studio",   "item": "Yoga Mat", "percent": 30, "category": "Fitness"},
    ]
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

st.set_page_config(page_title="My Bookmarks", layout="wide")
SideBarLinks(show_home=True)

st.title("📚 My Bookmarked Discounts")

# Build list of bookmarked discount records
booked = [d for d in st.session_state.student_discounts if d["id"] in st.session_state.bookmarks]

st.markdown(f"### ⭐ {len(booked)} Saved Discounts")
if booked:
    for d in booked:
        with st.expander(f"{d['store']} — {d['percent']}% off {d['item']} ({d['category']})"):
            st.write(f"**Store:** {d['store']}")
            st.write(f"**Item:** {d['item']}")
            st.write(f"**Discount:** {d['percent']}%")
            if st.button("🗑️ Remove Bookmark", key=f"rm_{d['id']}"):
                st.session_state.bookmarks.remove(d["id"])
                st.success("Removed! (refresh page)")
else:
    st.info("You haven't bookmarked any discounts yet.")

st.markdown("---")
st.caption("CampusPerks • Your personal savings list")
