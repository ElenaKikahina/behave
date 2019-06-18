#Укажем что это за фича
Feature: HomePage - Logo
#Укажем имя сценария (в одной фиче может быть несколько)
Scenario: After click on logo HomePage opens
#И используем наши шаги.
  Given I open the website
  When I click on logo
  Then I should be redirected to HomePage