# pages/13_Student_Available_Discounts.py
import streamlit as st
from modules.nav import SideBarLinks
from datetime import datetime, timedelta

st.set_page_config(page_title="Discounts Expiring Soon", layout="wide")
SideBarLinks(show_home=True)

# --- ensure sample discounts exist ---
if "student_discounts" not in st.session_state:
    st.error("No discount data loaded. Go to Browse first.")
    st.stop()

# --- bookmarks ---
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

# --- compute expiring soon ---
threshold = datetime.today() + timedelta(days=7)
def to_dt(s): 
    return datetime.fromisoformat(s) if s else datetime.max

expiring = [d for d in st.session_state.student_discounts
            if to_dt(d["endDate"]) <= threshold]

expiring.sort(key=lambda d: to_dt(d["endDate"]))

st.title("⏳ Discounts Expiring Soon")

<<<<<<< HEAD
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
=======
if not expiring:
    st.info("No discounts expiring in the next 7 days.")
>>>>>>> 62c5761399138a821e1a296cb36c8c0c3d5a915d
else:
    st.markdown(f"### 🔔 {len(expiring)} Expiring Soon")
    for d in expiring:
        did = d["discountId"]
        with st.expander(f"{d['storeName']} — {d['percentOff']}% off {d['item']} (until {d['endDate']})"):
            if did in st.session_state.bookmarks:
                st.success("✅ Already Bookmarked")
            else:
                if st.button("⭐ Bookmark", key=f"s_{did}"):
                    st.session_state.bookmarks.append(did)
                    st.success("Saved!")

st.markdown("---")
st.caption("CampusPerks • Stay ahead and save before it's too late.")
