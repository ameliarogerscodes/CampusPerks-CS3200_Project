import streamlit as st
from modules.nav import SideBarLinks

# Setup
st.set_page_config(page_title="Club Leader Dashboard", layout="wide")
SideBarLinks(show_home=True)

# Greeting
st.title(f"Welcome, Glen! 🎉")
st.subheader("Plan great events and save money for your club!")

# Dashboard Cards for Actions
st.markdown("### 🔧 Quick Actions")
col1, col2, col3 = st.columns(3)
with col1:
    st.button("🔍 Filter Discounts by Category")
with col2:
    st.button("📚 View Educational Discounts")
with col3:
    st.button("🔥 See Popular Deals")

# Tip for usage
st.info("Tip: Use bookmarks to save discounts while you browse and revisit them before events!")

# Planned Future Pages
st.markdown("---")
st.markdown("### 📅 Coming Soon for Club Leaders")
st.markdown("""
- Sort discounts by savings
- Filter by food, merch, or educational category
- See popular discounts used by students at Northeastern
- Save and review bookmarked discounts before making decisions
""")

# Footer
st.markdown("---")
st.caption("CampusPerks • Helping clubs plan smarter, cheaper, and faster.")
