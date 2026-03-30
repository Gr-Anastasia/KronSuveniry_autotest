import re
import time

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.card_page import CardPage
from playwright.sync_api import expect, Page

from pages.section_page import SectionPage


def test_12_making_an_order(page: Page):
    poster = SectionPage(page, "https://pumpenergy.ru/catalog/literature")
    main = MainPage(page, "https://pumpenergy.ru/catalog/office")
    card = CardPage(page, "https://pumpenergy.ru/catalog/cart")
    order = OrderPage(page, "https://pumpenergy.ru/catalog?mode=order")
    poster.open()

    poster.click_button_buy_in_product_card_by_title("Плакат WQB")
    expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    main.click_to_cart()
    expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
    expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
    expect(page.get_by_role("link", name="Плакат WQB")).to_be_visible()

    card.click_button_buy_no_register()
    expect(page).to_have_url("https://pumpenergy.ru/catalog?mode=order")
    expect(page.get_by_role("heading", name="Доставка")).to_be_visible()
    time.sleep(2)

    order.click_radiobutton_product_by_delivery("Курьер - бесплатно")
    time.sleep(5)





