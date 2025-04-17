import streamlit as st
import requests
from datetime import datetime, timedelta

st.set_page_config(page_title="Discounts Ending Soon", layout="wide")
st.title("⏳ Discounts Expiring Soon")

# Fetch all available discounts
try:
    response = requests.get("http://localhost:5000/api/discounts")
    response.raise_for_status()
    discounts = response.json()
except Exception as e:
    st.error("⚠️ Could not load discounts from the server.")
    discounts = []
    st.stop()

# Filter and sort by expiration date
soon_threshold = datetime.today() + timedelta(days=7)

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except:
        return datetime.max  # If no date or error

discounts_with_dates = [
    d for d in discounts if "endDate" in d and parse_date(d["endDate"]) < soon_threshold
]
discounts_with_dates.sort(key=lambda d: parse_date(d["endDate"]))

# Display results
if discounts_with_dates:
    st.markdown(f"### 🔔 {len(discounts_with_dates)} Discount(s) Expiring Soon")
    for d in discounts_with_dates:
        store = d.get("storeName", "Unknown Store")
        item = d.get("item", "Item")
        percent = d.get("percentOff", "N/A")
        end_date = d.get("endDate", "Unknown")

        st.markdown(f"""
        #### 🏪 {store}
        - **Item:** {item}
        - **Discount:** {percent}% off
        - **Expires on:** `{end_date}`
        """)
else:
    st.info("No discounts are expiring soon. Check back later!")

# Footer
st.markdown("---")
st.caption("CampusPerks • Stay ahead and save before it's too late.")
