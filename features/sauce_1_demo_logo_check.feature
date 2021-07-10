Feature: Logo on main page
  I want to check if logo on main page is present correctly

  @test_1
  Scenario: Checking if logo on main page is available
    Given I launch the browser
    When open saucedemo.com page
    Then verify if the logo is present on main page
    And close browser
