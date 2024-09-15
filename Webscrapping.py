import requests
from bs4 import BeautifulSoup
url = "https://www.bookchor.com/category/6/fictioncomicsmangas"
r = requests.get(url)
print(r)
soup = BeautifulSoup(r.text,"lxml")
book = soup.find("div",class_="product-listing")
# print(book)
name = book.find_all("h3")
# name = detail.find_all()
bookname = []
for i in name:
    bookname.append(i.text)
bookprice = []
price = book.find_all("span")
for i in price[3:]:
    bookprice.append(i.text)
# print(len(bookname))
# print(len(bookprice))
