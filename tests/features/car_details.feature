Feature: Search car details using registration number
  Tests related to searching ona car valuation website and verify details
  Background: User is on the car valuation page

  Scenario Outline: User searches car valuation website with multiple registration numbers
    Given I have a list of car registration numbers "<input_file_name>"
    When Search for registration number in car valuation website
    Then Verify car details returned for registration number match the expected output

    Examples:
      | input_file_name |
      | car_input.txt   |
