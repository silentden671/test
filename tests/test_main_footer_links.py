import time

import allure
import pytest_check as check
from locators.locators_main_page import MainPage
from conftest import web_browser

@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки ссылок в футтере главной страницы')
def test_text_main_page(web_browser):
    """Этот тест проверяет работоспособность ссылок в футтере главной страницы"""

    page = MainPage(web_browser)

    page.scroll_down(5500)
    check.equal(page.str_footer_also.get_text(), 'You may also like')
    check.is_true(page.link_footer_first.is_clickable())
    check.is_true(page.link_footer_second.is_clickable())
    check.is_true(page.link_footer_third.is_clickable())
    check.is_true(page.link_footer_fourth.is_clickable())
    check.is_true(page.btn_footer_logo.is_clickable())


    time.sleep(4)
