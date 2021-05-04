from selenium import webdriver

from Pages.googe_page import GooglePage


def test_open_news_page():

    drv = webdriver.Chrome()
    gp = GooglePage(drv)
    gp.open_news_page()
    gp.accept_cookies()

    assert gp.driver.title.startswith("Google News")


# Open https://news.google.com/
# Search for “Covid-19”
# Select “Covid-19” from the dropdown menu
# Verify you are on the right page
# Extract a list of strings for all the headlines for “Top news”
# Extract a list of strings for all the headlines for “Local news”
# Extract a list of strings for all the headlines for “Fact Check”

# Verify that the share link functionality works.
# Copy the link and open it in the same tab.
# Verify that the page opens up for Covid-19.