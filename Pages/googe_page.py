from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class GooglePage():
    search_locator_class_name = "gb_Ue gb_sf VISqTe"
    news_page_url = "https://www.news.google.com"
    query = "covid-19"

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def accept_cookies(self):
        accept_button = self.wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, self.accept_button_xpath)))
        accept_button.click()

    def open_news_page(self):
        self.driver.get(self.news_page_url)
        # self.driver.get(url="https://www.news.google.com")

    def search(self, query: str):
        # search_field = self.wait.until(expected_conditions.presence_of_element(By.CLASS_NAME))
        search_field = self.driver.find_element_by_class_name(self.search_locator_class_name)
        search_field.send_keys(self.query)

