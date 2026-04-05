from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from controls.button_all import ButtonAll


class FormOrderWithoutRegistration(BaseComponent):
    """
    Класс, описывающий форму 'Оформить заказ' и кнопку купить без регистрации
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_button_by_name(self, name):
        return ButtonAll(self.page, self.wrapper.locator(f".shop2-button-left:has-text('{name}')"))
