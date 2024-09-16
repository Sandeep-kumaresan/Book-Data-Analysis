from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time

chrome_driver_path = "/home/sandeep/Downloads/chromedriver-linux64/chromedriver"

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-infobars")

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

def scrape_page(page_url, writer):
    driver.get(page_url)
    time.sleep(5) 

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

base_url = "https://www.bookchor.com/category/29/textbookslaw?page="

csv_file = "LawBook.csv"
csv_columns = ["Title", "Price"]

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(csv_columns)  


    for page in range(1, 11): 
        page_url = base_url + str(page)
        print(f"Scraping page: {page_url}")
        scrape_page(page_url, writer)

driver.quit()