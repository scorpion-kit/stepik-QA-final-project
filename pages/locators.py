from selenium.webdriver.common.by import By

#селектор - это пара: как искать и что искать
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    #регистрация
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#login_form")
    #логин
    LOGIN_FORM = (By.CSS_SELECTOR, "#register_form")
    #url
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
