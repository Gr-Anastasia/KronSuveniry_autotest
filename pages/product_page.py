from pages.base_page import BasePage
from components.product_card import ProductCard


class ProductPage(BasePage):
    """
    Класс, описывающий страницу товара
    """
    def __init__(self, page, url):
        super().__init__(page, url)

    def get_product(self):
        return ProductCard(self.page, self.page.locator(".content-inner"))

    def click_button_product_by_name(self, name):
        return self.get_product().get_button_in_product_by_name(name).wrapper.click()

    def click_button_add_count_input_by_title(self):
        return self.get_product().get_add_count_input().wrapper.click()

    def click_button_remove_count_input_by_title(self):
        return self.get_product().get_remove_count_input().wrapper.click()

    def fill_input_count_by_title(self, fill_value):
        return self.get_product().get_input_count().wrapper.fill(f"{fill_value}")