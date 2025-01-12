from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def wait_for_presence(self, locator):
        return self._wait.until(expected_conditions.presence_of_element_located(locator))

    def get_element(self, locator):
        return self.driver.find_element(locator)

