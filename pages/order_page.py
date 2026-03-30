from pages.base_page import BasePage
from components.cart_delivery import CartDelivery


class OrderPage(BasePage):
    """
    Класс, описывающий страницу оформления заказа
    """
    def __init__(self, page, url):
        super().__init__(page, url)

    def get_cart_delivery(self):
        return CartDelivery(self.page, self.page.locator("#delivery-form"))

    def click_radiobutton_product_by_delivery(self, delivery):
        return self.get_cart_delivery().get_checkbox_delivery(delivery).wrapper.click()

