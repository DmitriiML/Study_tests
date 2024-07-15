# Импортировал из selenium'а webdriver и все необходимые библиотеки
# I imported all necessary stuff from selenium and other libraries
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# С помощью объекта driver и метода get открыл тестируемый сервис, вторым методом увеличил окно
# Using driver and method get site being tested, using second I maximazed the window
driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
# Можно использовать неявное ожидание, но с ним дольше по времени(но для пробы вставлю под комментом)
# Implicity wait can be here also used, but it functions slower(below this comment this variant)
# driver.implicitly_wait(5)
# Создаю класс и общий метод для всего процесса(можно и без класса и метода, здесь для демонстрации способа)
# I create class and common method for all process(it can works even without it, just to demonstrate the way)
class Test1:
    def test_selection(self):
        #  Использую цикл, выдающий цифры от 1 до 6, которые вставляю в локаторы и таким образом перебираю пользователей
        # Using a loop produces numbers from 1 to 6, which I put in locators and sort through all users on the page
        for i in range(1, 7):
            # С помощью инкапсулирующего класса By нахожу локаторы и вставляю имена и пароль в поля и перехожу на
            # следующую страницу
            # Using this incapsulated class By I find locators and enter names and password and gp to the next page
            user_name = driver.find_element(By.ID, "user-name")
            user_name.send_keys(driver.find_element(By.XPATH, '//*[@id="login_credentials"]').text.splitlines()[i])
            print("Name input")
            user_pass = driver.find_element(By.XPATH, "//*[@id='password']")
            user_pass.send_keys(
                driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]').text.splitlines()[1])
            print("Password input")
            driver.find_element(By.CSS_SELECTOR, '#login-button').click()
            time.sleep(1)
            # Делаю скриншот с датой для каждого результата, используя библиотеку datetime
            # I make a screenschoot for all results using library datetime
            now_date = datetime.datetime.now().strftime("%H.%M.%S")
            screenshot_nam = "screenshot_n" + str(i) + "_" + now_date + ".png"
            driver.save_screenshot(screenshot_nam)
            print("Test №", i, "completed")
            # Использую конструкцию Try&Except(в случае отсутствия текста ошибки срабатывает оператор pass) для того,
            # чтобы после появления ошибки продолжить тест, очистив поля методом refresh
            # Using construction Try&Except(in case of absence of the failure text operator pass is triggered
            try:
                if driver.find_element(By.XPATH,
                                       '//*[@id="login_button_container"]/div/form/div[3]/h3').text == "Epic sadface: Sorry, this user has been locked out.":
                    print("Epic sadface: Sorry, this user has been locked out.")
                    driver.refresh()
                    continue
            except Exception:
                pass
            # По локатору открываю меню и используя явное ожидание прожиmаю кнопку logout
            # Using locator I open the menu and using explicit wait I press the button logout
            driver.find_element(By.XPATH, '//*[@id="menu_button_container"]/div/div[1]/div').click()
            WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
# Создаю экземпляр класса и запускаю метод test_selection()
# Create the exemplar of class and run the method test_selection()
test = Test1()
test.test_selection()
