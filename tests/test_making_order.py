import time
import allure
from playwright.sync_api import expect, Page

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.card_page import CardPage
from pages.product_page import ProductPage
from pages.section_page import SectionPage


@allure.title("Оформление заказа")
@allure.feature("Оформление заказа")
@allure.id("12")
def test_12_making_an_order(page: Page):
    poster_page = SectionPage(page, "https://pumpenergy.ru/catalog/literature")
    main_page = MainPage(page, "https://pumpenergy.ru/catalog/office")
    card_page= CardPage(page, "https://pumpenergy.ru/catalog/cart")
    order_page = OrderPage(page, "https://pumpenergy.ru/catalog?mode=order")

    with allure.step("Предусловие: Перейти по ссылке https://pumpenergy.ru/catalog/literature"):
        poster_page.open()

    with allure.step("Нажать кнопку [Купить] у товара «Брошюра А4 МНХИ»"):
        poster_page.click_button_buy_in_product_card_by_title("Брошюра А4 МНХИ")
        expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    with allure.step("Нажать на кнопку корзины в верхнем правом меню"):
        main_page.click_to_cart()

        price = page.locator("#cart-row-725769909 > .shop2-cart-price").all()[1].inner_text()
        count = page.locator('input[name="amounts[725769909]"]').input_value()
        sum_card = int(price) * int(count)

        expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
        expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
        expect(page.get_by_role("link", name="Брошюра А4 МНХИ")).to_be_visible()
        expect(page.locator('//*[@class="total-price last-line"]')).to_contain_text(f"{str(sum_card)} Крон")

    with allure.step("Нажать кнопку [Купить без регистрации]"):
        card_page.click_button_buy_no_register()
        expect(page).to_have_url("https://pumpenergy.ru/catalog?mode=order")
        expect(page.get_by_role("heading", name="Доставка")).to_be_visible()

    with allure.step("Нажать [Самовывоз – бесплатно]"):
        order_page.click_radiobutton_product_by_delivery("Самовывоз - бесплатно")
        expect(page.get_by_label("Самовывоз - бесплатно")).to_be_checked()

    with allure.step("Нажать [Оформить заказ]"):
        order_page.click_button_making_order_in_delivery()
        expect(page.get_by_role("heading", name="Оформление заказа")).to_be_visible()
        expect(page.get_by_label("ФИО")).to_be_visible()
        expect(page.get_by_label("Компания")).to_be_visible()
        expect(page.get_by_label("Телефон")).to_be_visible()
        expect(page.get_by_label("E-mail")).to_be_visible()
        expect(page.get_by_label("Дополнительная информация")).to_be_visible()

    with allure.step("Заполнить все поля тестовыми данными"):
        order_page.fill_input_form_add_data("ФИО", "Арбузов Иван Петрович")
        order_page.fill_input_form_add_data("Компания", "Технотекст")
        order_page.fill_input_form_add_data("Телефон", "88005553535")
        order_page.fill_input_form_add_data("E-mail", "qa@mail.com")
        expect(page.get_by_label("ФИО")).to_have_value("Арбузов Иван Петрович")
        expect(page.get_by_label("Компания")).to_have_value("Технотекст")
        expect(page.get_by_label("Телефон")).to_have_value("88005553535")
        expect(page.get_by_label("E-mail")).to_have_value("qa@mail.com")

