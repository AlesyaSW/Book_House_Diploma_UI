from book.models.pages.home_page import HomePage
from selene.support.shared import browser


class BasketPage(HomePage):

    def __int__(self):
        return self

    def open_basket(self):
        browser.element('//span[contains(@class, "icon-item basket-icon")]').click()
        return self

    def enter_promocode(self, text):
        browser.element(
            '//input[contains(@class, "form-control") and contains(@data-entity,"basket-coupon-input")]').click()
        browser.element(
            '//input[contains(@class, "form-control") and contains(@data-entity,"basket-coupon-input")]').type(text)

        return self

    def apply_button(self):
        browser.element('//span[contains(@class, "basket-coupon-block-coupon-btn btn-primary")]').click()
        return self

    def check_error_promocode(self):
        browser.element('//span[contains(@class, "basket-coupon-text")]')
        return self
