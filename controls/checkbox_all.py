from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl

class CheckboxDelivery(BaseControl):
    """
    Класс, описывающий чекбокс "Добавить к сравнению" в карточке товара
    и при выборе доставки
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
