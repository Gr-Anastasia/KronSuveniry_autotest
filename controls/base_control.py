from playwright.sync_api import Page, Locator, expect


class BaseControl:
    def __init__(self, page: Page, wrapper: Locator):
        self.page = page
        self.wrapper: Locator = wrapper

