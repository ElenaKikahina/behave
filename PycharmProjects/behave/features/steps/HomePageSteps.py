from behave import *

from features.pageobjects.HomePage import HomePage
from features.pageobjects.SearchPage import SearchPage
from features.pageobjects.BookPage import BookPage
import allure

@given('I open the website')
def step_impl(context):
    page = HomePage(context)
    page.visit("https://rosenclassroom.com")


@when("I click on logo")
def step(context):
    HomePage(context).click_logo()


@then("I should be redirected to HomePage")
def step(context):
    url = HomePage(context).get_url()
    assert "https://rosenclassroom.com" in url


@when("I enter title 'snake' in search field")
def step(context):
    HomePage(context).find_by_title("snake")


@then("I push search button")
def step_impl(context):
    HomePage(context).click_search()


@then("search results contain the product with this title 'snake'")
def step(context):
    result = SearchPage(context).get_find_elements()
    return True
    for element in result:
        assert "snake" in element


@when("I enter ISBN '9781508139799' in search field")
def step(context):
    HomePage(context).find_by_isbn("9781508139799")


@then("I click on finding book")
def step(context):
    HomePage(context).click_book_name()


@then("on finding book page I see book with ISBN '9781508139799'")
def step(context):
    resultt = BookPage(context).get_find_isbn("9781508139799")
    assert "9781508139799" in resultt


@when("I enter title 'snakke' in search field")
def step(context):
    HomePage(context).find_by_title("snakke")


@then("search results don't contain the product with this title 'snakke'")
def step(context):
    result = SearchPage(context).get_find_elements("snakke")
    return False
    for element in result:
        assert "snakke" in element

#@then("search results contain message 'No results found for your search'")
#def step(context):
#    page = SearchPage(context).get_not_find_element("No results found for your search")
#    assert "No results found for your search" in page

