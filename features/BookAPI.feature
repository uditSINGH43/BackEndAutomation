# Created by Udit Singh at 16-10-2025
Feature: Verify if Books are added or deleted using Library API
  # Enter feature description here
  @library
  Scenario: Verify AddBook API functionality
    Given the book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And status code of response should be 200



  @library
  Scenario Outline: Verify AddBook API functionality
    Given the book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
    Examples:
      |isbn  | aisle |
      |sdsas | 6780  |
      |zaku  |6789   |
      |makima|106    |