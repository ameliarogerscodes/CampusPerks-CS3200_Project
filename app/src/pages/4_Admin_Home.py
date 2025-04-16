import logging
import streamlit as st
from modules.nav import SideBarLinks
'''
# Setup
logger = logging.getLogger(__name__)
st.set_page_config(page_title="Admin Homepage", layout="wide")
SideBarLinks(show_home=True)
'''
# Set page configuration
st.set_page_config(page_title="Admin Homepage")

# Sample user data for profiles (example data)
users_data = [
    {"username": "emmafoley", "first_name": "Emma", "last_name": "Foley", "email": "emma@example.com", "phone": "123-456-7890", "birthdate": "2000-05-12"},
    {"username": "johnsmith", "first_name": "John", "last_name": "Smith", "email": "john@example.com", "phone": "987-654-3210", "birthdate": "1999-08-22"},
    {"username": "janedoe", "first_name": "Jane", "last_name": "Doe", "email": "jane@example.com", "phone": "555-123-4567", "birthdate": "1998-11-30"},
    {"username": "markspencer", "first_name": "Mark", "last_name": "Spencer", "email": "mark@example.com", "phone": "321-654-9870", "birthdate": "2001-02-15"},
]

# Sample interaction data
interaction_data = [
    {"user": "emmafoley", "action": "Used discount CODE123", "time": "2025-04-10 14:23"},
    {"user": "johnsmith", "action": "Joined club ArtSociety", "time": "2025-04-10 15:02"},
    {"user": "janedoe", "action": "Viewed store Starbucks", "time": "2025-04-10 15:45"},
    {"user": "markspencer", "action": "Checked out item Laptop", "time": "2025-04-10 16:00"},
]

# Tabs for navigation
tab = st.selectbox("Select Page", ["User Interactions", "Search Users"])

# User Interactions Tab
if tab == "User Interactions":
    st.markdown("<h1 style='text-align: center;'>Admin Homepage</h1>", unsafe_allow_html=True)

    # Search input from the user
    search_query = st.text_input("Search User Interactions", "")

    # Filter the interactions based on the search query (case-insensitive)
    if search_query:
        filtered_interactions = [
            entry for entry in interaction_data
            if search_query.lower() in entry['user'].lower() or search_query.lower() in entry['action'].lower()
        ]
    else:
        filtered_interactions = interaction_data  # Show all if no search query

    # Display user interactions
    st.subheader("User Interaction Log")

    # Loop through filtered interactions and display them with smaller text
    if filtered_interactions:
        for entry in filtered_interactions:
            st.markdown(f"""
            <p style='font-size: 12px;'>
            <strong>User:</strong> {entry['user']}<br>
            <strong>Action:</strong> {entry['action']}<br>
            <strong>Time:</strong> {entry['time']}
            </p>
            <hr style="border: 1px solid #e1e1e1;">
            """, unsafe_allow_html=True)
    else:
        st.markdown("<p style='font-size: 12px;'>No interactions found matching your search.</p>", unsafe_allow_html=True)

# Search Users Tab
elif tab == "Search Users":
    st.markdown("<h1 style='text-align: center;'>Search for Users</h1>", unsafe_allow_html=True)

    # User search input
    username_search = st.text_input("Search by Username", "")

    # Filter users based on search query (case-insensitive)
    if username_search:
        filtered_users = [
            user for user in users_data if username_search.lower() in user['username'].lower()
        ]
    else:
        filtered_users = users_data  # Show all if no search query

    # Display user profiles
    if filtered_users:
        for user in filtered_users:
            st.subheader(f"Profile of {user['first_name']} {user['last_name']}")
            st.write(f"**Username:** {user['username']}")
            st.write(f"**Email:** {user['email']}")
            st.write(f"**Phone:** {user['phone']}")
            st.write(f"**Birthdate:** {user['birthdate']}")

            # Editing fields (inputs to update user profile)
            st.markdown("### Edit User Information")
            new_first_name = st.text_input("First Name", user['first_name'])
            new_last_name = st.text_input("Last Name", user['last_name'])
            new_email = st.text_input("Email", user['email'])
            new_phone = st.text_input("Phone", user['phone'])
            new_birthdate = st.text_input("Birthdate", user['birthdate'])

            # Button to update user info
            if st.button(f"Update {user['username']} Profile"):
                # Update the user data (in-memory update for this example)
                user['first_name'] = new_first_name
                user['last_name'] = new_last_name
                user['email'] = new_email
                user['phone'] = new_phone
                user['birthdate'] = new_birthdate

                st.success(f"Profile of {user['username']} has been updated!")

            st.markdown("---")
    else:
        st.write("No users found matching your search.")
