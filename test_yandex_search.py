import pytest
from selene import browser, have

@pytest.fixture
def open_yandex(window_browser_settings):
    browser.open('https://www.ya.ru')
    print("\nopen_yandex")


def test_yandex_search_with_result(open_yandex):
    browser.element('[name="text"]').type('qa.guru').press_enter()
    browser.element('[id="search-result"]').should(have.text('Курсы тестировщиков — обучение'))

def test_yandex_search_without_results(open_yandex):
    browser.element('[name="text"]').type('выапролдюбортипмавапо').press_enter()
    browser.element('[class="EmptySearchResults"]').should(have.text('Ничего не нашли'))