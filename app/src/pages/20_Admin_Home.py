import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('System Admin Home Page')

if st.button('Update ML Models', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_ML_Model_Mgmt.py')


# add window to display user interactions
if "interaction_log" not in st.session_state:
    st.session_state.interaction_log = []

if admin_input:
    st.session_state.interaction_log.append(admin_input)

st.subheader("User Interactions")
interaction_window = "\n".join(st.session_state.interaction_log)
st.text_area("Interaction Window", interaction_window, height=200)

# user examples:
users = [
    {"username": "emmafoley", "name": "Emma Foley", "email": "ef@northeastern.edu"},
    {"username": "johnsmith", "name": "John Smith", "email": "js@example.com"},
    {"username": "alexdoe", "name": "Alex Doe", "email": "alex@example.com"},
]

# search bar to search for users in the app
search_query = st.text_input("Search Users by username, name, or email")

if search_query:
    filtered_users = [
        user for user in users
        if search_query.lower() in user["username"].lower()
        or search_query.lower() in user["name"].lower()
        or search_query.lower() in user["email"].lower()
    ]
else:
    filtered_users = users

st.subheader("Search Results")
if filtered_users:
    for user in filtered_users:
        st.markdown(f"**Username:** {user['username']}")
        st.markdown(f"**Name:** {user['name']}")
        st.markdown(f"**Email:** {user['email']}")
        st.markdown("---")
else:
    st.write("No users found.")