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
    price = page.locator(".price-current > strong").inner_text()
    expect(page.locator(".price-current > strong")).to_have_text("700")

    product.click_button_product_by_name("Купить")
    expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()
    time.sleep(1)
    expect(page.locator("#cart_total")).to_have_text(price)
    expect(page.locator("#cart_total_amount")).to_have_text("1")

def test_07_count_cart_logo(page: Page):
    office = SectionPage(page, "https://pumpenergy.ru/catalog/office")
    office.open()

    office.click_button_buy_in_product_card_by_title("Карта-флешка")
    expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()
    time.sleep(1)
    price_usb = page.locator('.product-item.shop2-product-item:has(a:has-text("Карта-флешка"))').locator(".product-price > strong").inner_text()

    expect(page.locator("#cart_total")).to_have_text(price_usb)
    expect(page.locator("#cart_total_amount")).to_have_text("1")


    office.click_button_buy_in_product_card_by_title("Бумажный пакет")
    expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()
    time.sleep(1)
    price_poket = page.locator('.product-item.shop2-product-item:has(a:has-text("Бумажный пакет"))').locator(".product-price > strong").inner_text()
    sum_usb_poket = int(price_usb) + int(price_poket)

    expect(page.locator("#cart_total")).to_have_text(str(sum_usb_poket))
    expect(page.locator("#cart_total_amount")).to_have_text("2")

    office.click_button_buy_in_product_card_by_title("Блокнот")
    expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()
    price_notebook = page.locator('.product-item.shop2-product-item:has(a:has-text("Блокнот"))').locator(".product-price > strong").inner_text()
    sum_usb_poket_notebook = int(price_usb) + int(price_poket) + int(price_notebook)

    # expect(page.locator("#cart_total")).to_contain_text(str(sum_usb_poket_notebook))
    expect(page.locator("#cart_total")).to_contain_text("1 050")
    expect(page.locator("#cart_total_amount")).to_have_text("3")

