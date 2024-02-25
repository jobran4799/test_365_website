# test_runner.py
import json
import unittest
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

from infra.brawser_wrapper import BrowserWrapper
from tests.tests import TestPage

try:
    with open('../infra/config.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
    raise  # Raise the error to halt execution if the file is essential for the script to run


def test_brawser_runer(browser):
    TestPage.browser = browser

    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestPage)
    print(test_suite, browser)

    unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    browser_wrapper = BrowserWrapper()
    parallel = data["parallel"]
    grid = data["grid"]
    get_browser = data["browser"]
    if grid:
        browsers = data["browser_types"]

        if parallel:
            with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
                executor.map(test_brawser_runer, browsers)
        else:
            for browser in browsers:
                test_brawser_runer(browser)

    else:
        test_brawser_runer(get_browser)
