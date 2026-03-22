import time

from pages.section_page import SectionPage
from playwright.sync_api import expect, Page

def test_06_go_to_cart_product(page: Page):
    food = SectionPage(page, "https://pumpenergy.ru/catalog/eatable")
    food.open()

    food.click_product_in_card_by_title("Тульский пряник")
    expect(page).to_have_url("https://pumpenergy.ru/catalog/pryanick-tula")
    expect(page.get_by_role("heading", name="Тульский пряник")).to_be_visible()
    expect(page.locator(".price-current > strong")).to_have_text("700")
