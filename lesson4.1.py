from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
try:
    def fanc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    button = browser.find_element_by_id("book")
    button.click()
    
    input=browser.find_element_by_id("input_value")
    x=input.text
    y=fanc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()