import time
from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from infra.basepage import BasePage


class LogicPage(BasePage):
    BASKETBALL_PATH = (By.XPATH, "//button[@class='main-header-module-desktop-tab '][./div[contains(text(),'כדורסל')]]")
    TENNIS_PATH = (By.XPATH, "//button[@class='main-header-module-desktop-tab '][./div[contains(text(),'טניס')]]")
    BASEBALL_PATH = (By.XPATH, "//button[@class='main-header-module-desktop-tab '][./div[contains(text(),'בייסבול')]]")

    VIDEO_TITLES = (By.ID, 'video-title')

    def __init__(self, driver):
        super().__init__(driver)
        self._driver.fullscreen_window()
        self.wait_xpath(
            "//button[@class='main-header-module-desktop-tab ']//div[contains(text(),'כדורסל')]")

        self.basketball_navigate_button = self._driver.find_element(*self.BASKETBALL_PATH)
        self.tennis_navigate_button = self._driver.find_element(*self.TENNIS_PATH)


    def navigate_to_basketball(self):
        self.basketball_navigate_button.send_keys(Keys.SPACE)

    def navigate_to_tennis(self):
        self.wait_xpath(self.TENNIS_PATH[1])

        self.tennis_navigate_button.send_keys(Keys.SPACE)