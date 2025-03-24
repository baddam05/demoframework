
from selenium import webdriver
import pytest # This is needed to attach screenshots!
import pytest_html
import base64


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


import pytest
import base64
import pytest_html

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")  # Make sure 'setup' is your fixture name
        if driver:
            # Take screenshot in memory
            screenshot = driver.get_screenshot_as_png()
            encoded = base64.b64encode(screenshot).decode('utf-8')
            img_html = f'<div><img src="data:image/png;base64,{encoded}" ' \
                       f'style="width:600px;height:auto;" alt="screenshot"></div>'

            # Attach to HTML report
            extra = getattr(report, 'extra', [])
            extra.append(pytest_html.extras.html(img_html))
            report.extra = extra



@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser!")

    yield driver
    driver.quit()


def pytest_metadata(metadata):
    # Remove unwanted metadata
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

    # Add custom metadata
    metadata['Project Name'] = 'framework'
    metadata['Module Name'] = 'shopping'
    metadata['Tester'] = 'rakhi'
    return metadata


























