# -*- coding: utf-8 -*-
from lib2to3.pgen2 import driver

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from features.steps.home_page import Logo


@given('website "{url}"')
def step_impl(context, url):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get("https://rosenclassroom.com")

    homepage = Logo(driver)
    homepage.click_logo()


# Теперь нажмем на кнопку "Logo"
@then("push button with text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable(Logo.logo_id)
    )
    context.browser.find_element_by_id(Logo.logo_id).click()


# Проверим, что мы на странице с результатами поиска, есть некоторый искомый текст
@then("check that page opens '{url}'")
def step(context, url):
    WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '/html/head/title'.format()))
    )
    assert context.browser.find_element_by_xpath('/html/head/title'.format())
    context.browser.quit()


@then("enter title '{text}' in search field and push search button")
def step(context, text):
    context.browser.find_element_by_name('s').send_keys('snake')
    WebDriverWait(context.browser, 120).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="search-box-menu"]/div[1]/button'))
    )
    context.browser.find_element_by_xpath('//*[@id="search-box-menu"]/div[1]/button').click()


@then("search results contain the product with this title '{text}'")
def step(context, text):
     assert context.browser.find_element_by_class_name('product-small-teaser__title'.format()), title_contains ('snake')
