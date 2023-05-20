from selene.support.shared import browser
from selene import have


class SeriesPage:

    def open_series(self):
        browser.element('//a[contains(@class, "navigation-link") and contains(text(), "Серии")]').click()
        return self

    def selection_specific_series(self):
        browser.element('//span[contains(@class, "brand_item_text") and contains(text(), "#Рецепты Рунета")]').click()
        return self

    def check_valid_series(self):
        browser.element('//h1[contains(@class, "brand_name")]').should(have.text("#Рецепты Рунета"))
        return self
