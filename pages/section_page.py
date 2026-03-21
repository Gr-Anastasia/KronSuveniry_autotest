from pages.base_page import BasePage
from components.filter_price import FilterPrice

class SectionPage(BasePage):
    """
    Класс, описывающий страницы раздела категорий сайта: офис, съедобное, флешки, литература, выставки и карты озон
    """
    def __init__(self, page, url):
        super().__init__(page, url)

    def get_filter(self):
        return FilterPrice(self.page, self.page.locator('.shop2-filter'))

    def fill_filter_price_by_name(self, name, fill_value):
        return self.get_filter().get_input_filter_price_by_name(name).wrapper.fill(fill_value)

    def click_button_by_name(self, name):
        return self.get_filter().get_button_filter_price_by_name(name).wrapper.click()