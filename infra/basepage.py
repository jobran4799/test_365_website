from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    def __init__(self, driver):
        self._driver = driver

    def wait_xpath(self, path):
        WebDriverWait(self._driver, 20).until(lambda x: x.find_element(By.XPATH, path))

    def wait_CSS(self, path):
        WebDriverWait(self._driver, 10).until(lambda x: x.find_element(By.CSS_SELECTOR, path))

    def get_url(self):
        return self._driver.current_url