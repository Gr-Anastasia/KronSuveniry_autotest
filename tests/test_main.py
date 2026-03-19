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
