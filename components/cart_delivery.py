from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent
from controls.checkbox_all import CheckboxDelivery


class CartDelivery(BaseComponent):
    """
    Класс, описывающий чек-боксы выбора способа доставки
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_checkbox_delivery(self, delivery):
        return CheckboxDelivery(self.page, self.wrapper.locator(f"label:has-text('{delivery}') input.delivery-radio"))






