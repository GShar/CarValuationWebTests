
# PyBDD-Identity
This project is designed to automate a test scenario for a car valuation website  

### Prerequisites

Make sure you have Python and Pip installed.
Also make sure you are using an editor with support for Python.
I have used the Intellij Idea as the editor
* browser=chrome
* URL or car valuation website , https://www.motorways.co.uk

### Assumptions Made

I have assumed that we will have multiple files for this test and so have used Scenario Outline in the feature file,
instead of just simply using Scenario.

### Issues faced
I have had to face a major blocker which prevented me to run and test my code.
The car valuation website had blocked my IP Address, saying that there were too many attempts from my machine.
This prevented me from running the code and making progress.


### Code Structure:
common_utils - > Contains the commonly used base code  
  *  BasePage -> Contains Base function for the Page classes  
  *  Constants -> Contains the Constans used in the project  

page_object_model -> The Page Object Design Pattern, contains the Page Objects   
  *  car_details_page_object - > page object for car details page  
  *  car_search_page_object -> page object for car search page  

tests -> main folder for all the tests code  
  *  features-> contains the feature file for BDD scenarios/tests  
  *  step_definitions -> the test steps python for the features  

    

## Running the tests

Please folow the steps below to run the test suite:
1. After cloning, run the following command in the root directory:

 `pytest tests/step_definitions/test_car_details.py -v -s`


## Tools Used

1. Selenium
2. Python
3. Gherkin for BDD
4. Pandas
5. Pytest
6. Py-BDD

## Design Pattern

POM (Page Object Model)

I have kept my Page elements in the PageObjects within Page Object Classes.  
For each page , car search and car details respectively, I have created a seperate Page Object.  
This is to keep the locaters and web elements related identifiers in its own page.  


## Scenario Covered.

I have covered end-to-end scenario which inludes:
1. The tests for this E2E scenario will cover entering registration number on the car valuation website
2. Searching for the details
3. Verifying the details using expected output data

* For this test I have made use of Scenario Outline so that in future multiple input files cold also be used

## Authors
Gopal Sharma
