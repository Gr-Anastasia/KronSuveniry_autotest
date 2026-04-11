import allure
from playwright.sync_api import expect, Page

from pages.section_page import SectionPage


@allure.title("Ввод количества в карточке товара ")
@allure.feature("Работа + и - количества в карточке товара")
@allure.id("08")
def test_08_count_product_card_mini(page: Page):
    office_page = SectionPage(page, "https://pumpenergy.ru/catalog/office")

    with allure.step("Предусловие: Открытие страницы https://pumpenergy.ru/catalog/office"):
        office_page.open()

    with allure.step("Нажать кнопку [+] в количестве у товара «Карта-флешка»"):
        office_page.click_button_add_count_input_by_title("Карта-флешка")
        expect(page.locator('.product-item.shop2-product-item:has(a:has-text("Карта-флешка"))')
               .locator('input[name="amount"]')).to_have_value("2")

    with allure.step("Нажать кнопку [-] в количестве у товара «Карта-флешка»"):
        office_page.click_button_remove_count_input_by_title("Карта-флешка")
        expect(page.locator('.product-item.shop2-product-item:has(a:has-text("Карта-флешка"))')
               .locator('input[name="amount"]')).to_have_value("1")

    with allure.step("Нажать на инпут количества у товара «Карта-флешка», написать «22»"):
        office_page.fill_input_count_by_title("Карта-флешка", "22")
        expect(page.locator('.product-item.shop2-product-item:has(a:has-text("Карта-флешка"))')
               .locator('input[name="amount"]')).to_have_value("22")
