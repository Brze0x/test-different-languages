import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language es or en")


@pytest.fixture(scope="function")
def browser(request):
    # Setup
    print("\nstart browser..")
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=profile)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    # Teardown
    print("\nquit browser..")
    browser.quit()