import streamlit as st
from modules.nav import SideBarLinks

# Sample expiring‐soon discounts (days_left ≤ 7)
if "student_discounts" not in st.session_state:
    st.session_state.student_discounts = [
        {"id": 101, "store": "Cafe 123",   "item": "Coffee",    "percent": 15, "days_left": 3},
        {"id": 102, "store": "Book Nook",  "item": "Notebook",  "percent": 20, "days_left": 10},
        {"id": 103, "store": "Tech Hub",   "item": "USB Drive", "percent": 10, "days_left": 5},
        {"id": 104, "store": "Style Corner","item": "T-Shirt",   "percent": 25, "days_left": 2},
        {"id": 105, "store": "Fit Studio", "item": "Yoga Mat",  "percent": 30, "days_left": 8},
    ]

st.set_page_config(page_title="Expiring Soon", layout="wide")
SideBarLinks(show_home=True)

st.title("⏳ Discounts Expiring Soon")

# Filter to those expiring in 7 days or less
soon = sorted(
    [d for d in st.session_state.student_discounts if "days_left" in d and d["days_left"] <= 7],
    key=lambda x: x["days_left"]
)



st.markdown(f"### 🔔 {len(soon)} Discount(s) Expiring Soon")
if soon:
    for d in soon:
        with st.expander(f"{d['store']} — {d['percent']}% off {d['item']} (in {d['days_left']} days)"):
            st.write(f"**Store:** {d['store']}")
            st.write(f"**Item:** {d['item']}")
            st.write(f"**Discount:** {d['percent']}%")
            st.write(f"**Expires in:** {d['days_left']} day(s)")
else:
    st.info("Nothing is expiring within the next week.")

st.markdown("---")
st.caption("CampusPerks • Stay ahead and save before it's too late")
