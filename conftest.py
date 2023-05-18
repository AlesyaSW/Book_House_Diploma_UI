import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def preparations():
    browser.config.hold_browser_open = True
    browser.config.window_width = 1150
    browser.config.window_height = 796

