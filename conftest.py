import pytest
from selene.support.shared import browser
from book.utils import attach


@pytest.fixture(scope="session")
def preparations():
    browser.config.hold_browser_open = True
    browser.config.window_width = 1150
    browser.config.window_height = 796

    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    # attach.add_video(browser)
