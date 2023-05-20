from selene.support.shared import browser
from selene import be


class LoginPage:

    def click_login(self):
        browser.element('//span[contains(text(),"Войти") and contains(@class,"icon-txt")]').click()
        return self

    def login_by_email(self):
        browser.element('//input[contains(@name,"LOGIN")]').click()
        browser.element('//input[contains(@name,"LOGIN")]').type('qwer@.wew')
        return self

    def enter_password(self):
        browser.element('//input[contains(@name,"PASSWORD")]').type('Qwe')
        browser.element('//input[contains(@name,"PASSWORD")]').type('Qwer')
        return self

    def button_login(self):
        browser.element('//input[contains(@name,"Login")]').press_enter()
        return self

    def check_error_auth_email(self):
        browser.element("//div[contains(text(), 'Неверный логин или пароль.')]").should(
            be.visible)
        return self
