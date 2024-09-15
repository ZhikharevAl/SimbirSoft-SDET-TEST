import logging

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function", autouse=True)
def setup_teardown(request, browser):
    allure.dynamic.parameter("browser", browser.capabilities["browserName"])
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(browser.get_screenshot_as_png(),
                      name=f"screenshot_{item.name}",
                      attachment_type=allure.attachment_type.PNG)
        allure.attach(
            "\n".join(browser.get_log("browser")),
            name="browser_logs",
            attachment_type=allure.attachment_type.TEXT
        )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

def pytest_configure(config):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

@pytest.fixture(scope='session')
def logger():
    return logging.getLogger(__name__)
