from pages.base_page import BasePage


class Dashboard(BasePage):
    mainpage_button = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span'
    players_button = '//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span'
    language_button = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span'
    sign_out_button = '//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span'
    surname_button = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[3]/table/thead/tr/th[2]/span/button/span[1]/div/div[1]'
    age_button = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[3]/table/thead/tr/th[3]/span/button/span[1]/div/div[1]'
    mainposition_button = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[3]/table/thead/tr/th[4]/span/button/span[1]/div/div[1]'
    club_button = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[3]/table/thead/tr/th[5]/span/button/span[1]/div/div[1]'
    rating_button = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[3]/table/thead/tr/th[6]/span/button/span[1]/div/div[1]'
    filter_table = '//*[@id="__next"]/div[1]/main/div[2]/div/div/div[1]/div[2]/span[3]/button/span[1]/svg'
    pass