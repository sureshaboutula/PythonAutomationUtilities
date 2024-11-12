# Created by SureshAboutula at 2024-11-03
Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here

  @smoke @library
  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to the Library
    When we execute the AddBook PostAPI method
    Then book is successfully added

    @regression @library
    Scenario Outline: Verify AddBook API functionality
    Given the Book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
      Examples:
        |isbn  | aisle |
        | sudsd | 659 |
        | sadyr | 8406 |
