import time

from pages.product_page import ProductPage
from pages.section_page import SectionPage
from playwright.sync_api import expect, Page

def test_06_go_to_cart_product(page: Page):
    food = SectionPage(page, "https://pumpenergy.ru/catalog/eatable")
    product = ProductPage(page,"https://pumpenergy.ru/catalog/pryanick-tula")
    food.open()

    food.click_product_in_card_by_link("Тульский пряник")
    expect(page).to_have_url("https://pumpenergy.ru/catalog/pryanick-tula")
    expect(page.get_by_role("heading", name="Тульский пряник")).to_be_visible()
    expect(page.locator(".price-current > strong")).to_have_text("700")

    product.click_button_product_by_name("Купить")
    expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()
    time.sleep(2)
    expect(page.locator("#cart_total")).to_have_text("700")
    expect(page.locator("#cart_total_amount")).to_have_text("1")

def test_07_count_cart_logo(page: Page):
    office = SectionPage(page, "https://pumpenergy.ru/catalog/office")
    office.open()

    office.click_button_buy_in_product_card_by_title("Карта-флешка")
    office.click_button_buy_in_product_card_by_title("Бумажный пакет")
    office.click_button_buy_in_product_card_by_title("Блокнот")


