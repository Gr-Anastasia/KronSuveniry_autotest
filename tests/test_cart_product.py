from pages.main_page import MainPage
from playwright.sync_api import expect, Page

def test_06_go_to_cart_product(page: Page):
    main = MainPage(page, 'https://pumpenergy.ru/')
    main.open()

    main.click_to_left_menu_by_title("Съедобное")
    expect(page).to_have_url("https://pumpenergy.ru/catalog/eatable")

