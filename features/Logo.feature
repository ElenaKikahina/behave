#Specify the Feature name.
Feature: HomePage - Logo
#Specify the Scenario name (there may be several in one Feature).
Scenario: HomePage opens after click on site logo
#Specify the steps of the test case.
  Given I open the website
  When I click on site logo
  Then I should be redirected to HomePage

