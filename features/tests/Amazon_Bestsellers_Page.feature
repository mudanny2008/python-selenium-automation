# Created by danielb.mugabo at 10/1/21
Feature: Test for bestsellers page functionality

  Scenario: There are 5 bestsellers links
    Given Open Amazon Bestsellers
    Then Verify there are 5 links