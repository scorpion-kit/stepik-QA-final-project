#файл с тест-кейсами
from pages.main_page import MainPage
from pages.login_page import LoginPage


def go_to_login_page(browser):
    #login_link = browser.find_element_by_css_selector("#login_link")
    login_link = browser.find_element_by_css_selector(*MainPageLocators.LOGIN_LINK)
    login_link.click()
    alert = self.browser.switch_to.alert
    alert.accept()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url) 
    login_page.should_be_login_page() #проверяем, является ли ссылка - ссылкой на страницу логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page2 = LoginPage(browser, link)
    page2.open()
    page2.should_be_login_page()


