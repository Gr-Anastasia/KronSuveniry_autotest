from playwright.sync_api import Page

from pages.base_page import BasePage
from components.product_card import ProductCard


class ProductPage(BasePage):
    """
    Класс, описывающий страницу товара
    """
    def __init__(self, page, url):
        super().__init__(page, url)

    def get_product(self):
        return ProductCard(self.page, self.page.locator(".content-inner"))

    def click_button_product_by_name(self, name):
        return self.get_product().get_button_in_product_by_name(name).wrapper.click()

    def fill_input_count_by_title(self, fill_value):
        return self.get_product().get_input_count().wrapper.fill(f"{fill_value}")

    def inner_price(self):
        return self.get_product().get_price().inner_text()

    def input_value(self):
        return self.get_product().get_input_count().wrapper.input_value()
