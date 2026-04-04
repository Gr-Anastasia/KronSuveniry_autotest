from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent
from controls.button_all import ButtonAll
from controls.checkbox_all import CheckboxDelivery


class CartDelivery(BaseComponent):
    """
    Класс, описывающий чек-боксы выбора способа доставки
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_checkbox_delivery(self, delivery):
        return CheckboxDelivery(self.page, self.wrapper.locator(f"label:has-text('{delivery}') input.delivery-radio"))

    def get_button_making_order_in_delivery(self):
        return ButtonAll(self.page, self.wrapper.get_by_role("link", name="Оформить заказ »"))







