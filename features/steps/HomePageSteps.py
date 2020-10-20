from behave import *

from features.pageobjects.BookPage import BookPage
from features.pageobjects.HomePage import HomePage
from features.pageobjects.SearchPage import SearchPage


@given('I open the website')
def step_impl(context):
    page = HomePage(context)
    page.visit("https://rosenclassroom.com")


@when("I click on site logo")
def step(context):
    HomePage(context).click_logo()


@then("I should be redirected to HomePage")
def step(context):
    url = HomePage(context).get_url()
    assert "https://rosenclassroom.com" in url


@when("I enter 'Classic Chargers' title in search field")
def step(context):
    HomePage(context).find_by_query_in_search_field("Classic Chargers")


@when("I push search button")
def step_impl(context):
    HomePage(context).display_simple_search_results()


@then("search results contain the product with 'Classic Chargers' title")
def step(context):
    book_title = SearchPage(context).get_find_teaser_title_text()
    assert "Classic Chargers" in book_title


@when("I enter '9781508139799' ISBN in search field")
def step(context):
    HomePage(context).find_by_query_in_search_field("9781508139799")


@when("I click on finding book")
def step(context):
    SearchPage(context).open_book_page()


@then("I see book with '9781508139799' ISBN on finding book page")
def step(context):
    book_isbn = BookPage(context).get_book_isbn_info()
    assert "978-1-5081-3979-9" in book_isbn


@when("I enter 'snakke' title in search field")
def step(context):
    HomePage(context).find_by_query_in_search_field("snakke")


@then("search result contains the 'No results found for your search' message")
def step(context):
    result_not_found_message = SearchPage(context).get_not_search_message()
    assert "No results found for your search" in result_not_found_message


