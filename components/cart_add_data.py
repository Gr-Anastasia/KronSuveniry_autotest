from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent
from controls.button_all import ButtonAll
from controls.input_all import InputAll


class AddData(BaseComponent):
    """
    Класс, описывающий форму для заполнения данными на странице оформления заказа
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_input_by_data(self, data):
        return InputAll(self.page, self.wrapper.locator(f"label:has-text('{data}') input"))

    def get_button_making_order(self):
        return ButtonAll(self.page, self.wrapper.get_by_role("link", name="Оформить заказ »"))





