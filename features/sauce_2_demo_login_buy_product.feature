Feature: Log in online shop and buy a product

  Scenario: Buying a Sauce Labs Bolt T-Shirt
    Given I open the browser
    And open saucedemo.com page
    Then I log into the online shop
    And I reset app state
    When I add Sauce Labs Bolt T-Shirt into the cart
    Then I place an order
    And I log out
    And I close browser
