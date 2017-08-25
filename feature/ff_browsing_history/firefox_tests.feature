Feature: Test saving browse history in Firefox places.sqlite database.

  Scenario Outline: Check if Firefox save browsing history
    Given I open <website> web page
    And I check if <website> web page is visible
    When I run "select_url_from_database" - <query> against "moz_places" table in "places.sqlite" database
    Then the <website> web page address should be in the table

      Examples:

        | website |     query       |
        | python  |    python       |
        |   edX   |      edX        |
        |  udemy  |     udemy       |
        | netflix |    netflix      |