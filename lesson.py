import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationexercise.com/")
    page.get_by_label("Consent", exact=True).click()
    page.get_by_role("link", name=" Signup / Login").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("robert")
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill("robert123")
    page.get_by_role("button", name="Signup").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
