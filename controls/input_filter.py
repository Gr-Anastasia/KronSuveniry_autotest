from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl

class InputFilter(BaseControl):
    """
    Класс, описывающий инпут для ввода 'цены от' и 'цены до' в фильтрах на страницах разделах
    """

    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
