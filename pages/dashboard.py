import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    mainpage_button = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span'
    players_button = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span'
    language_button = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span'
    sign_out_button = '//ul[3]/div[2]/div[2]/span'
    surname_button = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[3]/table/thead/tr/th[2]/span/button/span[1]/div/div[1]'
    age_button = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[3]/table/thead/tr/th[3]/span/button/span[1]/div/div[1]'
    mainposition_button = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[3]/table/thead/tr/th[4]/span/button/span[1]/div/div[1]'
    club_button = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[3]/table/thead/tr/th[5]/span/button/span[1]/div/div[1]'
    rating_button = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[3]/table/thead/tr/th[6]/span/button/span[1]/div/div[1]'
    filter_table = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[1]/div[2]/span[3]/button/span[1]/svg'
    last_player_button = '//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]'
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = 'Scouts panel'
    title_of_box_xpath = '//header/div/h6'
    def get_page_title(self, url):
       self.driver.get(url)
       return self.driver.title

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.players_button)
        assert self.get_page_title(self.login_url) == self.expected_title

    def last_player(self):
        self.click_on_the_element(self.last_player_button)

    def press_button(self):
        self.click_on_the_element(self.sign_out_button)

    pass