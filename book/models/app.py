from book.models.pages.home_page import HomePage
from book.models.pages.login_page import LoginPage
from book.models.pages.book_page import BookPage
from book.models.pages.series_page import SeriesPage
from book.models.pages.basket_page import BasketPage


class ApplicationManager:

    def __init__(self):
        self.home_page = HomePage()
        self.login_page = LoginPage()
        self.book_page = BookPage()
        self.series_page = SeriesPage()
        self.basket_page = BasketPage()


app = ApplicationManager()
