from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent
from controls.input_all import InputAll
from controls.button_all import ButtonAll
from controls.checkbox_comparison import CheckboxComparison
from controls.title_product import ProductTitle

class ProductCardSection(BaseComponent):
    """
    Класс, описывающий карточку товара на страницах раздела
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_product_by_link(self, title):
        return ProductTitle(self.page, self.page.get_by_role("link", name=f"{title}").all()[1])

    def get_button_buy(self):
        return ButtonAll(self.page,  self.page.locator(f'.shop2-button-left:has-text("Купить")'))


