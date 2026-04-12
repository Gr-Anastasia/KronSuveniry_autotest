from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from controls.input_all import InputAll
from controls.button_all import ButtonAll


class ProductCard(BaseComponent):
    """
    Класс, описывающий форму карточки товара на странице товара
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_button_in_product_by_name(self, name):
        return ButtonAll(self.page, self.wrapper.locator(f'.shop2-button-left:has-text("{name}")'))

    def get_input_count(self):
        return InputAll(self.page, self.wrapper.locator('input[name="amount"]'))

    def get_price(self):
        price = self.wrapper.locator('.price-current > strong')
        return price