@allure.title("Ввод не всех данных при оформлении заказа ")
@allure.feature("Оформление заказа")
@allure.id("13")
def test_13_making_an_order_not_all_data(page: Page):
    poster_page = SectionPage(page, "https://pumpenergy.ru/catalog/literature")
    main_page = MainPage(page, "https://pumpenergy.ru/catalog/office")
    card_page= CardPage(page, "https://pumpenergy.ru/catalog/cart")
    order_page = OrderPage(page, "https://pumpenergy.ru/catalog?mode=order")

    with allure.step("Предусловие: Перейти по ссылке https://pumpenergy.ru/catalog/literature"):
        poster_page.open()

    with allure.step("Нажать кнопку [Купить] у товара «Брошюра А4 МНХИ»"):
        poster_page.click_button_buy_in_product_card_by_title("Брошюра А4 МНХИ")
        expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    with allure.step("Нажать на кнопку корзины в верхнем правом меню"):
        main_page.click_to_cart()

        price = page.locator("#cart-row-725769909 > .shop2-cart-price").all()[1].inner_text()
        count = page.locator('input[name="amounts[725769909]"]').input_value()
        sum_card = int(price) * int(count)

        expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
        expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
        expect(page.get_by_role("link", name="Брошюра А4 МНХИ")).to_be_visible()
        expect(page.locator('//*[@class="total-price last-line"]')).to_contain_text(f"{str(sum_card)} Крон")

    with allure.step("Нажать кнопку [Купить без регистрации]"):
        card_page.click_button_buy_no_register()
        expect(page).to_have_url("https://pumpenergy.ru/catalog?mode=order")
        expect(page.get_by_role("heading", name="Доставка")).to_be_visible()

    with allure.step("Нажать [Самовывоз – бесплатно]"):
        order_page.click_radiobutton_product_by_delivery("Самовывоз - бесплатно")
        expect(page.get_by_label("Самовывоз - бесплатно")).to_be_checked()

    with allure.step("Нажать [Оформить заказ]"):
        order_page.click_button_making_order_in_delivery()
        expect(page.get_by_role("heading", name="Оформление заказа")).to_be_visible()
        expect(page.get_by_label("ФИО")).to_be_visible()
        expect(page.get_by_label("Компания")).to_be_visible()
        expect(page.get_by_label("Телефон")).to_be_visible()
        expect(page.get_by_label("E-mail")).to_be_visible()
        expect(page.get_by_label("Дополнительная информация")).to_be_visible()

    with allure.step("Заполнить поля [Компания] и [E-mail] данными."):
        order_page.fill_input_form_add_data("Компания", "Технотекст")
        order_page.fill_input_form_add_data("E-mail", "qa@mail.com")
        expect(page.get_by_label("Компания")).to_have_value("Технотекст")
        expect(page.get_by_label("E-mail")).to_have_value("qa@mail.com")

    with allure.step("Нажать [Оформить заказ]"):
        order_page.click_button_making_order_in_making_order()
        expect(page.locator(".error")).to_contain_text("ФИО: это поле обязательно для заполнения! Телефон: это поле обязательно для заполнения. Неверный формат телефона!")

