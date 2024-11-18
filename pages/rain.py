import folium
import streamlit as st
from streamlit_extras.let_it_rain import rain

from streamlit_folium import st_folium

# center on Liberty Bell, add marker
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)


def example():
    rain(
        emoji="✨",
        font_size=50,
        falling_speed=2,
        animation_length="infinite",
    )

example()

def bobby():
    rain(
        emoji="❄️",
        font_size=54,
        falling_speed=10,
        animation_length="infinite",
    )

bobby()