Feature: Manipulating cookies and checking behaviour of the web page

  Scenario Outline: Delete cookies, refresh page and check if cookies policy alert is visible
    Given I open <webpage> web page
    And I check if "netflix cookies policy" is visible
    And I "accept cookie" policy
    When I delete cookies from current session
    And I refresh the web page
    Then the "netflix cookies policy" should be visible again

      Examples:
        |webpage|
        |netflix|