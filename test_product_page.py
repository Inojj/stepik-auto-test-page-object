from pages.product_page import ProductPage
import pytest
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    #page.get_item_name()
    #page.should_be_item_added_to_card_msg()
    #page.cart_price_msg_equals_item_price()