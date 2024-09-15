import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv

# Specify the path to the chromedriver executable
chrome_driver_path = "/home/sandeep/Downloads/chromedriver-linux64/chromedriver"

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-infobars")

# Set up the Chrome service
service = Service(chrome_driver_path)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to scrape a single page using BeautifulSoup
def scrape_single_page(page_url):
    r = requests.get(page_url)
    soup = BeautifulSoup(r.text, "lxml")
    books = soup.find_all("div", class_="product-listing")

    bookname = []
    bookprice = []

    for book in books:
        name_tag = book.find("h3")
        if name_tag:
            bookname.append(name_tag.text.strip())
        price_tag = book.find("span")
        if price_tag:
            bookprice.append(price_tag.text.strip())

    return pd.DataFrame({"Bookname": bookname, "bookprice": bookprice})

# Function to scrape multiple pages using Selenium
def scrape_page(page_url, writer):
    driver.get(page_url)
    time.sleep(5)  # Wait for the page to load

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    books = soup.find_all('div', class_='product-item-info')

    bookname = []
    bookprice = []

    for book in books:
        title_tag = book.find('h3')
        price_tag = book.find('span')

        book_title = title_tag.text.strip() if title_tag else 'N/A'
        book_price = price_tag.text.strip() if price_tag else 'N/A'

        bookname.append(book_title)
        bookprice.append(book_price)
        writer.writerow([book_title, book_price])
        print(f"Title: {book_title}, Price: {book_price}")

# Base URL
base_url = "https://www.bookchor.com/category/6/fictioncomicsmangas?page="

# CSV file setup
csv_file = "books1.csv"
csv_columns = ["Title", "Price"]

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(csv_columns)  # Write the header

    # Loop through multiple pages
    for page in range(1, 9):  # Change the range as per the number of pages you want to scrape
        page_url = base_url + str(page)
        print(f"Scraping page: {page_url}")
        scrape_page(page_url, writer)

# Close the browser
driver.quit()



