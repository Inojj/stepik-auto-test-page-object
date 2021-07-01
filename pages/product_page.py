import math
from .base_page import BasePage
from.locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_item_name(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), \
            "Item name is not presented"
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

    def item_price(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), \
            "Item price is not presented"
        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text

    def should_be_item_added_to_card_msg(self):
        book_name = self.get_item_name()
        added_book = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_TO_CART).text
        assert added_book == book_name, "Book added to cart differs from current book name"

    def cart_price_msg_equals_item_price(self):
        item_price = self.item_price()
        cart_total = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_CARD).text
        assert item_price == cart_total, "Cart total is differs from Item price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), \
        "Success message is presented, but should not be"

    def disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES),\
            "Success message is not disappeared"


