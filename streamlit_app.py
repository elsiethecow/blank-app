import streamlit as st

st.title("Mininons!")
st.audio("minions.mp3",autoplay=True)
st.image("minionguitar.png")
st.image("minionsgun.jpg")

st.feedback(options="thumbs", *, key=None, disabled=False, on_change=None, args=None, kwargs=None)