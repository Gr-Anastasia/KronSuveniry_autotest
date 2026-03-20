from components.base_component import BaseComponent
from playwright.sync_api import Page, Locator

class LeftMenu(BaseComponent):
    """
    Левое меню сайта, содержащая название разделов
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_left_menu_by_title(self, title):
        return self.wrapper.locator(f"a:has-text('{title}')")

