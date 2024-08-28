import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="edge")


@pytest.fixture(scope="class")
def browser_setup(request):
    browser = request.config.getoption("--browser")
    
    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.maximize_window()
    driver.implicitly_wait(5) # Set implicit wait globally to 5 seconds
    urls = {
        "url": "https://www.saucedemo.com/"
        
    }
    
    request.cls.driver = driver
    request.cls.urls = urls
    driver.implicitly_wait(5)
    
    yield driver
    
    driver.quit()
