import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def setup_browser_desktop():
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture(scope='function')
def setup_browser_tablet():
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = 820
    browser.config.window_height = 1180


@pytest.fixture(scope='function')
def setup_browser_mobile():
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = 375
    browser.config.window_height = 812


@pytest.fixture(params=['desktop', 'tablet', 'mobile'])
def window_size(request):
    return request.param


@pytest.fixture(scope='function')
def setup_browser(window_size):
    browser.config.base_url = 'https://github.com'
    if window_size == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif window_size == 'tablet':
        browser.config.window_width = 820
        browser.config.window_height = 1180
    elif window_size == 'mobile':
        browser.config.window_width = 375
        browser.config.window_height = 812
