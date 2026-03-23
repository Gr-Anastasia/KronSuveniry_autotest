import time

from pages.section_page import SectionPage
from playwright.sync_api import expect, Page

def test_04_filter(page: Page):
    """
        НЕ РАБОТАЕТ! ОШИБКА БД, ПРАВИТЬ!
    """

    office = SectionPage(page, "https://pumpenergy.ru/catalog/office")
    office.open()

    # office.click_button_by_name('Сбросить фильтр')
    office.fill_filter_price_by_name('от ', '500')
    expect(page.locator('//label[contains(text(), "от ")]/input')).to_have_value('500')
    time.sleep(10)


    office.fill_filter_price_by_name('до ', '2000')
    expect(page.locator('//label[contains(text(), "до ")]/input')).to_have_value('2000')
    time.sleep(10)
    office.click_button_filter_by_name('Показать')
    time.sleep(10)
    # count_product = page.locator(".product-top").count()
    # expect(page.locator(".filter-result")).to_be_visible()
    # expect(page.locator("#filter-result")).to_have_text(f"{count_product}")
    # expect(page.locator(".product-top")).to_have_count("5")

    # office.click_button_by_name('Сбросить фильтр')
    # time.sleep(2)


def test_05_filter(page: Page):
    """
        НЕ РАБОТАЕТ! ОШИБКА БД, ПРАВИТЬ!
    """

    office = SectionPage(page, "https://pumpenergy.ru/catalog/office")
    office.open()

    # office.click_button_by_name('Сбросить фильтр')
    office.fill_filter_price_by_name('от ', '1234567891011121314151617181920')
    expect(page.locator('//label[contains(text(), "от ")]/input')).to_have_count(7)
    time.sleep(10)

    office.fill_filter_price_by_name('до ', 'HelloWord!, Привет всем')
    expect(page.locator('//label[contains(text(), "до ")]/input')).to_have_count(0)
    time.sleep(10)
    office.click_button_filter_by_name('Показать')
    time.sleep(10)
