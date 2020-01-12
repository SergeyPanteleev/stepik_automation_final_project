from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


#links for promo
xfail_offer = 7
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
links = [link+str(i) for i in range(10) if i != xfail_offer]
xfail_link = pytest.param(link+str(xfail_offer), marks=pytest.mark.xfail(reason="the page should be fixed"))
links.insert(xfail_offer, xfail_link)

#link for product
link_product = ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"]

#link for product with alert
link_with_alert = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"]

@pytest.mark.need_review
@pytest.mark.parametrize("link", links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    product_name = page.should_be_product_name()
    page.should_be_the_same_name_and_message(product_name)
    basket_total = page.should_be_basket_total()
    page.should_be_the_same_price_and_basket_total(basket_total)


@pytest.mark.xfail
@pytest.mark.parametrize("link", links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.parametrize("link", links)
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize("link", links)
def test_message_disappeared_after_adding_product_to_basket(browser, link): 
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.should_be_disappeared_success_message()


@pytest.mark.parametrize("link", link_product)
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
@pytest.mark.parametrize("link", link_product)
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
@pytest.mark.parametrize("link", link_product)
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.no_products_in_basket()
    page.basket_is_empty_message()


@pytest.mark.parametrize("link", link_with_alert)
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.page = LoginPage(browser, login_link)
        self.page.open()
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()
    
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_price()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        product_name = page.should_be_product_name()
        page.should_be_the_same_name_and_message(product_name)
        basket_total = page.should_be_basket_total()
        page.should_be_the_same_price_and_basket_total(basket_total)
    