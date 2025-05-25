import time
import random
import string
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options

def generate_random_query():
    length = random.randint(3, 5)
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

options = Options()
options.add_argument("--disable-notifications")
driver_path = "C:\\Binaries\\edgedriver_win64\\msedgedriver.exe"

service = Service(driver_path)
driver = webdriver.Edge(service=service, options=options)

try:
    driver.get("https://www.bing.com")
    time.sleep(3)  
    
    for _ in range(31):  
        query = generate_random_query()
        print(f"Searching for: {query}")
        
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        time.sleep(10)  

finally:
    driver.quit()
    print("Browser closed.")
