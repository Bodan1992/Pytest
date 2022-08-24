from selene import have
from selene.support.shared import browser


def desktop_site():
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.exact_text("Sign in to GitHub"))


def mobile_or_tablet_site():
    browser.element(".octicon.octicon-three-bars").click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.exact_text("Sign in to GitHub"))