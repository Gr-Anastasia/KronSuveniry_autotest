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

    def get_product_by_title(self, title):
        return ProductTitle(self.page, self.page.get_by_role("link", name=f"{title}").all()[1])

