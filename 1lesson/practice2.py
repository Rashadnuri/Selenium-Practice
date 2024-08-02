from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://selenium.dev/')

time.sleep(3)
