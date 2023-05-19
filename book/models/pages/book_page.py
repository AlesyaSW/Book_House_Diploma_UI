from book.models.pages.home_page import HomePage
from selene.support.shared import browser
from selene import be


class BookPage(HomePage):
    def __int__(self):
        return self

    def open_book(self):
        browser.element('//img[contains(@class, "product_item_img-bg")]').click()
        return self

    def add_in_basket(self):
        browser.element('//div[contains(@class, "main-button-container")]').click()
        return self

    def quantity_on_page(self):
        browser.element('//input[contains(@class, "product-item-amount-field")]').should(be.visible)
        return self