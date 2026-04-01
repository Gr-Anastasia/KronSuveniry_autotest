import re
import time

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.card_page import CardPage
from playwright.sync_api import expect, Page

from pages.product_page import ProductPage
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

    order.click_radiobutton_product_by_delivery("Самовывоз - бесплатно")
    expect(page.get_by_label("Самовывоз - бесплатно")).to_be_checked()

    order.click_button_making_order()
    expect(page.get_by_role("heading", name="Оформление заказа")).to_be_visible()
    expect(page.get_by_label("ФИО")).to_be_visible()
    expect(page.get_by_label("Компания")).to_be_visible()
    expect(page.get_by_label("Телефон")).to_be_visible()
    expect(page.get_by_label("E-mail")).to_be_visible()
    expect(page.get_by_label("Дополнительная информация")).to_be_visible()


    order.fill_input_form_add_data("ФИО", "Арбузов Иван Петрович")
    order.fill_input_form_add_data("Компания", "Технотекст")
    order.fill_input_form_add_data("Телефон", "88005553535")
    order.fill_input_form_add_data("E-mail", "qa@mail.com")

    # expect(page.get_by_label("ФИО")).to_have_text("Арбузов Иван Петрович")
    # expect(page.get_by_label("Компания")).to_have_text("Технотекст")
    # expect(page.get_by_label("Телефон")).to_have_text("88005553535")
    # expect(page.get_by_label("E-mail")).to_have_text("qa@mail.com")

    time.sleep(2)

def test_13_making_an_order_not_all_data(page: Page):
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

    order.click_radiobutton_product_by_delivery("Самовывоз - бесплатно")
    expect(page.get_by_label("Самовывоз - бесплатно")).to_be_checked()

    order.click_button_making_order()
    expect(page.get_by_role("heading", name="Оформление заказа")).to_be_visible()
    expect(page.get_by_label("ФИО")).to_be_visible()
    expect(page.get_by_label("Компания")).to_be_visible()
    expect(page.get_by_label("Телефон")).to_be_visible()
    expect(page.get_by_label("E-mail")).to_be_visible()
    expect(page.get_by_label("Дополнительная информация")).to_be_visible()


    order.fill_input_form_add_data("Компания", "Технотекст")
    order.fill_input_form_add_data("E-mail", "qa@mail.com")

    order.click_button_making_order()

    expect(page.locator(".error")).to_have_text("ФИО: это поле обязательно для заполнения!/"
                                                "Телефон: это поле обязательно для заполнения. Неверный формат телефона!/"
                                                "E-mail: это поле обязательно для заполнения. Неверный формат адреса электронной почты!")


    # expect(page.get_by_label("ФИО")).to_have_text("Арбузов Иван Петрович")
    # expect(page.get_by_label("Компания")).to_have_text("Технотекст")
    # expect(page.get_by_label("Телефон")).to_have_text("88005553535")
    # expect(page.get_by_label("E-mail")).to_have_text("qa@mail.com")

    time.sleep(2)


def test_14_making_an_order_courier(page: Page):
    pie = ProductPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")
    main = MainPage(page, "https://pumpenergy.ru/catalog/office")
    card = CardPage(page, "https://pumpenergy.ru/catalog/cart")
    order = OrderPage(page, "https://pumpenergy.ru/catalog?mode=order")
    pie.open()

    pie.click_button_product_by_name("Купить")
    expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    main.click_to_cart()
    expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
    expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
    expect(page.get_by_role("link", name="Тульский пряник")).to_be_visible()

    card.click_button_buy_no_register()
    expect(page).to_have_url("https://pumpenergy.ru/catalog?mode=order")
    expect(page.get_by_role("heading", name="Доставка")).to_be_visible()

    order.click_radiobutton_product_by_delivery("Курьер - бесплатно")
    expect(page.get_by_label("Курьер - бесплатно")).to_be_checked()

    time.sleep(2)

    expect(page.get_by_label("Адрес доставки:")).to_be_visible()
    expect(page.locator(".delivery-type.delivery-type-current label:has(span:has-text('Телефон:'))")).to_be_visible()
    expect(page.locator(".delivery-type.delivery-type-current label:has(span:has-text('Дата и время доставки:'))")).to_be_visible()

    order.click_button_making_order()
    expect(page.locator(".error")).to_have_text("Неверно заполнено поле: Адрес доставки")




