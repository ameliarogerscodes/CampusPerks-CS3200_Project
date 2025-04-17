import streamlit as st
import requests

st.set_page_config(page_title="My Bookmarked Discounts", layout="wide")
st.title("📚 My Saved Discounts")

# Grab username from session
username = st.session_state.get("username", "guest_user")

# Fetch saved discounts from the backend
api_url = f"http://localhost:5000/api/savedDiscounts/{username}"

try:
    response = requests.get(api_url)
    response.raise_for_status()
    saved_discounts = response.json()
except Exception as e:
    st.error("⚠️ Unable to load your saved discounts.")
    saved_discounts = []
    st.stop()

# Display saved discounts
if saved_discounts:
    st.markdown("### ⭐ Bookmarked Discounts")
    for disc in saved_discounts:
        with st.expander(f"{disc['storeName']} — {disc['percentOff']}% off {disc['item']}"):
            st.write(f"**Category:** {disc.get('category', 'N/A')}")
            st.write(f"**Valid until:** {disc.get('endDate', 'Unknown')}")
            st.write(f"**Code:** {disc.get('code', 'N/A')}")

            if st.button(f"🗑️ Remove Bookmark", key=f"remove_{disc['discountId']}"):
                delete_url = f"http://localhost:5000/api/savedDiscounts/{username}/{disc['discountId']}"
                del_response = requests.delete(delete_url)
                if del_response.status_code == 200:
                    st.success("Bookmark removed. Refresh the page to update.")
                else:
                    st.error("Could not remove bookmark. Try again.")
else:
    st.info("You haven't bookmarked any discounts yet.")
