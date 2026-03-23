from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent
from controls.input_all import InputAll
from controls.button_all import ButtonAll
from controls.checkbox_comparison import CheckboxComparison
from controls.title_product import ProductTitle

class ProductCard(BaseComponent):
    """
    Класс, описывающий страницу карточки товара
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_button_in_product_by_name(self, name):
        return ButtonAll(self.page, self.page.locator(f'.shop2-button-left:has-text("{name}")'))

