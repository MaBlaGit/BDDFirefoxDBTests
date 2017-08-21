Feature: Testing history in Firefox browser.

  Scenario: Log to the Firefox moz_places database and delete all entries
    Given I connect to the "places.sqlite" database
    When I run "delete_all" query against "moz_places"
    Then the "moz_places" should be empty

  Scenario Outline: Check if Firefox save browsing history
    Given I go to the "website"
    When I run "select_all" query against "moz_places"
    Then the "website" should be in "moz_places" table

      Examples:
        |       website         |
        |https://www.python.org |