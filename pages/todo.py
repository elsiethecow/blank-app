import streamlit as st

if st.button("Add a to do"):
    title = st.text_input("what todo", "brush your teeth")   

yoyo = st.checkbox(title)
st.write(yoyo)

#if "my_stuff" not in st.session_state:
    #st.session_state["my_stuff"] = []



st.write("SESSION STATE:")
st.write(str(st.session_state))