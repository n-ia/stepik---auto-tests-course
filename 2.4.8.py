from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    #говорим повторять в течении 12 сек, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )
    button = browser.find_element_by_id("book")
    button.click()  
    #решить задачу
    x_element = browser.find_element_by_id("input_value")
    x=x_element.text
    y=calc(x)
    #ищем строчку для ввода ответа
    z = browser.find_element_by_id("answer")
    z.send_keys(y)
    #нажимаем ответ
    button1 = browser.find_element_by_id("solve")
    button1.click()   
finally:
    time.sleep(15)
    browser.quit() 