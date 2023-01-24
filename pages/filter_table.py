from pages.base_page import BasePage


class filter_table(BasePage):
    name_path = '/html/body/div[2]/div[3]/div/div[2]/div[1]/div/div/div/input'
    surname_path = '/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div/div/input'
    min_age = '/html/body/div[2]/div[3]/div/div[2]/div[3]/div/div/div/div[1]/div/input'
    max_age = '/html/body/div[2]/div[3]/div/div[2]/div[3]/div/div/div/div[2]/div/input'
    main_position = '/html/body/div[2]/div[3]/div/div[2]/div[4]/div/div/div/input'
    club_path = '/html/body/div[2]/div[3]/div/div[2]/div[5]/div/div/div/input'
    min_rate_path = '/html/body/div[2]/div[3]/div/div[2]/div[6]/div/div/div/div[1]/div/input'
    max_rate_path = '/html/body/div[2]/div[3]/div/div[2]/div[6]/div/div/div/div[2]/div/input'

    pass
