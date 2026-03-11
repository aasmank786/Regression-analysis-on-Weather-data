import streamlit as st
import pandas as pd

st.title("Weather Regression Analysis")

st.write("Upload your weather dataset")

file = st.file_uploader("Upload CSV", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    st.write("Dataset Preview")
    st.dataframe(df.head())
