import unittest
from infra.brawser_wrapper import BrowserWrapper
from logic.logic import LogicPage


class TestPage(unittest.TestCase):

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.driver = self.browser_wrapper.get_driver()
        self.logic_page = LogicPage(self.driver)

    def test_navigate_to_tennis(self):
        self.logic_page.navigate_to_tennis()
        url = self.logic_page.get_url()
        self.assertEqual(url, "https://www.365scores.com/he/tennis")


    def test_navigate_to_basketball(self):
        self.logic_page.navigate_to_basketball()
        url = self.logic_page.get_url()
        self.assertEqual(url, "https://www.365scores.com/he/basketball")

    def tearDown(self):
        self.driver.quit()
