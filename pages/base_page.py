from selenium.common.exceptions import NoSuchElementException

class BasePage():
    #конструктор — метод, который вызывается, когда мы создаем объект.
    #передаем экземпляр браузера и url 
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout) #команда для неявного ожидания
        
    def open(self):
        self.browser.get(self.url)

    #перехватываем исключение - нет элемента
        #как искать - (css, id, xpath и тд)
        #что искать - строку-селектор
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