@allure.title("Проверка оформления заказа доставкой Курьером ")
@allure.feature("Оформление заказа")
@allure.id("14")
def test_14_making_an_order_courier(page: Page):
    pie_page = ProductPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")
    main_page = MainPage(page, "https://pumpenergy.ru/catalog/office")
    card_page = CardPage(page, "https://pumpenergy.ru/catalog/cart")
    order_page = OrderPage(page, "https://pumpenergy.ru/catalog?mode=order")

    with allure.step("Предусловие: Перейти по ссылке https://pumpenergy.ru/catalog/pryanick-tula"):
        pie_page.open()

    with allure.step("Нажать кнопку [Купить] "):
        pie_page.click_button_product_by_name("Купить")
        expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    with allure.step("Нажать на кнопку корзины в верхнем правом меню"):
        main_page.click_to_cart()
        price = page.locator("#cart-row-925418108 > .shop2-cart-price").all()[1].inner_text()
        count = page.locator('input[name="amounts[925418108]"]').input_value()
        sum_card = int(price) * int(count)
        expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
        expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
        expect(page.get_by_role("link", name="Тульский пряник")).to_be_visible()
        expect(page.locator('//*[@class="total-price last-line"]')).to_contain_text(f"{str(sum_card)} Крон")

    with allure.step("Нажать кнопку [Купить без регистрации]"):
        card_page.click_button_buy_no_register()
        expect(page).to_have_url("https://pumpenergy.ru/catalog?mode=order")
        expect(page.get_by_role("heading", name="Доставка")).to_be_visible()

    with allure.step("Нажать [Курьер - бесплатно]"):
        order_page.click_radiobutton_product_by_delivery("Курьер - бесплатно")
        expect(page.get_by_label("Курьер - бесплатно")).to_be_checked()
        time.sleep(2)
        expect(page.get_by_label("Адрес доставки:")).to_be_visible()
        expect(page.locator(".delivery-type.delivery-type-current label:has(span:has-text('Телефон:'))")).to_be_visible()
        expect(page.locator(".delivery-type.delivery-type-current label:has(span:has-text('Дата и время доставки:'))")).to_be_visible()

    with allure.step("Заполнить поля тестовыми данными"):
        order_page.fill_input_form_add_data_by_courier("Адрес доставки:", "г. Москва, ул. Максима Рыльского, д.1.")
        order_page.fill_input_form_add_data_by_courier("Телефон:", "880055353555")
        order_page.fill_input_form_add_data_by_courier("Дата и время доставки:", "11.03.2026, 15:00")
        expect(page.locator("#delivery-0").all()[0]).to_have_value("г. Москва, ул. Максима Рыльского, д.1.")
        expect(page.locator("#delivery-1").all()[0]).to_have_value("880055353555")
        expect(page.locator("#delivery-2").all()[0]).to_have_value("11.03.2026, 15:00")

    with allure.step("Нажать [Оформить заказ]"):
        order_page.click_button_making_order_in_delivery()
        expect(page.get_by_role("heading", name="Оформление заказа")).to_be_visible()
        expect(page.get_by_label("ФИО")).to_be_visible()
        expect(page.get_by_label("Компания")).to_be_visible()
        expect(page.get_by_label("Телефон")).to_be_visible()
        expect(page.get_by_label("E-mail")).to_be_visible()
        expect(page.get_by_label("Дополнительная информация")).to_be_visible()

@allure.title("Проверка оформления заказа доставкой Почтой-России ")
@allure.feature("Оформление заказа")
@allure.id("15")
def test_15_making_an_order_post(page: Page):
    pie_page = ProductPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")
    main_page = MainPage(page, "https://pumpenergy.ru/catalog/office")
    card_page = CardPage(page, "https://pumpenergy.ru/catalog/cart")
    order_page = OrderPage(page, "https://pumpenergy.ru/catalog?mode=order")

    with allure.step("Предусловие: Перейти по ссылке https://pumpenergy.ru/catalog/pryanick-tula"):
        pie_page.open()

    with allure.step("Нажать кнопку [Купить] "):
        pie_page.click_button_product_by_name("Купить")
        expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    with allure.step("Нажать на кнопку корзины в верхнем правом меню"):
        main_page.click_to_cart()
        price = page.locator("#cart-row-925418108 > .shop2-cart-price").all()[1].inner_text()
        count = page.locator('input[name="amounts[925418108]"]').input_value()
        sum_card = int(price) * int(count)
        expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
        expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
        expect(page.get_by_role("link", name="Тульский пряник")).to_be_visible()
        expect(page.locator('//*[@class="total-price last-line"]')).to_contain_text(f"{str(sum_card)} Крон")

    with allure.step("Нажать кнопку [Купить без регистрации]"):
        card_page.click_button_buy_no_register()
        expect(page).to_have_url("https://pumpenergy.ru/catalog?mode=order")
        expect(page.get_by_role("heading", name="Доставка")).to_be_visible()

    with allure.step("Нажать [Почта России - бесплатно]"):
        order_page.click_radiobutton_product_by_delivery("Почта России - бесплатно")
        expect(page.get_by_label("Почта России - бесплатно")).to_be_checked()
        time.sleep(2)
        expect(page.locator("#delivery-detail-7435909 label:has(span:has-text('Адрес доставки:'))")).to_be_visible()
        expect(page.locator("#delivery-detail-7435909 label:has(span:has-text('Почтовый индекс:'))")).to_be_visible()
        expect(page.locator("#delivery-detail-7435909 label:has(span:has-text('Телефон:'))")).to_be_visible()

    with allure.step("Заполнить поля тестовыми данными"):
        order_page.fill_input_form_add_data_by_post("Адрес доставки:", "г. Москва, ул. Максима Рыльского, д.1.")
        order_page.fill_input_form_add_data_by_post("Почтовый индекс:", "000555")
        order_page.fill_input_form_add_data_by_post("Телефон:", "880055353555")
        expect(page.locator("#delivery-0").all()[1]).to_have_value("г. Москва, ул. Максима Рыльского, д.1.")
        expect(page.locator("#delivery-1").all()[1]).to_have_value("000555")
        expect(page.locator("#delivery-2").all()[1]).to_have_value("880055353555")

    with allure.step("Нажать [Оформить заказ]"):
        order_page.click_button_making_order_in_delivery()
        expect(page.get_by_role("heading", name="Оформление заказа")).to_be_visible()
        expect(page.get_by_label("ФИО")).to_be_visible()
        expect(page.get_by_label("Компания")).to_be_visible()
        expect(page.get_by_label("Телефон")).to_be_visible()
        expect(page.get_by_label("E-mail")).to_be_visible()
        expect(page.get_by_label("Дополнительная информация")).to_be_visible()

