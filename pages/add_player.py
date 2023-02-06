import time

from pages.base_page import BasePage


class Add_player(BasePage):
    add_player_button_xpath = '//div[2]//a/button/span[1]'
    name_button_xpath = '//div[2]/div/div/input'
    surname_button_xpath = '//div[3]/div/div/input'
    main_pos_but_xpath = '//div[11]/div/div/input'
    submit_button_xpath = '//div[3]/button[1]/span[1]'
    date_button_xpath = '//div[7]/div/div/input'

    def new_player(self):
        self.click_on_the_element(self.add_player_button_xpath)
    def name_player(self):
        self.click_on_the_element(self.name_button_xpath)
    def print_player_name(self, name):
        self.field_send_keys(self.name_button_xpath, name)
    def surname_button(self):
        self.click_on_the_element(self.surname_button_xpath)
    def surname_player(self, surname):
        self.field_send_keys(self.surname_button_xpath, surname)
    def position_button(self):
        self.click_on_the_element(self.main_pos_but_xpath)
    def position_player(self, position):
        self.field_send_keys(self.main_pos_but_xpath, position)
    def date_button(self):
        self.click_on_the_element(self.date_button_xpath)
    def actual_date(self, date):
        self.field_send_keys(self.date_button_xpath, date)

    def submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title



    pass