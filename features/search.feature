Feature: Search for "behave" in a duckduckgo website

  Scenario: search behave
    Given   web page "https://duckduckgo.com/" is open
    When the user searches for "behave"
    Then The search results should be displayed
    And the results should contains "behave"

  @googleTest
  Scenario: search behave using google
    Given   A new web page "https://google.com/" is open