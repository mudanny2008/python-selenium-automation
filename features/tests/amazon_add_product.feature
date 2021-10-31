# Created by danielb.mugabo at 10/2/21
Feature: Test Scenarios for add to the cart functionality

  Scenario: User can add a product to the cart
    Given Open Amazon add Page
    When Input Watches into amazon search
    And Click amazon search icon
    And Click on the first product
    And Store product name
    #And Click on product
    And Click on add to the cart button
    And Open cart page
    Then Verify cart has 1 item(s)

Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon add page
 When Click Amazon Orders link
 Then Verify Sign In page is opened

Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon add page
 When Click on cart icon
 Then Verify 'Your Shopping Cart is empty.' text present

Scenario: User can select and search in a department
  Given Open Amazon add Page
  When Select department by alias stripbooks
  And Input Bible into amazon search
  And Click on Amazon search icon
  Then Verify books department is selected

Scenario: User can see New Arrivals
  Given Open Amazon product B074TBCSC8 Page
  When Hover over new arrivals options
  Then Verify correct options present