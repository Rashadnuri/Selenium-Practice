from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time 

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.facebook.com/")

print(driver.find_element("id" , "email")) # email id-li Web elementi tapmaq üçün istifadə edəcəyimiz method

driver.find_element("name" , "login").click() # id-ə uyğun gələn elementə klikləmək üçün 

time.sleep(5)