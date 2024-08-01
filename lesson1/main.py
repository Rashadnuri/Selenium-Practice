from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time 

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com") ## istifadə edəcəyimiz saytın url-i

time.sleep(10) ## WebDriver anında bağlanmaması üçün istafə edəcəyimiz method

driver.back() ## URl daxilində hər-hansı manipulyasiya etdikdə geri dönüş etmək üçün istifadə edəcəyimiz method

time.sleep(3)

driver.forward() ## geri dönüş etdikdən sonra bir daha əvvəlki url-ə qayıtmağımız üçün istifadə etdiyimiz method

time.sleep(3)

driver.refresh() ## səhifəni yeniləmək üçün istifadə etdiyimiz method

time.sleep(3)