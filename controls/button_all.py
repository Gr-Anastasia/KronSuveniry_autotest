from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl

class ButtonAll(BaseControl):
    """
    Класс, описывающий кнопки 'Показать' и 'Сбросить фильтр' в фильтрах на страницах разделах
    и кнопку "Купить" в карточке товара
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
