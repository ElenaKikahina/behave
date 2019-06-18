from behave import fixture
from selenium import webdriver
from allure_behave.hooks import allure_report


@fixture
def before_all(context):
    print("Executing before all")


def before_feature(context, feature):
    print("Before feature\n")


def before_scenario(context, scenario):
    print("Before scenario")
    # behave -D BROWSER=chrome features
    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is None:
            BROWSER = 'chrome'
        else:
            BROWSER = context.config.userdata['BROWSER']
    else:
        BROWSER = 'chrome'
    if BROWSER == 'chrome':
        context.browser = webdriver.Chrome()
    elif BROWSER == 'firefox':
        context.browser = webdriver.Firefox()
    elif BROWSER == 'safari':
        context.browser = webdriver.Safari()
    elif BROWSER == 'ie':
        context.browser = webdriver.Ie()
    elif BROWSER == 'opera':
        context.browser = webdriver.Opera()
    elif BROWSER == 'phantomjs':
        context.browser = webdriver.PhantomJS()
    else:
        print("Browser you entered:", BROWSER, "is invalid value")

    context.browser.maximize_window()
    print("Before scenario\n")


def after_scenario(context, scenario):
    #print("After scenario")
    context.browser.quit()


def after_feature(context, feature):
    print("\nAfter Feature")


def after_all(context):
    print("After all")

allure_report("path/to/result/dir")