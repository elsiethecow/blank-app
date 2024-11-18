import streamlit as st

output = st.checkbox("Brush your teeth")
st.write(output)

todos = {
    "Brush your teeth": False,
    "Comb your hair": False,
    "Wake up": True,
}

st.write(todos)

if st.button("Add a new item"):
    

if "my_stuff" not in st.session_state:
    st.session_state["my_stuff"] = []

if st.button("Add a thing"):
    st.session_state["my_stuff"].append("A thing!")

st.write("SESSION STATE:")
st.write(str(st.session_state))