import time

from pages.section_page import SectionPage
from playwright.sync_api import expect, Page

def test_06_go_to_cart_product(page: Page):
    food = SectionPage(page, "https://pumpenergy.ru/catalog/eatable")
    food.open()

    food.click_product_in_card_by_title("Тульский пряник")
    time.sleep(2)

