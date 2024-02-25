import json
import time
from os.path import dirname, join

from selenium import webdriver

try:
    with open('../infra/config.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
    raise  # Raise the error to halt execution if the file is essential for the script to run


class BrowserWrapper:

    def __init__(self):
        self.driver = None

    def get_driver(self):
        global options
        browser_type = data["browser"]
        if data["grid"]:
            if browser_type.lower() == 'chrome':
                options = webdriver.ChromeOptions()
            elif browser_type.lower() == 'firefox':
                options = webdriver.FirefoxOptions()
            elif browser_type.lower() == 'edge':
                options = webdriver.EdgeOptions()
            platform_name = data["platform"]
            options.add_argument(f'--platformName={platform_name}')
            self.driver = webdriver.Remote(command_executor=data["hub"], options=options)
        else:
            if browser_type.lower() == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser_type.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser_type.lower() == 'edge':
                self.driver = webdriver.Edge()
        url = data["url"]
        self.driver.get(url)
        time.sleep(4)
        return self.driver

    def close_browser(self):
        if self.driver:
            self.driver.close()


