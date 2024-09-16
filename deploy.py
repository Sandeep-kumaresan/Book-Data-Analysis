import streamlit as st
import matplotlib as plt
import seaborn as sns
import pandas as pd

st.title("Welcome to Book Data Analysis!")
df = pd.read_csv("Comics,Manga.csv")
st.bar_chart(data=df, x = "Price", y = "Title")


