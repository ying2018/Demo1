from time import sleep

from appium import webdriver


class TestPytest(object):
    def setup_method(self,method):
        caps = {}
        caps['platformName'] = 'android'
        caps['deviceName'] = 'demo'
        caps['appPackage'] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def test_xueqiu(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/iv_close").click()
        sleep(2)
        self.driver.find_element_by_xpath("//*[@text='动态']").click()

    def test_xueqiu_login(self):
        self.driver.find_element_by_xpath("//*[@text='手机及其他登录']").click()