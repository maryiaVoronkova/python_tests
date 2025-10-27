import allure
import requests

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCommon:

    @allure.story("UI")
    @allure.title("UI tests for Onliner pagers")
    def test_example_ui_interaction_selenium(self, pre_post_condition):
        driver = pre_post_condition
        with allure.step('Go to Onliner WebSite'):
            driver.get("https://www.onliner.by/")
        with allure.step('Click on the button Вход'):
            driver.find_element(By.XPATH, "//div[contains(@class, 'auth-bar__item') and .='Вход']").click()
        with allure.step('Click on the Link Я не помню пароль'):
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Я не помню пароль")))
            driver.find_element(By.PARTIAL_LINK_TEXT,"Я не помню пароль").click()
        with allure.step('Check the page contains title Восстановление пароля'):
            assert driver.find_element(By.XPATH, "//div[contains(@class, 'auth-form__title')]").text.strip() == "Восстановление пароля"

    @allure.story("API")
    @allure.title("API for GET requests for objects")
    def test_example_api_interaction(self):
        request_url ="https://api.restful-api.dev/objects"
        response = requests.get(request_url)
        assert response.status_code == 200
        objects_list = response.json()
        assert len(objects_list) == 13