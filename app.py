import streamlit as st
import core_agents  # Our agents from Lesson 4

# Top Bar
st.markdown("""
<div style='background-color: #2E2E2E; padding: 10px; display: flex; justify-content: space-between; align-items: center;'>
    <div style='display: flex; align-items: center;'>
        <span style='font-size: 24px; color: #FFFFFF;'>🍕 AI Delivery Sales Suite</span>
    </div>
    <div>
        <span style='color: #FFFFFF; margin-right: 20px;'>Home</span>
        <span style='color: #FFFFFF; margin-right: 20px;'>About</span>
        <span style='color: #FFFFFF;'>Contact</span>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)  # Add some space below the top bar

# Language picker
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Arabic": "ar",
    "Chinese": "zh",
    "Hindi": "hi",
    "Portuguese": "pt",
    "Russian": "ru",
    "Japanese": "ja"
}
lang = st.selectbox("Pick your language!", list(languages.keys()))

# Title
st.title("Boost Your Sales 🚀")

# Inputs
st.header("Tell us about your restaurant!")
restaurant_type = st.text_input("What kind of food do you sell? (e.g., Pizza)", "Pizza")
menu = st.text_area("Your menu (e.g., Burger $10, Fries $3)", "Burger $10\nFries $3\nSoda $2")
slow_days = st.text_input("Slow days? (e.g., Tuesday, Wednesday)", "Tuesday, Wednesday")
hours = st.text_input("Your hours? (e.g., 11 AM-10 PM)", "11 AM-10 PM")
goals = st.text_input("Your goal? (e.g., More sales)", "More sales")
zip_code = st.text_input("ZIP code? (e.g., 10001)", "10001")
opening_date = st.text_input("Opening date? (e.g., March 15, 2025)", "March 15, 2025")
platform = st.selectbox("Which platform?", ["Uber Eats", "DoorDash", "Zomato", "Deliveroo"])

# Convert menu to a list
menu_items = menu.split("\n")

# Run button
if st.button("Get Sales Ideas!"):
    st.header("Your Sales Boosters!")

    # Promo Agent
    st.subheader("Promo Ideas")
    promo_deals = core_agents.promo_agent()
    for deal in promo_deals:
        st.write(f"- {deal}")

    # Lurer Agent
    st.subheader("Quick Messages")
    lurer_msgs = core_agents.lurer_agent()
    for msg in lurer_msgs:
        st.write(f"- {msg}")

    # Menu Agent
    st.subheader("Top Menu Items")
    menu_picks = core_agents.menu_agent(menu_items)
    for item, desc in menu_picks:
        st.write(f"- {item}: {desc}")

    # Surge Agent
    st.subheader("Busy Time Deal")
    surge_deal = core_agents.surge_agent()
    st.write(f"- {surge_deal}")

    # Bumper Agent
    st.subheader("Add-On Suggestions")
    bumper_addons = core_agents.bumper_agent(menu_items)
    for addon in bumper_addons:
        st.write(f"- {addon}")

    # Placeholder for Lesson 5 agents (not coded yet)
    st.subheader("Coming Soon...")
    st.write("Boost Agent: Welcome deal for new restaurants!")
    st.write("Trend Agent: What’s trending on TikTok/X!")
    st.write("Area Agent: Local deal for your area!")
    st.write("Competitor Agent: Beat your rivals!")
    st.write("Remote Agent: We’ll set it up for you!")
    st.write("Smart Bundle Agent: Combo deals to boost orders!")    