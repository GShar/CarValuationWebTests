from selenium.webdriver.common.by import By
from common_utils.BasePage import BasePage

'''
This is the page object class for the car details page
'''
class CarDetails(BasePage):
    loc_car_make = (By.CSS_SELECTOR, "h1[data-cy='vehicleMakeAndModel']")
    loc_vehicle_specifics = (By.CSS_SELECTOR, "ul[data-cy='vehicleSpecifics']")

    def get_car_make(self):
        return self.wait_for_presence(self.loc_car_make).text

    def get_vehicle_specification_list(self):
        return self.wait_for_presence(self.loc_vehicle_specifics).find_element(By.TAG_NAME, "li")

    def get_model_number(self):
        return self.get_vehicle_specification_list[0].text
