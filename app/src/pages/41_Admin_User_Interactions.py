import streamlit as st
from modules.nav import SideBarLinks

# Page config first!
st.set_page_config(page_title="Admin: User Interactions", layout="wide")
SideBarLinks(show_home=True)

# 🔥 Simulated log data (replace later with API)
interaction_data = [
    {"user": "emmafoley", "action": "Used discount CODE123", "time": "2025-04-10 14:23"},
    {"user": "johnsmith", "action": "Joined club ArtSociety", "time": "2025-04-10 15:02"},
    {"user": "janedoe", "action": "Viewed store Starbucks", "time": "2025-04-10 15:45"},
    {"user": "markspencer", "action": "Checked out item Laptop", "time": "2025-04-10 16:00"},
    {"user": "janedoe", "action": "Used discount BOOKS15", "time": "2025-04-11 10:01"},
    {"user": "emmafoley", "action": "Bookmarked Espresso deal", "time": "2025-04-11 10:03"},
]

# 🏷️ Title & Filter
st.title("🧾 User Interaction Log")
st.caption("View recent platform activity from all users.")

search_query = st.text_input("🔍 Filter by username or action", "")

if search_query:
    filtered = [
        log for log in interaction_data
        if search_query.lower() in log["user"].lower() or search_query.lower() in log["action"].lower()
    ]
else:
    filtered = interaction_data

# 📋 Display Interactions
if filtered:
    for entry in filtered:
        with st.container():
            st.markdown(f"""
                <p style='font-size:14px;'>
                <strong>👤 User:</strong> {entry['user']}<br>
                <strong>📝 Action:</strong> {entry['action']}<br>
                <strong>⏰ Time:</strong> {entry['time']}
                </p>
                <hr style="border: 0.5px solid #666;">
            """, unsafe_allow_html=True)
else:
    st.info("No interactions match your search.")

# Footer
st.markdown("---")
st.caption("CampusPerks • Admin tools for better visibility and platform management.")