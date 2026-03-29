from pages.base_page import BasePage
from components.card_form import FormCard
from components.card_list import ListCard


class CardPage(BasePage):
    """
    Класс, описывающий страницу корзины
    """
    def __init__(self, page, url):
        super().__init__(page, url)

    def get_form_card(self):
        return FormCard(self.page, self.page.locator("#shop2-cart"))

    def click_button_product_by_name(self, name):
        return self.get_form_card().get_button_by_name(name).wrapper.click()

    def get_lict_card_by_title(self, title):
        return ListCard(self.page, self.page.locator(f'//a[text()="[{title}]"]/ancestor::tr[contains(@id, "cart-row")]'))

    def click_title_product_in_list_card(self, title):
        return self.get_lict_card_by_title(title).get_title_link(title).wrapper.click()

    def fill_count_product_by_title_in_list_card(self, title):
        return self.get_lict_card_by_title(title).get_input_count().wrapper.fill()

    def click_delete_product_by_title_in_list_card(self, title):
        return self.get_lict_card_by_title(title).get_delete_icon().wrapper.click()
