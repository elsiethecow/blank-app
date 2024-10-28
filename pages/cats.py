import pyjokes
import streamlit as st
import requests


# st.write(# pyjokes.get_joke()

response = requests.get("https://pokeapi.co/api/v2/pokemon/124/")

st.image(response.json()["sprites"]["front_default"])