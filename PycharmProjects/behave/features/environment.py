from behave import fixture
from selenium import webdriver


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
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--start-maximized')
        # chrome_options.add_argument('--disable-extensions')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        context.browser = webdriver.Chrome(chrome_options=chrome_options)
    # context.browser = webdriver.Chrome()
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
