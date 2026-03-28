import time

from pages.section_page import SectionPage
from playwright.sync_api import expect, Page


def test_08_count_product_card_mini(page: Page):
    office = SectionPage(page, "https://pumpenergy.ru/catalog/office")
    office.open()

    office.click_button_add_count_input_by_title("Карта-флешка")
    (expect(page.locator('//div[@class="product-item shop2-product-item"][.//a[text()="Карта-флешка"]]//input[@name="amount"]'))
     .to_have_value("2"))

    office.click_button_remove_count_input_by_title("Карта-флешка")
    (expect(page.locator('//div[@class="product-item shop2-product-item"][.//a[text()="Карта-флешка"]]//input[@name="amount"]'))
     .to_have_value("1"))

    office.fill_input_count_by_title("Карта-флешка", "22")
    (expect(page.locator('//div[@class="product-item shop2-product-item"][.//a[text()="Карта-флешка"]]//input[@name="amount"]'))
     .to_have_value("22"))



