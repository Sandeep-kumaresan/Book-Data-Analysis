import streamlit as st
import matplotlib as plt
import seaborn as sns
import pandas as pd

st.title("Welcome to Book Data Analysis!")
df = pd.read_csv("Comics,Manga.csv")
st.text("Comics and Manga Prices")
st.bar_chart(data=df, x = "Price", y = "Title", x_label="Price", y_label="Book")
st.plotly_chart(data=df, x = "Price", y = "Title", x_label="Price", y_label="Book")


