from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BaseClass:
    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(by_locator)).click()


    def do_send_keys(self,by_locator,text):
            WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(by_locator)).text

    def get_all_elements(self,by_locator):
        return WebDriverWait(self.driver,10).until(ec.visibility_of_all_elements_located(by_locator))


