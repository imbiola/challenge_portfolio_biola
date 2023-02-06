import time

from pages.login_page import LogInPage
from pages.add_player import Add_player

import os
import unittest

from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT




class TestNewPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_very_new_player(self):
        user_login = LogInPage(self.driver)
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        new_player = Add_player(self.driver)
        new_player.new_player()
        new_player.name_player()
        new_player.print_player_name('Super')
        new_player.surname_button()
        new_player.surname_player('BOSS')
        new_player.position_button()
        new_player.position_player('3000')
        new_player.date_button()
        new_player.actual_date('02/06/2023')
        new_player.submit_button()
        time.sleep(7)




    @classmethod
    def tearDown(self):
        self.driver.quit()