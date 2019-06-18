Feature: HomePage - Search
Scenario: Сheck that search by title return the correct results
  Given I open the website
  When I enter title 'snake' in search field
  Then I push search button
  Then search results contain the product with this title 'snake'

Scenario: Сheck that search by ISBN return the correct results
  Given I open the website
  When I enter ISBN '9781508139799' in search field
  Then I push search button
  Then I click on finding book
  Then on finding book page I see book with ISBN '9781508139799'

Scenario: Сheck that search by invalid title return the correct results
  Given I open the website
  When I enter title 'snakke' in search field
  Then I push search button
  Then search results don't contain the product with this title 'snakke'