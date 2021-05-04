import pytest
from selenium import webdriver

from Pages.googe_page import GooglePage


@pytest.fixture()
def google_page():
    drv = webdriver.Chrome()
    gp = GooglePage(drv)
    gp.open_news_page()
    gp.accept_cookies()
    yield gp
