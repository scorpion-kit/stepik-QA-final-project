from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

import pytest
import random
import time

@pytest.mark.xfail(reason="wrong message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    #product_page.solve_quiz_and_get_code()
    #time.sleep(5)
    product_page.should_not_be_success_message()
    product_page.should_be_book_price()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail(reason="not disappiring")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.is_dissappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage (browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_be_book_name()
    product_page.should_be_book_price()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.should_be_basket_empty_message()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        count = random.randint(1, 100)
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time() + count)
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.product_page = ProductPage(browser, link)
        self.product_page.open()
        self.product_page.should_not_be_success_message()
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	product_page = ProductPage (browser, link)
	product_page.open()
	product_page.add_to_basket()
	product_page.solve_quiz_and_get_code()
	time.sleep(5)
	product_page.should_be_book_name()
	product_page.should_be_book_price()
