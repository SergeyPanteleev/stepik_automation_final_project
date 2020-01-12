from .base_page import BasePage
from .basket_page import BasketPage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_basket(self): 
        try:
            button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
            button.click() 
        except:
            assert False, "Basket's button is not found"

    def should_be_product_name(self):
        try:
            product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
            return product_name
        except:
            assert False, "Product name is not found"

    def should_be_the_same_name_and_message(self, product_name):
        assert product_name == self.browser.find_element(*ProductPageLocators.BUSKETS_ADD_MESSAGE).text, \
            "Product name and message in basket are different"

    def should_be_basket_total(self):
        try:
            basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
            return basket_total
        except:
            assert False, "Basket total is not found"

    def should_be_price(self):
        try:
            price = self.browser.find_element(*ProductPageLocators.PRICE).text
            return price
        except:
            assert False, "Price is not found"

    def should_be_the_same_price_and_basket_total(self, price):
        assert price == self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text, \
            "Basket total and good's price are different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BUSKETS_ADD_MESSAGE), \
           "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.BUSKETS_ADD_MESSAGE), \
           "Success message is presented, but should disappear"
