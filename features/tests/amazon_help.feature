# Created by danielb.mugabo at 9/27/21
Feature: Search for an order on Amazon

  Scenario: User can cancel an order
    Given open Amazon help page
    When input cancel order into search help library and press enter
    Then verify cancel order is executable