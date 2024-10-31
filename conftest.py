import pytest
from helpers import WebdriverFactory  # Убедитесь, что вы импортируете WebdriverFactory

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    driver = WebdriverFactory.getWebdriver(browser)
    yield driver
    driver.quit()

#class WebdriverFactory:
    #@staticmethod
    #def getWebdriver(browserName):
        #if browserName == "firefox":
            #return webdriver.firefox
        #elif browserName == "chrome":
            #return webdriver.chrome