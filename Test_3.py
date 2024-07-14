from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
import calendar
#Импортировал вебдрайвер и все необходимые библиотеки
options = Options()
driver = webdriver.Chrome(options=options)
#Создал экземпляр браузера и присвоил его значение переменной
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
#С помощью объекта driver и метода get открыл тестируемый сервис
driver.maximize_window()
time.sleep(1)
#Развернул окно браузера
new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
#Нашёл необходимый элемент по локатору/идентификатору
new_date.send_keys(Keys.BACKSPACE*10)
time.sleep(1)
print("Clear!")
#Стёр полностью дату

date_today = str(datetime.date.today()+ datetime.timedelta(days=10))
print(date_today)
new_date.send_keys(date_today)
time.sleep(3)
#Способ через библиотеку datetime

# day = int(datetime.datetime.utcnow().strftime("%d")) + 10
# print(day)
# date_today = datetime.datetime.utcnow().strftime("%m/" + str(day) +"/%Y")
# print(date_today)
# new_date.send_keys(date_today)
# time.sleep(1)
#Альтернативный "математический способ"

driver.save_screenshot('screenshot.png')
time.sleep(3)
print("Everything worked out! Congrats!")