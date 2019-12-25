
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import math
import pytest

@pytest.mark.parametrize("promo_code", [1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail(reason="mistake on page")), 8, 9, 10])
def test_guest_can_add_product_to_basket(browser, promo_code):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_code}"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    product_name = page.should_be_product_name()
    page.should_be_the_same_name_and_message(product_name)
    basket_total = page.should_be_basket_total()
    page.should_be_the_same_price_and_basket_total(basket_total)

