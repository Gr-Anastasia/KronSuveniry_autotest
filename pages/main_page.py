from pages.base_page import BasePage
from components.header_menu import HeaderMenu
from components.left_menu import LeftMenu

class MainPage(BasePage):
    """
    Главная страница сайта
    """
    def __init__(self, page, url):
        super().__init__(page, url)

    def get_header_menu(self):
        return HeaderMenu(self.page, self.page.locator('.wrap-bottom-block'))

    def click_to_menu_up_by_title(self, title):
        return self.get_header_menu().get_by_title_menu(title).click()

    def click_to_menu_by_home(self):
        return self.get_header_menu().get_by_home_menu().click()

    def click_to_cart(self):
        return self.get_header_menu().get_card_button().wrapper.click()

    def get_left_menu(self):
        return LeftMenu(self.page, self.page.locator(".left-menu"))

    def click_to_left_menu_by_title(self, title):
        return self.get_left_menu().get_left_menu_by_title(title).click()

