from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class GooglePage():
    search_locator_class_name = \
        (By.XPATH, '//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]')
    news_page_url = "https://www.news.google.com"
    accept_button_xpath_locator = \
        (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/div[2]')
    covid19_suggestion_xpath_locator = (By.XPATH, '//*[@id="nngdp150"]/div/div/div/div[2]')


    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def accept_cookies(self):
        accept_button = self.wait.until(expected_conditions.presence_of_element_located(
            self.accept_button_xpath_locator))
        accept_button.click()

    def open_news_page(self):
        self.driver.get(self.news_page_url)
        # self.driver.get(url="https://www.news.google.com")

    def search(self, query: str):
        # search_field = self.wait.until(expected_conditions.presence_of_element(By.CLASS_NAME))
        search_field = self.driver.find_element(*self.search_locator_class_name)
        search_field.send_keys(query)
        search_field.send_keys(Keys.ENTER)
        # covid19_suggestion_element = self.wait.until(expected_conditions.presence_of_element_located(
        #     self.accept_button_xpath_locator))
        # covid19_suggestion_element.click()

        # // *[ @ id = "c286"] / div / h2


