"""
Сделайте разные фикстуры для каждого теста
"""
from tests.confest import *
from github_test.controls.utils import *
from github_test.controls.elements import *


def test_github_desktop(setup_browser_desktop):
    opened_page_url("https://github.com")
    desktop_site()


def test_github_mobile_or_tablet(setup_browser_mobile, setup_browser_tablet):
    opened_page_url("https://github.com")
    mobile_or_tablet_site()

