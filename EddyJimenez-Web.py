import streamlit as st


import google.generativeai as genai
import os

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2, col3 = st.columns(3)

# Clearly, this format takes just an eensy weensy bit of inspiration from Hassan's streamlit website.

# Note to self: try to figure out how to get a line graph.

with col1:
    st.subheader("Hello,")
    st.title("Welcome to Eddy Jimenez")
    st.title("")
    st.title("")
    st.title("")
    st.write("Eddy aspires to have a career either in programming or engineering.")
    st.title("")
    st.title("")
    st.write("")
    st.text("")
    st.subheader("Other website:")
    st.image("images/BoblandUrl.png")
    # The AI will go at the bottom of the page as a sort of conclusion thingy
    st.image("images/BoblandWebsite.png")
    st.title("")
    st.title("")
    st.subheader("Youtube Channel")
    st.write("- One of the smallest miscallaneous content channel on Youtube")
    st.write("- Less than 400k+ Subscribers")
    st.write("- Zero tutorials")
    st.write("- Less than 15 Million+ Views")
    st.write("- Less than 1.5 Million Hours+ Watch time")


with col2:
    st.image("images/HeyLookItsAPictureOfEddy.png")
    # The AI will go at the bottom of the page as a sort of conclusion thingy
    st.title("")
    st.title("")
    st.text("")
    st.write("----------")
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.text("")
    st.text("")
    st.write("----------")
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.write("")
    st.write("----------")
    st.title("")
    st.title("")
    st.title("")
    st.title("--Skills--")
    st.slider("Programming", 0, 100, 10)
    st.slider("Sleeping", 0, 100, 96)
    st.slider("Breathing", 0, 100, 100)
    st.slider("Being not dead", 0, 100, 100)
    st.title("")
    st.title("")
    st.title("")
    st.title("Any other questions?")
    st.write("---------------ASK THE AI.---------------")
    st.subheader("------EDDY'S AI------Input question here:")
    user_question = st.text_input("")
    if st.button("Click to receive response", use_container_width=400):
        prompt = user_question
        response = model.generate_content("You are a Response Ai created by Eddy Jimenez. Your job is to respond to any questions regarding Eddy Jimenez. Eddy is a 15 year old boy who lives in New Jersey and aspires to gain a job in programming or mechanical engineering. Eddy enjoys taking peaceful walks outside, reading, listening to music, and playing strategy video games. ")
        st.write(response.text)


with col3:
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.title("")
    st.image("images/pythonlogo.png")
    st.subheader("")
    st.image("images/engineering.png")
    st.title("")
    st.write("")
    st.write("")
    st.write("It may already be clear from the photo but Bobland is absolutely intended to be a joke website. You can still explore the AI's unique personality there.")
    st.title("")
    st.title("")
    st.title("")
    st.text("")
    st.image("images/YTChannel.png")

st.title("Any inquiries? Contact me at eddyjimenezv1223@gmail.com")
