import pandas as pd
import requests
from bs4 import BeautifulSoup
from cleo.helpers import option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import csv
import time

chrome_driver_path = "/home/sandeep/Downloads/chromedriver-linux64/chromedriver"
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service,options=chrome_options)

def scrape_page(page_url,):

baseurl = "https://www.bookchor.com/category/16/nonfictionengineering"
csvfile = "Engineering.csv"
csv_columns = ["Title","Price"]