@allure.title("Проверка оформления заказа доставкой Курьером, игнорируя обязательные поля")
@allure.feature("Оформление заказа")
@allure.id("16")
def test_16_making_an_order_courier_not_all_data(page: Page):
    pie_page = ProductPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")
    main_page = MainPage(page, "https://pumpenergy.ru/catalog/office")
    card_page = CardPage(page, "https://pumpenergy.ru/catalog/cart")
    order_page = OrderPage(page, "https://pumpenergy.ru/catalog?mode=order")

    with allure.step("Предусловие: Перейти по ссылке https://pumpenergy.ru/catalog/pryanick-tula"):
        pie_page.open()

    with allure.step("Нажать кнопку [Купить] "):
        pie_page.click_button_product_by_name("Купить")
        expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    with allure.step("Нажать на кнопку корзины в верхнем правом меню"):
        main_page.click_to_cart()
        price = page.locator("#cart-row-925418108 > .shop2-cart-price").all()[1].inner_text()
        count = page.locator('input[name="amounts[925418108]"]').input_value()
        sum_card = int(price) * int(count)
        expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
        expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
        expect(page.get_by_role("link", name="Тульский пряник")).to_be_visible()
        expect(page.locator('//*[@class="total-price last-line"]')).to_contain_text(f"{str(sum_card)} Крон")

    with allure.step("Нажать кнопку [Купить без регистрации]"):
        card_page.click_button_buy_no_register()
        expect(page).to_have_url("https://pumpenergy.ru/catalog?mode=order")
        expect(page.get_by_role("heading", name="Доставка")).to_be_visible()

    with allure.step("Нажать [Курьер - бесплатно]"):
        order_page.click_radiobutton_product_by_delivery("Курьер - бесплатно")
        expect(page.get_by_label("Курьер - бесплатно")).to_be_checked()
        time.sleep(2)
        expect(page.get_by_label("Адрес доставки:")).to_be_visible()
        expect(page.locator(".delivery-type.delivery-type-current label:has(span:has-text('Телефон:'))")).to_be_visible()
        expect(page.locator(".delivery-type.delivery-type-current label:has(span:has-text('Дата и время доставки:'))")).to_be_visible()

    with allure.step("Заполнить поля тестовыми данными, КРОМЕ АДРЕСА ДОСТАВКИ"):
        order_page.fill_input_form_add_data_by_courier("Телефон:", "880055888555")
        order_page.fill_input_form_add_data_by_courier("Дата и время доставки:", "12.03.2027, 15:00")
        expect(page.locator("#delivery-1").all()[0]).to_have_value("880055888555")
        expect(page.locator("#delivery-2").all()[0]).to_have_value("12.03.2027, 15:00")

    with allure.step("Нажать [Оформить заказ]"):
        order_page.click_button_making_order_in_delivery()
        expect(page.locator(".error")).to_have_text("Неверно заполнено поле: Адрес доставки")

