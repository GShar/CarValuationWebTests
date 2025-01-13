from selenium.webdriver.common.by import By

from common_utils.BasePage import BasePage

'''
Page Object class for the car search page
'''


class CarSearch(BasePage):
    txt_reg_num = (By.ID, "vrm-input")
    btn_search = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_the_reg_num(self, reg_num):
        self.wait_for_presence(self.txt_reg_num).send_keys(reg_num)

    def click_search_button(self):
        self.wait_for_presence(self.btn_search).click()
