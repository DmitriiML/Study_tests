# Импортировал из selenium'а webdriver и все необходимые библиотеки
# I imported all necessary stuff from selenium and other libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from faker import Faker
faker = Faker("en_US")
# Приветствие, каталог с выбором(input)
# Greetings and catalog of options
print("Приветствую Вас в нашем интернет магазине")
print("Выберите один из следующих товаров и укажите его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light, 3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie, 6 - Test.allTheThings() T-Shirt (Red)")
product = input()
# Настроил класс chrome options(Сохранил на всякий случай headless режим)

options = Options()
# options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)
# С помощью объекта driver и метода get открыл тестируемый сервис, вторым методом увеличил окно
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
# С помощью локаторов и инкапсулирующего класса By ввёл имя и пароль
user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys('standard_user')
print("Name input")
time.sleep(1)
user_pass = driver.find_element(By.XPATH, "//*[@id='password']")
user_pass.send_keys('secret_sauce')
time.sleep(1)
print("Password input")
time.sleep(1)
# С помощью локатора, инкапсулирующего класса By и метода click() нажимаю кнопку login
driver.find_element(By.CSS_SELECTOR, '#login-button').click()
# Проверяю url через оператор assert
url = 'https://www.saucedemo.com/inventory.html'
current_url = driver.current_url
assert current_url == url
print("All right, you're at the right place!")
time.sleep(1)
# Создал класс Goods(Товары) и его атрибуты
class Goods():
    def __init__(self, name, price, address):
        self.name = name
        self.price = price
        self.address = address
#Создал 6 экземпляров с указанными атрибутами(всё, что доступно на главной странице) и список
product1 = Goods('//*[@id="item_4_title_link"]', "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div", '//*[@id="add-to-cart-sauce-labs-backpack"]')
product2 = Goods('//*[@id="item_0_title_link"]', "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div", '//*[@id="add-to-cart-sauce-labs-bike-light"]')
product3 = Goods('//*[@id="item_1_title_link"]', "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div", '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
product4 = Goods('//*[@id="item_5_title_link"]', "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div", '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
product5 = Goods('//*[@id="item_2_title_link"]', "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div", '//*[@id="add-to-cart-sauce-labs-onesie"]')
product6 = Goods('//*[@id="item_3_title_link"]', "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div", '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
products = ['-', product1, product2, product3, product4, product5, product6]
#Создаю 2 переменных самого предмета и цены
item = driver.find_element(By.XPATH, products[int(product)].name).text
price = driver.find_element(By.XPATH, products[int(product)].price).text
# Пользуясь плодами знаний из ООП, печатаю товар и его цену
print(item,', price is ', price)
# Снова магия ООП позволяет добавить выбранный вначале товар в корзину
driver.find_element(By.XPATH, products[int(product)].address).click()
time.sleep(1)
item = driver.find_element(By.XPATH, products[int(product)].name).text
price = driver.find_element(By.XPATH, products[int(product)].price).text
# Открываю корзину
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]').click()
print("Cart enter")
time.sleep(1)
#Так как на каждый товар используется уникальный локатор, использую оператор if и проверяю наличие названия продукта, объединяю с проверкой цены товара с ценой в корзине, здесь всё стандартно через экземпляр и местный локатор цены
if item in driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]').text and price == driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div').text.lstrip(("Item total: ")):
    print("Your order is in the cart and price is correct!")
# Используя метод click и локатор перехожу на следующую страницу
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
time.sleep(1)
# Через локаторы, метод send_keys и библиотеку faker вводим рандомные ФИО и почтовый индекс
user_firstname = driver.find_element(By.XPATH, "//*[@id='first-name']")
user_firstname.send_keys(faker.first_name())
print("First Name input")
time.sleep(1)
user_lastname = driver.find_element(By.XPATH, "//*[@id='last-name']")
user_lastname.send_keys(faker.last_name())
print("Last Name input")
time.sleep(1)
user_postindex = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
user_postindex.send_keys(faker.random_int())
print("Post Index input")
time.sleep(1)
# Используя метод click и локатор перехожу на следующую страницу
driver.find_element(By.XPATH, '//*[@id="continue"]').click()
#Так как здесь аналогично на каждый товар используется уникальный локатор, использую снова оператор if и проверяю наличие названия продукта, объединяю с проверкой цены товара с указанной ценой, здесь всё стандартно через экземпляр и местный локатор цены
if item in driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]').text:
    assert price == driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]').text.lstrip("Item total: ")
    print("Вы выбирали номер", product, "и это", driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]').text)
    while True:
        print("Всё верно?(1 - да, это мой заказ, 2 - нет, здесь ошибка)")
        answer = input()
        if answer == "1":
            print('Item and price are correct, test is over')
            break
        elif answer == "2":
            print("А зачем врать? Подумайте ещё раз")
            continue
        else:
            print("Только 1 или 2! Подумайте ещё раз")
            continue
# Делаю победный скрин
driver.save_screenshot('screenshot.png')
time.sleep(1)
# Chrome закрывается сам, но оставил на всякий случай
# driver.close()
