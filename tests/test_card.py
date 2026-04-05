import time
from playwright.sync_api import expect, Page

from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.card_page import CardPage
from pages.section_page import SectionPage


def test_09_card(page: Page):
    product = ProductPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")
    main = MainPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")
    product.open()

    price = page.locator(".price-current > strong").inner_text()
    product.fill_input_count_by_title("5")
    expect(page.locator('input[name="amount"]')).to_have_value("5")

    product.click_button_product_by_name("Купить")
    expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    main.click_to_cart()
    count = page.locator('input[name="amounts[925418108]"]').input_value()
    sum_pie = int(price) * int(count)
    expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
    expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
    expect(page.get_by_role("link", name="Тульский пряник")).to_be_visible()
    expect(page.locator('input[name="amounts[925418108]"]')).to_have_value(count)
    expect(page.locator('.shop2-cart-price').all()[0]).to_have_text(price)
    expect(page.locator('.shop2-cart-price').all()[1]).to_have_text("3 500")
    # expect(page.locator('.shop2-cart-price').all()[1]).to_have_text(str(sum_pie))

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

def test_11_card_count(page: Page):
    office = SectionPage(page, "https://pumpenergy.ru/catalog/office")
    main = MainPage(page, "https://pumpenergy.ru/catalog/office")
    card = CardPage(page, "https://pumpenergy.ru/catalog/cart")
    office.open()

    office.click_button_buy_in_product_card_by_title("Карта-флешка")
    expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()
    time.sleep(1)
    office.click_button_buy_in_product_card_by_title("Бумажный пакет")
    expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    main.click_to_cart()
    time.sleep(2)
    expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
    expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
    expect(page.get_by_role("link", name="Карта-флешка")).to_be_visible()
    expect(page.get_by_role("link", name="Бумажный пакет")).to_be_visible()

    price_usb = page.locator("#cart-row-925428108 > .shop2-cart-price").all()[1].inner_text()
    price_poket = page.locator("#cart-row-925402708 > .shop2-cart-price").all()[1].inner_text()
    count_usb_before = page.locator('input[name="amounts[925428108]"]').input_value()
    count_poket = page.locator('input[name="amounts[925402708]"]').input_value()
    sum_usb_before = int(price_usb) * int(count_usb_before)
    sum_poket = int(price_poket) * int(count_poket)
    sum_card_before = sum_usb_before + sum_poket
    time.sleep(1)
    expect(page.locator('//*[@class="total-price last-line"]')).to_contain_text(str(sum_card_before))

    card.fill_count_product_by_title_in_list_card("Карта-флешка", "22")
    page.keyboard.press("Enter")
    card.click_button_product_by_name("Пересчитать")

    count_usb_before = page.locator('input[name="amounts[925428108]"]').input_value()
    sum_usb_after = int(price_usb) * int(count_usb_before)
    sum_card_after = sum_usb_after + sum_poket
    expect(page.locator('//*[@class="total-price last-line"]')).to_contain_text("8 100")
    # expect(page.locator('//*[@class="total-price last-line"]')).to_contain_text(str(sum_card_after))

    card.click_delete_product_by_title_in_list_card("Бумажный пакет")

    expect(page.get_by_role("link", name="Карта-флешка")).to_be_visible()
    expect(page.get_by_role("link", name="Бумажный пакет")).to_be_hidden()

    time.sleep(1)
    card.click_button_product_by_name("Очистить корзину")
    expect(page.locator("p", has_text="Корзина пуста")).to_be_visible()

