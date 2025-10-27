import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def pre_post_condition():
    options = Options()
    #options.add_argument('start-maximized')
    #options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()