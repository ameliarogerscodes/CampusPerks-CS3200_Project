import streamlit as st
import requests

st.set_page_config(page_title="Browse Discounts", layout="wide")
st.title("🔍 Find the Best Student Discounts")

# --- Sidebar Filters ---
st.sidebar.header("🎛️ Filter Discounts")
category = st.sidebar.selectbox("Category", ["All", "Food", "Clothing", "Books", "Tech"])
location = st.sidebar.text_input("City (e.g., Boston)", value="Boston")
sort_option = st.sidebar.radio("Sort by", ["Highest % Off", "Newest First"])

# --- API Call Setup ---
params = {}
if category != "All":
    params["category"] = category
if location:
    params["location"] = location

api_url = "http://localhost:5000/api/discounts"
response = requests.get(api_url, params=params)

if response.status_code == 200:
    discounts = response.json()

    if sort_option == "Highest % Off":
        discounts = sorted(discounts, key=lambda d: d["percentOff"], reverse=True)
    elif sort_option == "Newest First":
        discounts = sorted(discounts, key=lambda d: d.get("startDate", ""), reverse=True)

    # --- Display Results ---
    st.subheader(f"🎯 {len(discounts)} Matching Discounts")
    for disc in discounts:
        st.markdown(f"""
        #### 🏪 {disc['storeName']}
        - **Item:** {disc['item']}
        - **Discount:** {disc['percentOff']}%
        - **Valid until:** {disc['endDate']}
        """)
else:
    st.error("Failed to load discounts. Please try again later.")

# Footer
st.markdown("---")
st.caption("CampusPerks • Helping students save smarter.")