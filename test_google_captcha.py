import pytest
from selene import browser, have

@pytest.fixture
def open_google(window_browser_settings):
    browser.open('https://www.google.com')
    print("\nopen_google")

def test_google_captcha_should_be_shown(open_google):
    browser.element('[name="q"]').type('qa.guru').press_enter()
    browser.element('html').should(have.text('Об этой странице'))

def test_google_captcha_should_be_shown_fail(open_google):
    browser.element('[name="q"]').type('qa.guru').press_enter()
    browser.element('html').should(have.text('About this page'))