@allure.title("Проверка оформления заказа доставкой Почтой-России, игнорируя обязательные поля ")
@allure.feature("Оформление заказа")
@allure.id("17")
def test_17_making_an_order_post_not_all_data(page: Page):
    pie_page = ProductPage(page, "https://pumpenergy.ru/catalog/pryanick-tula")
    main_page = MainPage(page, "https://pumpenergy.ru/catalog/office")
    card_page = CardPage(page, "https://pumpenergy.ru/catalog/cart")
    order_page = OrderPage(page, "https://pumpenergy.ru/catalog?mode=order")

    with allure.step("Предусловие: Перейти по ссылке https://pumpenergy.ru/catalog/pryanick-tula"):
        pie_page.open()

    with allure.step("Нажать кнопку [Купить] "):
        pie_page.click_button_product_by_name("Купить")
        expect(page.locator(".added-to-cart:has-text('Добавлено')")).to_be_visible()

    with allure.step("Нажать на кнопку корзины в верхнем правом меню"):
        main_page.click_to_cart()
        price = page.locator("#cart-row-925418108 > .shop2-cart-price").all()[1].inner_text()
        count = page.locator('input[name="amounts[925418108]"]').input_value()
        sum_card = int(price) * int(count)
        expect(page).to_have_url("https://pumpenergy.ru/catalog/cart")
        expect(page.get_by_role("heading", name="Корзина")).to_be_visible()
        expect(page.get_by_role("link", name="Тульский пряник")).to_be_visible()
        expect(page.locator('//*[@class="total-price last-line"]')).to_contain_text(f"{str(sum_card)} Крон")

    with allure.step("Нажать кнопку [Купить без регистрации]"):
        card_page.click_button_buy_no_register()
        expect(page).to_have_url("https://pumpenergy.ru/catalog?mode=order")
        expect(page.get_by_role("heading", name="Доставка")).to_be_visible()

    with allure.step("Нажать [Почта России - бесплатно]"):
        order_page.click_radiobutton_product_by_delivery("Почта России - бесплатно")
        expect(page.get_by_label("Почта России - бесплатно")).to_be_checked()
        time.sleep(2)
        expect(page.locator("#delivery-detail-7435909 label:has(span:has-text('Адрес доставки:'))")).to_be_visible()
        expect(page.locator("#delivery-detail-7435909 label:has(span:has-text('Почтовый индекс:'))")).to_be_visible()
        expect(page.locator("#delivery-detail-7435909 label:has(span:has-text('Телефон:'))")).to_be_visible()

    with allure.step("Заполнить поля тестовыми данными, КРОМЕ ИНДЕКСА"):
        order_page.fill_input_form_add_data_by_post("Адрес доставки:", "г. Москва, ул. Максима Рыльского, д.1.")
        order_page.fill_input_form_add_data_by_post("Телефон:", "880055353555")
        expect(page.locator("#delivery-0").all()[1]).to_have_value("г. Москва, ул. Максима Рыльского, д.1.")
        expect(page.locator("#delivery-2").all()[1]).to_have_value("880055353555")

    with allure.step("Нажать [Оформить заказ]"):
        order_page.click_button_making_order_in_delivery()
        expect(page.locator(".error")).to_have_text("Неверно заполнено поле: Почтовый индекс")
