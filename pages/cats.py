
import streamlit as st
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/16/")

st.slider("find you favorit pokemon", 1, 1025, 1)
st.image(response.json()["sprites"]["front_default"])