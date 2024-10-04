import streamlit as st

st.write("=", num2*num1)


num1 = st.number_input("Number1  ", value=4)


num2 = st.number_input("Number2 ", value=5)

if st.button("Devide"):
    st.write("num1 % num2=", num2%num1)


if st.button("Times"):
    st.write("num1 * num2=", num2*num1)


if st.button("minuse"):
    st.write("num1 - num2=", num2-num1)

if st.button("plus")
    st.write("num1 + num2=", num2+num1)

