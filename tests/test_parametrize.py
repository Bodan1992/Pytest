"""
Переопределите параметр с помощью indirect
"""
from github_test.controls.utils import *
from github_test.controls.elements import *
from tests.confest import *


@pytest.mark.parametrize('window_size', ['desktop'], indirect=True)
def test_github_desktop(setup_browser):
    opened_page_url("https://github.com")
    desktop_site()


@pytest.mark.parametrize('window_size', ['tablet', 'mobile'], indirect=True)
def test_mobile_or_tablet_site(setup_browser):
    opened_page_url("https://github.com")
    mobile_or_tablet_site()
