from behave import *

from features.pageobjects.SearchPage import SearchPage
from features.pageobjects.HomePage import HomePage
from features.pageobjects.BookPage import BookPage


@given('I open the Advanced Search page')
def step_impl(context):
    page = SearchPage(context)
    page.visit("https://rosenclassroom.com/advanced-search-filter")


@when("I enter 'Classic Chargers' title in search by title field")
def step(context):
    SearchPage(context).find_by_title_advanced("Classic Chargers")


@when("I push Advanced search button")
def step_impl(context):
    SearchPage(context).display_advanced_search_results()


@then("Advanced search result contains the product with 'Classic Chargers' title")
def step(context):
    finding_book_title = SearchPage(context).get_find_teaser_title_text()
    assert "Classic Chargers" in finding_book_title


@when("I enter 'Caitie McAneney' author name in search by author field")
def step(context):
    SearchPage(context).find_by_author_advanced("Caitie McAneney")


@when("I click on any book in advanced search results")
def step(context):
    SearchPage(context).open_book_page()

# make check for each found book
@then("I see that 'Caitie McAneney' is author name of the book")
def step(context):
    author_name = BookPage(context).get_book_author_name()
    assert "Caitie McAneney" in author_name


@when("I click on 'Format' field")
def step(context):
    SearchPage(context).find_by_format_advanced()


@when("I choose 'Multimedia' format from dropdown list")
def step(context):
    SearchPage(context).get_format_in_dropdown()


@then("Advanced search results contains the product with the 'Multimedia' format")
def step(context):
    books_format = SearchPage(context).get_books_with_format()
    for book in books_format:
        assert 'Multimedia' in book