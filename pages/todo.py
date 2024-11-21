import streamlit as st

output = st.checkbox("wake up")
st.write(output)


title = st.text_input("what todo", "brush your teeth")   


if "my_stuff" not in st.session_state:
    st.session_state["my_stuff"] = []

if st.button("Add a thing"):
    st.session_state["my_stuff"].append(title)

st.write("SESSION STATE:")
st.write(str(st.session_state))

yoyo = st.checkbox(title)
st.write(yoyo)















































































