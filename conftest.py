import pytest
from selene.support.shared import browser
from book.utils import attach
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def driver_managment_remote():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.window_width = 1200
    browser.config.window_height = 800

    yield browser
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
