from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl

class AddProductCount(BaseControl):
    """
    Класс, описывающий кнопку "+" в количестве в карточке товара на страницах разделов
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
