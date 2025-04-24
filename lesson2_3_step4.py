from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    # Подтверждаем (нажимаем ок) в модальном окне-алерте
    alert = browser.switch_to.alert.accept()

    # Решаем капчу для роботов
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    field = browser.find_element(By.CSS_SELECTOR, "#answer")
    field.send_keys(y)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла