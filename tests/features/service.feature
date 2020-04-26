Feature:DuckDuckGo

  Scenario Outline: Basic Duck DuckGo API
    Given the DuckDuckGo API is queried with "<phrase>"
    Then the response status code is "200"
    And the response contains results for "<phrase>"

    Examples: Animals
     | phrase   |
     | panda    |
     | python   |
     | platypus |

    Examples: Fruits
     | phrase    |
     | peach     |
     | pineapple |
     | banana    |