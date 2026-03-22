from pages.base_page import BasePage
from components.filter_price import FilterPrice
from components.product_card_mini import ProductCardSection

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

    def get_product_in_card(self):
        return ProductCardSection(self.page, self.page.locator(".product-item shop2-product-item"))

    def click_product_in_card_by_title(self, title):
        return self.get_product_in_card().get_product_by_title(title).wrapper.click()