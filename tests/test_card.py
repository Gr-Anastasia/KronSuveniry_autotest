import time

from pages.product_page import ProductPage
from playwright.sync_api import expect, Page


def test_09_card(page: Page):
    product = ProductPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")
    product.open()

    product.fill_input_count_by_title("5")
    expect(page.locator('input[name="amount"]')).to_have_value("5")
    time.sleep(2)

    product.click_button_product_by_name("Купить")
    expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()


    # expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
    time.sleep(2)



