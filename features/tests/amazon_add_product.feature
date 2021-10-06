# Created by danielb.mugabo at 10/2/21
Feature: Test Scenarios for add to the cart functionality

  Scenario: User can add a product to the cart
    Given Open Amazon Page
    When Input Watches into amazon search
    And Click on amazon search icon
    #And Click on the first product
    And Store product name
    And Click on product
    And Click on add to the cart
    And Open cart page
    Then Verify cart has 1 item(s)

