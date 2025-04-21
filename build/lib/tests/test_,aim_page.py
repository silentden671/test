import allure
import pytest_check as check
from locators.locators_main_page import MainPage
from conftest import web_browser


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедара')
def test_headers(web_browser):
    """Этот тест проверяет хедер главной страницы"""

    page = MainPage(web_browser)

    page.btn_pip_up_сookie.click()

    elements_headers = [
        (page.btn_headers_domain, 'Домены'),
        (page.btn_headers_hosting, 'Хостинг'),
        (page.btn_headers_cloud, 'Облако'),
        (page.btn_headers_mail, 'Почта')
    ]

    for elements, elements_text in elements_headers:
        with allure.step(f'Проверка "{elements_text}" на отображение'):
            check.is_true(elements.is_visible())

        with allure.step(f'Проверка "{elements_text}" на кликабельность'):
            check.is_true(elements.is_clickable())

        with allure.step(f'Сверка текста"{elements_text}"'):
            check.equal(elements.get_text(), elements_text)


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки текста в блоке main')
def test_text_main_page(web_browser):
    """Этот тест проверяет текст на главной страницы главного блока"""

    page = MainPage(web_browser)

    print(page.btn_headers_logo.get_text())
