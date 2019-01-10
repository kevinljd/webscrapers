from selenium import webdriver
import requests
from bs4 import BeautifulSoup

index = 1
base_url = 'https://www.sephora.com.au/categories/makeup/face/highlighter-and-illuminator?page='
curr_pg = base_url + str(index)

browser = webdriver.Chrome() # replace with .Firefox(), or with the browser of your choice
browser.get(curr_pg) #navigate to the page
innerHTML = browser.execute_script("return document.body.innerHTML")