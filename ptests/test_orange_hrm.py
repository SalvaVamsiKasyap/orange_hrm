import time

import pytest
from selenium.webdriver import ActionChains, Keys

from pageObjects.login_Page import login_Page
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class orange_hrm(BaseClass):

    def test_successful_login(self):
        log = self.get_logger()
        # orange-hrm login page
        A = ActionChains(self.driver)
        ohlp = login_Page(self.driver)
        username_inp = ohlp.enter_user_name()
        log.info("Entering the username..")
        username_inp.send_keys('Admin')
        log.info("Entered user name as Admin.")
        userpassword_inp = ohlp.enter_user_password()
        log.info("Entering the password")
        userpassword_inp.send_keys('admin123')
        log.info("Entered the password..")
        userpassword_inp.send_keys(Keys.ENTER)
        log.info("Navigating to the homepage..")
