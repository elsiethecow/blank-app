import streamlit as st

if st.button("Say hello"):
    st.write("Why hello there")

num1 = st.number_input("this number", value=4)


num2 = st.number_input("and this number", value=5)

st.write(" =", num2+num1)

num1 = st.number_input("this number ", value=4)


num2 = st.number_input("times this number", value=5)

st.write("=", num2*num1)


num1 = st.number_input("this number  ", value=4)


num2 = st.number_input("mines this number ", value=5)

st.write(" =", num1-num2)


if st.button("finished"):   
    st.write("Goodbye!")










