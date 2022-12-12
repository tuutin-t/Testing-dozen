from playwright.sync_api import Page
def test_maanantai(page: Page):
    page.goto("https://google.com")