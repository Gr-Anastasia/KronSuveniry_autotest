from playwright.sync_api import Page, Locator


class BaseComponent:
    """
    Базовый класс для компонентов
    """
    def __init__(self, page: Page, wrapper: Locator):
        self.page = page
        self.wrapper: Locator = wrapper