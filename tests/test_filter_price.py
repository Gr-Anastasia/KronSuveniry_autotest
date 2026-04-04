import time

from pages.section_page import SectionPage
from playwright.sync_api import expect, Page

def test_04_filter(page: Page):
    office = SectionPage(page, "https://pumpenergy.ru/catalog/office")
    office.open()
    count_product_before = page.locator(".product-top").count()

    office.fill_filter_price_by_name('от ', '500')
    page.keyboard.press("Enter")
    expect(page.locator('//label[contains(text(), "от ")]/input')).to_have_value('500')
    time.sleep(2)

    office.fill_filter_price_by_name('до ', '2000')
    page.keyboard.press("Enter")
    expect(page.locator('//label[contains(text(), "до ")]/input')).to_have_value('2000')
    time.sleep(2)

    office.click_button_filter_by_name('Показать')
    time.sleep(2)

    count_product_after = page.locator(".product-top").count()
    expect(page.locator('//*[@class="shop2-filter"]/span[@class="filter-result "]')).to_be_visible()
    expect(page.locator("#filter-result")).to_have_text(f"{count_product_after}")

    office.click_button_filter_by_name('Сбросить фильтр')
    expect(page.locator(".product-top")).to_have_count(count_product_before)

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
