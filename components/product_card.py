from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent
from controls.input_all import InputAll
from controls.button_all import ButtonAll
from controls.checkbox_comparison import CheckboxComparison
from controls.add_count_input import AddProductCount
from controls.remove_count_input import RemoveProductCount


class ProductCard(BaseComponent):
    """
    Класс, описывающий страницу карточки товара
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_button_in_product_by_name(self, name):
        return ButtonAll(self.page, self.wrapper.locator(f'.shop2-button-left:has-text("{name}")'))

    def get_add_count_input(self):
        return AddProductCount(self.page, self.wrapper.locator(".product-amount-button p-plus"))

    def get_remove_count_input(self):
        return RemoveProductCount(self.page, self.wrapper.locator(".product-amount-button p-minus"))

    def get_input_count(self):
        return InputAll(self.page, self.wrapper.locator('input[name="amount"]'))



