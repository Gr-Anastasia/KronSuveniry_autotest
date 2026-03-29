import re
import time

from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.card_page import CardPage
from playwright.sync_api import expect, Page


def test_09_card(page: Page):
    product = ProductPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")
    main = MainPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")
    product.open()

    product.fill_input_count_by_title("5")
    expect(page.locator('input[name="amount"]')).to_have_value("5")

    product.click_button_product_by_name("Купить")
    expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    main.click_to_cart()
    expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
    expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
    expect(page.get_by_role("link", name="Тульский пряник")).to_be_visible()
    expect(page.locator('input[name="amounts[925418108]"]')).to_have_value("5")
    expect(page.locator('.shop2-cart-price').all()[0]).to_have_text("700")
    expect(page.locator('.shop2-cart-price').all()[1]).to_have_text("3 500")

def test_10_from_card_to_product(page: Page):
    card = CardPage(page, "https://pumpenergy.ru/catalog/cart")
    product = ProductPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")
    main = MainPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")

    product.open()
    product.click_button_product_by_name("Купить")
    expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    main.click_to_cart()
    expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
    expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
    expect(page.get_by_role("link", name="Тульский пряник")).to_be_visible()

    card.click_title_product_in_list_card("Тульский пряник")
    expect(page).to_have_url("https://pumpenergy.ru/catalog/pryanick-tula")
    expect(page.get_by_role("heading", name="Тульский пряник")).to_be_visible()






