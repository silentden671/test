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

    page.scroll_down(5500)
    page.inp_footer_email.send_keys('dididada@gmail.com')
    time.sleep(1)
    page.btn_footer_subscribe.click()
    check.equal(page.str_footer_thx.get_text(), 'Thanks for subscribing :)')


    time.sleep(4)