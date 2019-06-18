Feature: AdvancedSearch
Scenario: Сheck that Advanced search by title return the correct results
  Given I open the Advanced Search page
  When I enter title 'koko the cat' in search title field
  Then I push Advanced search button
  Then search results contain the product with this title 'koko the cat'

Scenario: Сheck that Advanced search by author return the correct results
  Given I open the Advanced Search page
  When I enter author name 'Caitie McAneney' in search author field
  Then I push Advanced search button
  Then search results contain the product by author name 'Caitie McAneney'