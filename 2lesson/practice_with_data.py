from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time 

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org")

url = driver.current_url  # ilk açılan səhifənin url-ni göstərmək üçün istifadə etdiyimiz atribut
print("səhifənin URL-i - " , url)   # açılan url-in məlumatlarını terminalda görmək üçün 
assert url == "https://www.wikipedia.org/", "URL-in uyğunluq səhvi, düzgün səhifə açilmamişdir."  # Url-in eyni olmasını yoxlamaq üçün 

current_title = driver.title # açılan səhifənin başlığını göstərmək üçün istifadə etdiyimiz atribut
print("səhifənin başliği - " , current_title) 
assert current_title == "Wikipedia", "Başliğin uyğunsuzluq səhvi"

print (driver.page_source)  # Səhifənin kodunu terminalda göstərmək üçün 

time.sleep(3)

