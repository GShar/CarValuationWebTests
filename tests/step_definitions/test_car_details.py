import re
import pandas as pd
import pytest
from pytest_bdd import scenarios, given, then, parsers, when
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from common_utils.Constants import URL, REGEX_REG_NUM, EXP_OUTPUT_FILE_NAME
from page_object_model.car_details_page_object import *
from page_object_model.car_search_page_object import *

scenarios("../features/car_details.feature")


# read the reg num from the input file
def read_reg_num_from_file(input_file_name):
    f = open(input_file_name)
    car_input_text = f.read()
    number_plate = re.findall(REGEX_REG_NUM, car_input_text)
    return number_plate


# contains the expected output to be used for verification
@pytest.fixture()
def expected_output():
    csv_data = pd.read_csv(EXP_OUTPUT_FILE_NAME)
    data_dict = csv_data.to_dict(orient='records')
    return data_dict


@pytest.fixture()
def lst_of_reg_num():
    return []


@pytest.fixture()
def records_from_search():
    return []


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@given("User is on the car valuation page")
def open_browser(chrome_browser):
    chrome_browser.get(URL)


@given(parsers.parse('I have a list of car registration numbers "{input_file_name}"'))
def list_of_registration_numbers(lst_of_reg_num, input_file_name):
    lst_of_reg_num.extend(read_reg_num_from_file(input_file_name))
    print(lst_of_reg_num)


@when('Search for registration number in car valuation website')
def search_for_reg_numbers(chrome_browser, lst_of_reg_num, records_from_search):
    car_search = CarSearch(chrome_browser)
    car_details = CarDetails(chrome_browser)

    for reg_num in lst_of_reg_num:
        dict_car_details = dict.fromkeys(['VARIANT_REG', 'MAKE_MODEL', 'YEAR'])
        car_search.enter_the_reg_num(reg_num=reg_num)
        dict_car_details['VARIANT_REG'] = reg_num
        car_search.click_search_button()
        car_make = car_details.get_car_make()
        dict_car_details['MAKE_MODEL'] = car_make
        car_model_number = car_details.get_model_number()
        dict_car_details['YEAR'] = car_model_number
        records_from_search.append(dict_car_details)


@then('Verify car details returned for registration number match the expected output')
def verify_details_of_the_car(records_from_search, expected_output, lst_of_reg_num):
    lst_expected_output = expected_output
    lst_records_from_search = records_from_search
    for reg in lst_of_reg_num:
        expected_matching_record = next(record for record in lst_expected_output if record['VARIANT_REG'] == reg)
        input_matching_record = next(record for record in lst_records_from_search if record['VARIANT_REG'] == reg)
        assert input_matching_record['MAKE_MODEL'] == expected_matching_record['MAKE_MODEL']
        assert input_matching_record['YEAR'] == expected_matching_record['YEAR']
