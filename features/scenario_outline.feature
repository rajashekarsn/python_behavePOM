Feature:  search "behave" using scenario outline
  @scenariooutline
  Scenario Outline: search from the examples table
    Given using "<site>" to search
    When user searches for "<things>"
    Examples: Vegetables
      | site                         | things        |
      | https://google.com/          | carrot        |
      | https://duckduckgo.com/      | beans         |