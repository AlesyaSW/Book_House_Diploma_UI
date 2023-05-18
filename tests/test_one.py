import allure
from allure_commons.types import Severity
from book.models import app
from book.models.data import data_home_page


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Pimenova")
@allure.feature(f'Проверка авторизации с невалидными данными')
@allure.story("Проверка отображния ошибки при вводе email и пароля, который отсутствует в системе")
@allure.link("https://www.dom-knigi.ru/", name="Testing")
def test_auth_with_not_email(preparations):
    with allure.step("Открываем главную страницу 'Дом книги'"):
        app.home_page.open_page()
    with allure.step('Открываем форму авторизации и вводим невалидный логин и пароль'):
        app.login_page. \
            click_login(). \
            login_by_email(). \
            enter_password(). \
            button()
    with allure.step('Проверяем появление ошибки'):
        app.login_page.check_error_auth_email()


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Pimenova')
@allure.description('Проверка поиска')
@allure.feature('Проверка поиска отсутствующей книги')
@allure.link('https://www.dom-knigi.ru/')
def test_error_search_product():
    with allure.step('Открываем главную страницу ЧетыреЛапы'):
        app.home_page.open_page()
        app.home_page.search_book(data_home_page.not_valid_name_product)
    with allure.step('Проверяем получение пустого поиска'):
        app.home_page.check_error_search_book()


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Pimenova')
@allure.description('Проверка поиска книг')
@allure.feature('Проверка поиска существующей книги')
@allure.link('https://www.dom-knigi.ru/')
def test_valid_search_book():
    with allure.step('Открываем главную страницу и вводим в строку поска наименование книги'):
        app.home_page.open_page(). \
            search_book(data_home_page.valid_name_book)
    with allure.step('Проверяем результат поиска'):
        app.home_page.check_valid_search_book()


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Pimenova')
@allure.description('Проверка поиска cерии книг')
@allure.feature('Проверка поиска cерии')
@allure.link('https://www.dom-knigi.ru/')
def test_search_series():
    with allure.step('Открываем главную страницу переходим в серии книг'):
        app.home_page.open_page(). \
            search_series()


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Pimenova')
@allure.description('Добавление в корзину книги')
@allure.feature('Проверка добавления книги в корзину неавторизованным пользователем')
@allure.link('https://www.dom-knigi.ru/')
def test_add_book_in_basket():
    with allure.step('Открываем главную страницу сайта'):
        app.home_page.open_page()
    with allure.step(f'Переходим на главную страницу и вводим в поиске наименование книги {data_home_page.book_to_read}'):
        app.home_page.search_book(data_home_page.book_to_read)
    with allure.step('Открываем книгу и добавляем в корзину'):
        app.book_page.open_book(). \
                add_in_basket()
    with allure.step('Проверяем, что книга добавлена в корзину'):
        app.book_page.quantity_in_basket()










# @allure.tag("web")
# @allure.severity(Severity.CRITICAL)
# @allure.label("owner", "Pimenova")
# @allure.description('Проверка авторизации')
# @allure.feature(f'Проверка авторизации с невалидным паролем')
# @allure.feature("Проверка отображния окна регистрации при вводе email, который отсутствует в системе")
# @allure.link("https://4lapy.ru/", name="Testing")
# def test_auth_with_not_exist_password():
#     with allure.step('Открываем главную страницу ЧетыреЛапы и форму авторизации'):
#         app.home_page.open_page()
#         app.login_page.click_login()
#     with allure.step('Вводим пароль меньше 6 знаков'):
#         app.login_page.enter_password()
#     with allure.step('Проверяем получение ошибки авторизации'):
#              app.login_page.check_error_auth_password()


# attach.add_html(browser)
# attach.add_screenshot(browser)
# attach.add_logs(browser)
# attach.add_video(browser)
