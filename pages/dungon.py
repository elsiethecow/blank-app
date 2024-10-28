import streamlit as st


rooms = [
    {
        "treasures": ["gold coin", "gem"],
        "monsters": ["goblin"],
        "secrets": ["map to next room"],
    },
    {
        "treasures": ["silver coin"],
        "monsters": ["troll"],
        "secrets": ["look behind the rock"],
    },
    {
        "treasures": ["diamond"],
        "monsters": ["dragon"],
        "secrets": ["use the key to open the door"],
    },
    {
        "treasures": ["ruby"],
        "monsters": ["giant spider"],
        "secrets": ["spiders are afraid of fire"],
    },
    {
        "treasures": ["emerald"],
        "monsters": ["unicorn", "giant eagle"],
        "secrets": ["unicorns are afraid of the dark"],
    },
    {
        "treasures": ["sapphire"],
        "monsters": ["giant squid"],
        "secrets": ["squids are afraid of the light", "the sapphire is actually glass"],
    },
    {
        "treasures": ["opal", "ruby"],
        "monsters": ["giant eagle"],
        "secrets": ["the eagle is actually a hologram"],
    },
]


st.write("On day I wanderd in to the casle dungons and this is what I found.")


room_num = 1
for room in rooms:
    treasures = ", ".join(room["treasures"])
    monsters = ", ".join(room["monsters"])
    secrets = ", ".join(room["secrets"])
    st.write(f"Romm number {room_num}. had a bunch of treasures: {treasures}. had a bunch of monsters: {monsters}. And had secrets: {secrets}.")
    room_num = room_num + 1