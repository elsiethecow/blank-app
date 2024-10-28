import pyjokes
import streamlit as st
import requests


# st.write(# pyjokes.get_joke()

response = requests.get("")

st.image(response.json()["sprites"]["front_default"])