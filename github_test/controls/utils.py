import pytest
from selene import have
from selene.support.shared import browser


def check_browser_window_size():
    if browser.config.window_width < 1012:
        pytest.skip('The screen width is not desktop size.')


def opened_page_url(url: str):
    browser.open(url)



