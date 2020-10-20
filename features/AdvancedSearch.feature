Feature: AdvancedSearch


  Scenario: Advanced search by title returns the correct results
    Given I open the Advanced Search page
    When I enter 'Classic Chargers' title in search by title field
    And I push Advanced search button
    Then Advanced search result contains the product with 'Classic Chargers' title


  Scenario: Advanced search by author returns the correct results
    Given I open the Advanced Search page
    When I enter 'Caitie McAneney' author name in search by author field
    And I push Advanced search button
    And I click on any book in advanced search results
    Then I see that 'Caitie McAneney' is author name of the book

@test
  Scenario: Advanced search by format returns the correct results
    Given I open the Advanced Search page
    When I click on 'Format' field
    And I choose 'Multimedia' format from dropdown list
    And I push Advanced search button
    Then Advanced search results contains the product with the 'Multimedia' format