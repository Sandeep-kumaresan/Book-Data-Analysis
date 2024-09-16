import streamlit as st
import matplotlib as plt
import seaborn as sns
import pandas as pd

st.title("Welcome to Book Data Analysis!")
df = pd.read_csv("Comics,Manga.csv")
st.text("Comics and Manga Prices")
st.bar_chart(data=df, x = "Price", y = "Title", x_label="Price", y_label="Book")
plt.figure(figsize=(12, 8))
sns.countplot(data=df, x='Price', palette='viridis')
plt.xticks(rotation=90)
plt.title('Frequency of Each Book Price')
plt.xlabel('Price')
plt.ylabel('Count')
st.pyplot(plt)


