import time
import allure
from playwright.sync_api import expect, Page

from pages.card_page import CardPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.section_page import SectionPage

@allure.title("Работа корзины")
@allure.feature("Работа корзины")
@allure.id("09")
def test_09_card(page: Page):
    product_page = ProductPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")
    main_page = MainPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")
    card_page = CardPage(page, "https://pumpenergy.ru/catalog/cart")

    with allure.step("Предусловие: Открытие страницы https://pumpenergy.ru/catalog/pryanick-tula"):
        product_page.open()
        price = product_page.inner_price()

    with allure.step("Ввод количества '5' в поле количество"):
        product_page.fill_input_count_by_title("5")
        expect(page.locator('input[name="amount"]')).to_have_value("5")

    with allure.step("Нажать кнопку 'Купить'"):
        product_page.click_button_product_by_name("Купить")
        expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    with allure.step("Нажать кнопку корзины в верхнем левом углу"):
        main_page.click_to_cart()
        count = card_page.count_input_value("Тульский пряник")
        sum_pie = int(price) * int(count)
        cart_total_clean = card_page.get_cart_total_clean
        assert cart_total_clean(page) == str(sum_pie)
        expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
        expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
        expect(page.get_by_role("link", name="Тульский пряник")).to_be_visible()
        expect(page.locator('input[name="amounts[925418108]"]')).to_have_value(count)
        expect(page.locator('.shop2-cart-price').all()[0]).to_have_text(price)

@allure.title("Переход на карточку товара из корзины")
@allure.feature("Работа корзины")
@allure.id("10")
def test_10_from_card_to_product(page: Page):
    card_page = CardPage(page, "https://pumpenergy.ru/catalog/cart")
    product_page = ProductPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")
    main_page = MainPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")

    with allure.step("Предусловие: Открытие страницы https://pumpenergy.ru/catalog/pryanick-tula "):
        product_page.open()

    with allure.step("Нажать кнопку [Купить]"):
        product_page.click_button_product_by_name("Купить")
        expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    with allure.step("Нажать на кнопку корзины в верхнем правом меню"):
        main_page.click_to_cart()
        expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
        expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
        expect(page.get_by_role("link", name="Тульский пряник")).to_be_visible()

    with allure.step("Нажать на название [Тульский пряник]"):
        card_page.click_title_product_in_list_card("Тульский пряник")
        expect(page).to_have_url("https://pumpenergy.ru/catalog/pryanick-tula")
        expect(page.get_by_role("heading", name="Тульский пряник")).to_be_visible()

@allure.title("Изменение количества в корзине")
@allure.feature("Работа корзины")
@allure.id("11")
def test_11_card_count(page: Page):
    office_page = SectionPage(page, "https://pumpenergy.ru/catalog/office")
    main_page = MainPage(page, "https://pumpenergy.ru/catalog/office")
    card_page = CardPage(page, "https://pumpenergy.ru/catalog/cart")

    with allure.step("Предусловие: Открытие страницы https://pumpenergy.ru/catalog/office"):
        office_page.open()

    with allure.step("Нажать кнопку [Купить] у товара «Карта-флешка»"):
        office_page.click_button_buy_in_product_card_by_title("Карта-флешка")
        expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()


    with allure.step("Нажать кнопку [Купить] у товара «Бумажный пакет»"):
        time.sleep(1)
        office_page.click_button_buy_in_product_card_by_title("Бумажный пакет")
        expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    with allure.step("Нажать на кнопку корзины в верхнем правом меню"):
        main_page.click_to_cart()
        time.sleep(2)
        expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
        expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
        expect(page.get_by_role("link", name="Карта-флешка")).to_be_visible()
        expect(page.get_by_role("link", name="Бумажный пакет")).to_be_visible()
        price_usb = card_page.price_inner("Карта-флешка")
        price_poket = card_page.price_inner("Бумажный пакет")
        count_usb_before = card_page.count_input_value("Карта-флешка")
        count_poket = card_page.count_input_value("Бумажный пакет")
        sum_usb_before = int(price_usb) * int(count_usb_before)
        sum_poket = int(price_poket) * int(count_poket)
        sum_card_before = sum_usb_before + sum_poket
        time.sleep(1)
        expect(page.locator('//*[@class="total-price last-line"]')).to_contain_text(str(sum_card_before))

    with allure.step("Нажать на количество товара «Карта-флешка», исправить на «22»"):
        card_page.fill_count_product_by_title_in_list_card("Карта-флешка", "22")
        page.keyboard.press("Enter")

    with allure.step("Нажать кнопку [Пересчитать]"):
        card_page.click_button_product_by_name("Пересчитать")
        time.sleep(1)
        count_usb_before = card_page.count_input_value("Карта-флешка")
        sum_usb_after = int(price_usb) * int(count_usb_before)
        sum_card_after = sum_usb_after + sum_poket
        cart_total_clean = card_page.inner_clean_cart_total_all_card
        assert cart_total_clean(page) == str(sum_card_after)

    with allure.step("Нажать кнопку [ЛогоПомойки] у товара «Бумажный пакет» "):
        card_page.click_delete_product_by_title_in_list_card("Бумажный пакет")
        expect(page.get_by_role("link", name="Карта-флешка")).to_be_visible()
        expect(page.get_by_role("link", name="Бумажный пакет")).to_be_hidden()
        time.sleep(1)

    with allure.step("Нажать кнопку [Очистить корзину]"):
        card_page.click_button_product_by_name("Очистить корзину")
        expect(page.locator("p", has_text="Корзина пуста")).to_be_visible()
