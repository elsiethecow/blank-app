
import streamlit as st
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/1025/")

st.slider("find you favorit pokemon", 1, 1025, 1)
st.link_button(response.json()["sprites"]["front_default"])