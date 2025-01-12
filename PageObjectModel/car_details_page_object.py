from selenium.webdriver.common.by import By
from CommonUtils.BasePage import BasePage


class CarDetails(BasePage):
    ele_car_make = (By.CSS_SELECTOR, "h1[data-cy='vehicleMakeAndModel']")
    lst_vehicle_specifics = (By.CSS_SELECTOR, "ul[data-cy='vehicleSpecifics']")

    def get_car_make(self):
        return self.wait_for_presence(self.ele_car_make).text

    def get_vehicle_specification_list(self):
        return self.wait_for_presence(self.lst_vehicle_specifics).find_element(By.TAG_NAME, "li")

    def get_model_number(self):
        return self.get_vehicle_specification_list[0].text
