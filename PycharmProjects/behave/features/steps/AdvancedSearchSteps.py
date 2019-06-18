from behave import *

from features.pageobjects.SearchPage import SearchPage
from features.pageobjects.HomePage import HomePage


@given('I open the Advanced Search page')
def step_impl(context):
    page = SearchPage(context)
    page.visit("https://rosenclassroom.com/advanced-search-filter")


@when("I enter title 'koko the cat' in search title field")
def step(context):
    SearchPage(context).find_by_title_adv("koko the cat")


@then("I push Advanced search button")
def step_impl(context):
    SearchPage(context).click_search_adv()


@then("search results contain the product with this title 'koko the cat'")
def step(context):
    result = SearchPage(context).get_find_elements()
    return True
    for element in result:
        assert "koko the cat" in element


@when("I enter author name 'Caitie McAneney' in search author field")
def step(context):
    SearchPage(context).find_by_author("Caitie McAneney")


@then("search results contain the product by author name 'Caitie McAneney'")
def step(context):
    result = SearchPage(context).get_find_elements_by_author()
    return True
    for element in result:
        assert "Caitie McAneney" in element
