from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from controls.input_all import InputAll
from controls.delete_link import DeleteLinkCard
from controls.title_product import ProductTitle


class ListCard(BaseComponent):
    """
    Класс, описывающий список товаров на страницы корзины и кнопку пересчитать
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_title_link(self, title):
        return ProductTitle(self.page, self.page.get_by_role("link", name=f"{title}"))

    def get_input_count(self):
        return InputAll(self.page, self.wrapper.locator('//input[contains(@name, "amounts")]'))

    def get_delete_icon(self):
        return DeleteLinkCard(self.page, self.wrapper.get_by_title("Удалить"))

    def get_price_by_title(self):
        price = self.wrapper.locator('.shop2-cart-price').all()[0]
        return price

