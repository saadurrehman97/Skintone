import sys
import streamlit as st

st.title("Python version")
version_info=sys.version_info
st.write(f"python version:{version_info}")
st.write("I'm here")