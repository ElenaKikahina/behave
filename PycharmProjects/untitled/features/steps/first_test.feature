#Укажем что это за фича
Feature: Checking logo
#Укажем имя сценария (в одной фиче может быть несколько)
Scenario: Сheck that after click logo homepage opens
#И используем наши шаги.
  Given website "rosenclassroom.com"
  Then push button with text 'Rosen Classroom'
  Then check that page opens 'rosenclassroom.com'

# Scenario: Сheck that search by title return the correct results
 # Given website "rosenclassroom.com"
  #Then enter title 'snake' in search field and push search button
  #Then search results contain the product with this title 'snake'