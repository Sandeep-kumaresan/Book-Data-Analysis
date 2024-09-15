from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
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


def scrape_page(page_url, writer):
    driver.get(page_url)
    time.sleep(5)  # Wait for the page to load

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    books = soup.find_all('div', class_='product-listing')

    for book in books:
        title_tag = book.find_all('h3')  # Using find_all to get all h4 tags
        if title_tag:
            for title in title_tag:
                book_title = title.text.strip()
                book_url = book.find('a')['href']
                writer.writerow([book_title, book_url])
                print(f"Title: {book_title}, URL: {book_url}")


# Base URL
base_url = "https://www.bookchor.com/category/6/fictioncomicsmangas?page="

# CSV file setup
csv_file = "books.csv"
csv_columns = ["Title", "URL"]

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
