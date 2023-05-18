import time

from selene import have, be
from selene.support.shared import browser


class HomePage:
    def __init__(self):
        return

    def open_page(self):
        browser.open('https://www.dom-knigi.ru/')
        return self

    def search_book(self, text):
        browser.element('[name="q"]').type(text).press_enter()
        return self

    def check_error_search_book(self):
        browser.element('//*[@id="search-list"]/div[3]/div/div/div/p/font').should(
            have.text('К сожалению, на ваш поисковый запрос ничего не найдено.'))
        return self

    def check_valid_search_book(self):
        browser.element(
            '//*[@id="bx_3966226736_764157_362ce596257894d11ab5c1d73d13c755"]/div/div[3]/div[3]/a/div').should(
            have.text('Толстой Л.Н. Война и мир. Книга 2. Том 3, 4.-М.:АСТ,2021.-736с.-Лучшая мировая классика'))
        return self


    def search_series(self):
        browser.element('//*[@id="header-top-line"]/div[1]/div[2]/div/ul/li[3]/a').click()
        browser.element('//*[@id="bx_3218110189_734475"]/div/a/div/span').click()
        browser.element('//*[@id="bx_1878455859_734475"]/div[1]/h1').should(have.text("#Рецепты Рунета"))
        return self


