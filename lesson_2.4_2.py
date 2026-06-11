from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from math_func import calc

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока значение не станет "$100"
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    

    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    result = calc(x)
    # вывод полученного результата вычисления в теминал
    print(result)

    # получение поля, запись в переменную
    input = browser.find_element(By.ID, "answer")

    # ввод полученного значения в поле
    input.send_keys(result)

    # получение кнопки, запись в переменную 
    button1 = browser.find_element(By.ID, "solve")
    
    # клик по кнопке
    button1.click()   

finally:
     #ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
        # закрываем браузер после всех манипуляций
    browser.quit()