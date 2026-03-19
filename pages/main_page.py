from pages.base_page import BasePage
from components.header_menu import HeaderMenu

class MainPage(BasePage):
    """
    Главная страница сайта
    """
    def __init__(self, page, url):
        super().__init__(page, url)

    def vernut(self):
        return HeaderMenu

    def click_to_menu_up_by_title(self, title):
        return self.vernut.wrapper.get_by_title_menu
