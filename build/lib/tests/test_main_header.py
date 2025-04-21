import allure
import time
import pytest_check as check
from locators.locators_main_page import MainPage
from conftest import web_browser


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)

    check.is_true(page.btn_headers_logo.is_clickable())
    check.equal(page.txt_headers_title.get_text(), "Spend Bill Gates' Money")
    check.equal(page.txt_headers_money.get_text(), "$100,000,000,000")

    time.sleep(4)