from pages.base_page import BasePage
from components.cart_delivery import CartDelivery
from components.cart_add_data import AddData


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

    def click_button_making_order(self):
        return self.get_cart_delivery().get_button_making_order().wrapper.click()

    def get_form_add_data(self):
        return AddData(self.page, self.page.locator("#order-form"))

    def fill_input_form_add_data(self, data, fill_value):
        return self.get_form_add_data().get_input_by_data(data).wrapper.fill(fill_value)

    def get_form_add_data_in_delivery_form_by_courier(self):
        return AddData(self.page, self.page.locator("#delivery-detail-7435709"))

    def get_form_add_data_in_delivery_form_by_post(self):
        return AddData(self.page, self.page.locator("#delivery-detail-7435909"))

    def fill_input_form_add_data_by_courier(self, data, fill_value):
        return self.get_form_add_data_in_delivery_form_by_courier().get_input_by_data(data).wrapper.fill(fill_value)

    def fill_input_form_add_data_by_post(self, data, fill_value):
        return self.get_form_add_data_in_delivery_form_by_post().get_input_by_data(data).wrapper.fill(fill_value)