import time

from pages.main_page import MainPage
from playwright.sync_api import expect, Page

def test_01(page: Page):
    page.goto("https://pumpenergy.ru/")
    expect(page.locator(".company-name__inner")).to_have_text('НК «Крон»')
    expect(page.locator(".company-desc")).to_have_text('Сувениры')
    expect(page.locator("[data-folder-name=' Для офиса ']")).to_be_visible()
    expect(page.locator("[data-folder-name=' Съедобные ']")).to_be_visible()
    expect(page.locator("[data-folder-name=' USB-накопители ']")).to_be_visible()
    expect(page.locator("[data-folder-name='Литература']")).to_be_visible()

def test_02(page: Page):
    main = MainPage(page, 'https://pumpenergy.ru/')
    main.open()

    main.click_to_menu_up_by_title("Каталог сувениров")
    expect(page).to_have_url("https://pumpenergy.ru/catalog")
    expect(page.get_by_role("heading", name="Каталог сувениров")).to_be_visible()

    main.click_to_menu_up_by_title("Обратная связь")
    expect(page).to_have_url("https://pumpenergy.ru/obratnay_svayz")
    expect(page.get_by_role("heading", name="Обратная связь")).to_be_visible()

    main.click_to_menu_up_by_title("Личный кабинет")
    expect(page).to_have_url("https://pumpenergy.ru/registraciya")
    expect(page.get_by_role("heading", name="Доступ запрещен")).to_be_visible()

    main.click_to_menu_by_home()
    expect(page).to_have_url("https://pumpenergy.ru/")