import time

import allure
import pytest_check as check
from locators.locators_main_page import MainPage
from conftest import web_browser

@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки отправки подписки')
def test_text_main_page(web_browser):
    """Этот тест проверяет отправку подписки"""

    page = MainPage(web_browser)

    check.equal(page.name_body_mac.get_text(), "Big Mac")
    check.equal(page.cost_body_mac.get_text(), "$2")

    time.sleep(3)