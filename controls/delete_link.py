from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl

class DeleteLinkCard(BaseControl):
    """
    Класс, описывающий ссылку-иконку удалить на странице корзины
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
