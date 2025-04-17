# pages/13_Student_Available_Discounts.py
import streamlit as st
from modules.nav import SideBarLinks
from datetime import datetime, timedelta

if "discounts" not in st.session_state:
    st.error("Go to Browse first to load discounts.")
    st.stop()

st.set_page_config(page_title="Expiring Soon", layout="wide")
SideBarLinks(show_home=True)

st.title("⏳ Discounts Expiring Soon")

# parse helper
def parse_date(s):
    try: return datetime.strptime(s, "%Y-%m-%d")
    except: return datetime.max

threshold = datetime.today() + timedelta(days=7)
soon = [d for d in st.session_state.discounts if parse_date(d["endDate"]) < threshold]

# sidebar store filter
stores = sorted({d["store"] for d in soon})
choice_store = st.sidebar.selectbox("Store", ["All"] + stores)

if choice_store != "All":
    soon = [d for d in soon if d["store"] == choice_store]

st.markdown(f"### 🔔 {len(soon)} Expiring Within 7 Days")
for d in sorted(soon, key=lambda x: parse_date(x["endDate"])):
    st.markdown(f"**{d['store']}** — {d['percent']}% off {d['item']} (expires {d['endDate']})")

st.markdown("---")
st.caption("CampusPerks • Grab them before they’re gone.")
