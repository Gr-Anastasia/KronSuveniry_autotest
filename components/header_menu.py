from components.base_component import BaseComponent


class HeaderMenu(BaseComponent):
    """
    Верхнее меню сайта, содержащая разделы и строку поиска
    """
    def __init__(self, page, wrapper):
        super().__init__(page, page.locator('.wrap-bottom-block'))

    def get_by_title_menu(self, title):
        return self.wrapper.page.locator(f"a:has-text('{title}')")

    def get_by_home_menu(self):
        return self.wrapper.page.locator('.home')

