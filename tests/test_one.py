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
            button_login()
    with allure.step('Проверяем появление ошибки'):
        app.login_page.check_error_auth_email()


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Pimenova')
@allure.description('Проверка поиска')
@allure.feature('Проверка поиска отсутствующей книги')
@allure.link('https://www.dom-knigi.ru/')
def test_error_search_product(preparations):
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
def test_valid_search_book(preparations):
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
def test_search_series(preparations):
    with allure.step('Открываем главную страницу переходим в серии книг'):
        app.home_page.open_page()
    with allure.step('Выбираем раздел "Серии"'):
        app.series_page.open_series()
    with allure.step('Открываем определенную серию и проверяем, что открылась верная серия книг'):
        app.series_page.selection_specific_series().\
            check_valid_series()


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Pimenova')
@allure.description('Добавление в корзину книги')
@allure.feature('Проверка добавления книги в корзину неавторизованным пользователем')
@allure.link('https://www.dom-knigi.ru/')
def test_add_book_in_basket(preparations):
    with allure.step('Открываем главную страницу сайта'):
        app.home_page.open_page()
    with allure.step(f'Переходим на главную страницу и вводим в поиске наименование книги {data_home_page.book_to_read}'):
        app.home_page.search_book(data_home_page.book_to_read)
    with allure.step('Открываем книгу и добавляем ее в корзину'):
        app.book_page.open_book(). \
                add_in_basket()
    with allure.step('Проверяем, что книга добавлена в корзину'):
        app.book_page.quantity_on_page()


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Pimenova')
@allure.description('Ввод неверного промокода в корзине')
@allure.feature('Ввод неверного промокода в корзине')
@allure.link('https://www.dom-knigi.ru/')
def test_not_valid_promocode(preparations):
    with allure.step('Открываем главную страницу сайта'):
        app.home_page.open_page()
    with allure.step(f'Переходим на главную страницу и вводим в поиске наименование книги {data_home_page.book_to_read}'):
        app.home_page.search_book(data_home_page.book_to_read)
    with allure.step('Открываем книгу и добавляем ее в корзину'):
        app.book_page.open_book(). \
                add_in_basket()
    with allure.step('Открываем корзину'):
        app.basket_page.open_basket()
    with allure.step('Вводим в поле промокод и проверяем, что появилась ошибка'):
        app.basket_page.enter_promocode(data_home_page.not_valid_promocode).\
            apply_button().\
            check_error_promocode()


