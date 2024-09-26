from pages.login_page import LoginPage


def test_login(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Инициализируем объект страницы
    login_page = LoginPage(page)

    # Действия на странице
    login_page.navigate()
    login_page.accept_cookies()
    login_page.enter_username("robert")
    login_page.enter_password("123robert123@mail.com")
    login_page.click_login()

    # Добавляем проверки (assert)
    assert page.url == "https://automationexercise.com/signup"

    browser.close()
