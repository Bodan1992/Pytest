"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
from github_test.controls.elements import *
from github_test.controls.utils import *
from tests.confest import *


def test_github_sign_in_button(setup_browser):
    check_browser_window_size()
    opened_page_url("https://github.com")
    desktop_site()
