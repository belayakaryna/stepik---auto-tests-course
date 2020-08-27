from selenium import webdriver
import time
import math

try:
    def fanc(x):
     return str(math.log(abs(12*math.sin(int(x)))))
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    confirm=browser.switch_to.alert
    confirm.accept()
    input=browser.find_element_by_id("input_value")
    x=input.text
    y=fanc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()