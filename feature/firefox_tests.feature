Feature: Test saving browse history in Firefox places.sqlite database.

  Scenario Outline: Check if Firefox save browsing history
    Given I go to the "website"
    And I check if page is "visible"
    When I run "find_website_name" query against "moz_places" table in "places.sqlite" database
    Then the "website" should be in the table

      Examples:
        |       website         |
        |https://www.python.org |