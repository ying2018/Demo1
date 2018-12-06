
from appium import webdriver


class TestBrowser(object):
    def setup_method(self,method):
        caps = {
            'platformName': 'Android',
            'platformVersion': '4.4',
            'deviceName': 'Android Emulator',
            'browserName': 'Browser'
        }
        # caps['platformName'] = 'android'
        # caps['deviceName'] = 'demo'
        # caps['browserName'] = 'browser'
        # caps["platformVersion"] = "6.0"
        # caps["appPackage"] = "com.android.browser"
        # caps["appActivity"] = ".BrowserActivity"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def test_android_browser(self):
        self.driver.get("http://testerhome.com")