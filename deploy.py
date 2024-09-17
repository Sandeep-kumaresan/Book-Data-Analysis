import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

st.title("Welcome to Book Data Analysis!")
st.snow()
st.text("Source:")
st.code("https://www.bookchor.com/category/6/fictioncomicsmangas")
df = pd.read_csv("Comics_Manga.csv")
df['Price'] = df['Price'].replace({'₹': '', ',': ''}, regex=True).astype(float)
st.text("Comics and Manga Prices")
st.bar_chart(data=df, x = "Price", y = "Title", x_label="Price", y_label="Book")
plt.figure(figsize=(8, 5))
# sns.countplot(data=df, x='Price', palette='viridis')
# plt.xticks(rotation=90)
# plt.title('Frequency of Each Book Price')
# plt.xlabel('Price')
# plt.ylabel('Count')
# st.pyplot(plt)
fig = px.bar(df, x = "Price", y = "Title")
st.plotly_chart(fig)

top_expensive_books = df.nlargest(10, 'Price')

plt.figure(figsize=(12, 8))
sns.barplot(data=top_expensive_books, x='Price', y='Title', palette='coolwarm')
plt.title('Top 10 Most Expensive Books in Comics and Manga')
plt.xlabel('Price')
plt.ylabel('Title')
st.pyplot(plt)

top_cheapest_books = df.nsmallest(10, 'Price')
plt.figure(figsize=(11,8))
sns.barplot(data= top_cheapest_books, x='Price',y='Title',palette='coolwarm')
plt.title('Top 10 Most cheapest Books in Comics and Manga')
plt.xlabel('Price')
plt.ylabel('Title')
st.pyplot(plt)

