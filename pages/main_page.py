from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators #импорт локаторов 

class MainPage(BasePage): 
    def go_to_login_page(self):
       login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
       login_link.click()

    #проверить наличие ссылки;
    #*MainPageLocators.LOGIN_LINK - кортеж, который надо распаковать
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
            "Login link is not presented"
