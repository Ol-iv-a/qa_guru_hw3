import pytest
from selene import browser

@pytest.fixture
def window_browser_settings():
    browser.config.window_width = 800
    browser.config.window_height = 600
    print("\nwindow_browser_settings: 800x600")

    yield

    browser.quit()
    print("\nbrowser_closed")
