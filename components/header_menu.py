from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent


class HeaderMenu(BaseComponent):
    """
    Верхнее меню сайта, содержащая разделы и строку поиска
    """
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_navigation_menu(self):
        return self.wrapper.locator('nav')

    def get_by_title_menu(self, title):
        return self.get_navigation_menu().locator(f"a:has-text('{title}')")

    def get_by_home_menu(self):
        return self.wrapper.locator('.home')

