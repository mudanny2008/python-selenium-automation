# Created by danielb.mugabo at 9/28/21
Feature: Hamburger menu tests

  Scenario: Users can see amazon hamburger menu
    Given open Amazon page
    When Click on Amazon search icon
    Then verify hamburger menu icon is present

    Scenario: user can click in option
      Given open Amazon page
      When click on the icon
      Then verify text