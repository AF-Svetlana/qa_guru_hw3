import pytest
from selene import browser, be, have


@pytest.fixture(autouse=True)
def browser_setting():
    browser.open()
    browser.config.base_url = 'https://google.com'
    browser.driver.set_window_size(1920, 1080)
    yield
    browser.quit()


def test_google():
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_negative():
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('######q24234e///').press_enter()
    browser.element('[id="botstuff"]').should(
        have.text('По запросу ######q24234e/// ничего не найдено.'))
