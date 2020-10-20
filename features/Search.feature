Feature: HomePage - Search


Scenario: Search by title returns the correct results
  Given I open the website
  When I enter 'Classic Chargers' title in search field
  And I push search button
  Then search results contain the product with 'Classic Chargers' title


Scenario: Search by ISBN returns the correct results
  Given I open the website
  When I enter '9781508139799' ISBN in search field
  And I push search button
  And I click on finding book
  Then I see book with '9781508139799' ISBN on finding book page


Scenario: Search by invalid title doesn't return the finding books
  Given I open the website
  When I enter 'snakke' title in search field
  And I push search button
  Then search result contains the 'No results found for your search' message