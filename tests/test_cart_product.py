import time
import allure
from playwright.sync_api import expect, Page

from pages.product_page import ProductPage
from pages.section_page import SectionPage

@allure.title("Переход в карточку товара")
@allure.feature("Работа карточек товара")
@allure.id("06")
def test_06_go_to_cart_product(page: Page):
    food_page = SectionPage(page, "https://pumpenergy.ru/catalog/eatable")
    product_page = ProductPage(page,"https://pumpenergy.ru/catalog/pryanick-tula")

    with allure.step("Предусловие: Открытие страницы https://pumpenergy.ru/catalog/eatable "):
        food_page.open()

    with allure.step("Нажать на название карточки товара [Тульский пряник]"):
        food_page.click_product_in_card_by_link("Тульский пряник")
        expect(page).to_have_url("https://pumpenergy.ru/catalog/pryanick-tula")
        expect(page.get_by_role("heading", name="Тульский пряник")).to_be_visible()
        price = page.locator(".price-current > strong").inner_text()
        expect(page.locator(".price-current > strong")).to_have_text("700")

    with allure.step("Нажать кнопку [Купить]"):
        product_page.click_button_product_by_name("Купить")
        expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()
        time.sleep(1)
        expect(page.locator("#cart_total")).to_have_text(price)
        expect(page.locator("#cart_total_amount")).to_have_text("1")

@allure.title("Обновление количества в иконки корзины в Хэдере")
@allure.feature("Работа карточек товара")
@allure.id("07")
def test_07_count_cart_logo(page: Page):
    office_page = SectionPage(page, "https://pumpenergy.ru/catalog/office")

    with allure.step("Предусловие: Открытие страницы https://pumpenergy.ru/catalog/office"):
        office_page.open()

    with allure.step("Нажать кнопку [Купить] у товара «Карта-флешка»"):
        office_page.click_button_buy_in_product_card_by_title("Карта-флешка")
        expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()
        time.sleep(1)
        price_usb = page.locator('.product-item.shop2-product-item:has(a:has-text("Карта-флешка"))').locator(".product-price > strong").inner_text()
        expect(page.locator("#cart_total")).to_have_text(price_usb)
        expect(page.locator("#cart_total_amount")).to_have_text("1")

    with allure.step("Нажать кнопку [Купить] у товара «Бумажный пакет»"):
        office_page.click_button_buy_in_product_card_by_title("Бумажный пакет")
        expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()
        time.sleep(1)
        price_poket = page.locator('.product-item.shop2-product-item:has(a:has-text("Бумажный пакет"))').locator(".product-price > strong").inner_text()
        sum_usb_poket = int(price_usb) + int(price_poket)
        expect(page.locator("#cart_total")).to_have_text(str(sum_usb_poket))
        expect(page.locator("#cart_total_amount")).to_have_text("2")

    with allure.step("Нажать кнопку [Купить] у товара «Блокнот»"):
        office_page.click_button_buy_in_product_card_by_title("Блокнот")
        expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()
        price_notebook = page.locator('.product-item.shop2-product-item:has(a:has-text("Блокнот"))').locator(".product-price > strong").inner_text()
        sum_usb_poket_notebook = int(price_usb) + int(price_poket) + int(price_notebook)
        time.sleep(1)

        cart_total = page.locator("#cart_total").inner_text()
        cart_total_clean = cart_total.replace("\u00A0", "")

        assert cart_total_clean == str(sum_usb_poket_notebook)
        expect(page.locator("#cart_total_amount")).to_have_text("3")
