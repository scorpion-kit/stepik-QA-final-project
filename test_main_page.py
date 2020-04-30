#файл с тест-кейсами
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

##def go_to_login_page(browser):
##    #login_link = browser.find_element_by_css_selector("#login_link")
##    login_link = browser.find_element_by_css_selector(*MainPageLocators.LOGIN_LINK)
##    login_link.click()
##    alert = self.browser.switch_to.alert
##    alert.accept()

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        self.page.open()                      # открываем страницу
        self.page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
        self.login_page = LoginPage(browser, browser.current_url) 
        self.login_page.should_be_login_page() #проверяем, является ли ссылка - ссылкой на страницу логина

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, link)
        self.page.open()
        self.page.should_be_login_link()
        
##def test_guest_can_go_to_login_page(browser):
##    link = "http://selenium1py.pythonanywhere.com/"
##    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
##    page.open()                      # открываем страницу
##    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
##    login_page = LoginPage(browser, browser.current_url) 
##    login_page.should_be_login_page() #проверяем, является ли ссылка - ссылкой на страницу логина

##def test_guest_should_see_login_link(browser):
##    link = "http://selenium1py.pythonanywhere.com/"
##    page = MainPage(browser, link)
##    page.open()
##    page.should_be_login_link()

def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()

def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.should_be_basket_empty_message()
