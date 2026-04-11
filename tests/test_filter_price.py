import time
import allure
from playwright.sync_api import expect, Page

from pages.section_page import SectionPage

@allure.title("Работа фильтра «Цена»")
@allure.feature("Фильтр цена на страницах раздела")
@allure.id("04")
def test_04_filter(page: Page):
    office_page = SectionPage(page, "https://pumpenergy.ru/catalog/office")

    with allure.step("Предусловие: Открытие страницы https://pumpenergy.ru/catalog/office"):
        office_page.open()
        count_product_before = page.locator(".product-top").count()

    with allure.step("Ввести в фильтре «Цена» в графе «От» -[500]  "):
        office_page.fill_filter_price_by_name('от ', '500')
        page.keyboard.press("Enter")
        expect(page.locator('//label[contains(text(), "от ")]/input')).to_have_value('500')
        time.sleep(2)

    with allure.step("Ввести в фильтре «Цена» в графе «До» - [2000]  "):
        office_page.fill_filter_price_by_name('до ', '2000')
        page.keyboard.press("Enter")
        expect(page.locator('//label[contains(text(), "до ")]/input')).to_have_value('2000')
        time.sleep(2)

    with allure.step("Нажать кнопку [Показать]  "):
        office_page.click_button_filter_by_name('Показать')
        time.sleep(2)
        count_product_after = page.locator(".product-top").count()
        expect(page.locator('//*[@class="shop2-filter"]/span[@class="filter-result "]')).to_be_visible()
        expect(page.locator("#filter-result")).to_have_text(f"{count_product_after}")

    with allure.step("Нажать кнопку [Сбросить фильтр]  "):
        office_page.click_button_filter_by_name('Сбросить фильтр')
        expect(page.locator(".product-top")).to_have_count(count_product_before)

@allure.title("Валидация полей фильтра «Цена»")
@allure.feature("Фильтр цена на страницах раздела")
@allure.id("05")
def test_05_filter(page: Page):
    office_page = SectionPage(page, "https://pumpenergy.ru/catalog/office")

    with allure.step("Предусловие: Открытие страницы https://pumpenergy.ru/catalog/office"):
        office_page.open()

    with allure.step("Ввести в фильтре «Цена» в графе «От» -[1234567891011121314151617181920]  "):
        office_page.fill_filter_price_by_name('от ', '1234567891011121314151617181920')
        page.keyboard.press("Enter")
        expect(page.locator('//label[contains(text(), "от ")]/input')).to_have_count(7)

    with allure.step("Ввести в фильтре «Цена» в графе «До» - [HelloWord!, Привет всем!]  "):
        time.sleep(2)
        office_page.fill_filter_price_by_name('до ', 'HelloWord!, Привет всем')
        page.keyboard.press("Enter")
        expect(page.locator('//label[contains(text(), "до ")]/input')).to_have_count(0)
        time.sleep(2)

    with allure.step("Нажать кнопку [Показать]  "):
        office_page.click_button_filter_by_name('Показать')
        count_product = page.locator(".product-top").count()
        expect(page.locator('//*[@class="shop2-filter"]/span[@class="filter-result "]')).to_be_visible()
        expect(page.locator("#filter-result")).to_have_text(f"{count_product}")
