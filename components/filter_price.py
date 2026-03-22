from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent
from controls.input_all import InputAll
from controls.button_all import ButtonAll

class FilterPrice(BaseComponent):
    """
    Класс, описывающий компонент фильтра Цены (цена от и до, кнопки)
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    # def get_input_filter_price_by_name(self, name):
    #     return InputFilter(self.page, self.page.locator(f'label:has-text("{name}") > input'))

    def get_input_filter_price_by_name(self, name):
        return InputAll(self.page, self.page.locator(f'//label[contains(text(), "{name}")]/input'))

    def get_button_filter_price_by_name(self, name):
        return ButtonAll(self.page, self.page.locator(f'.shop2-button-left:has-text("{name}")'))

