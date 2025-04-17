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

if not expiring:
    st.info("No discounts expiring in the next 7 days.")
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
