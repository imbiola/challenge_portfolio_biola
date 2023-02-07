import time

from pages.add_player import Add_player
from pages.login_page import LogInPage
from pages.dashboard import Dashboard
import os
import unittest

from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT




class TestNewLanguage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_last_player_system(self):
        user_login = LogInPage(self.driver)
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        last_player_info = Dashboard(self.driver)
        last_player_info.last_player()
        add_new_language = Add_player(self.driver)
        add_new_language.add_language()
        add_new_language.print_new_language('MEGUSTA')
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()