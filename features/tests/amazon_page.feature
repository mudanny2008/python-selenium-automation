# Created by danielb.mugabo at 9/27/21
Feature: Amazon page


  Scenario: User can verify that amazon cart is empty
    Given open Amazon page
    When click on the cart icon
    Then verify that amazon cart is empty
