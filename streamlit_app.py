import datetime
import streamlit as st

st.title("About you.")

wow = st.text_input("full name", "Name")
st.write("Hello", wow)

age = st.slider("How old are you?", 5, 20, 5)
st.write("your ", age, "years old")

genre = st.radio(
    "What's your computer experiencs",
    [":rainbow[A LOT]", "***avrige***", " very little"],
    index=None,
)

st.write("You selected:", genre)

color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)

st.write("your rating of computers")

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")
