from pages.base_page import BasePage


class LogInPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = 'Scouts panel - sign in'
    title_of_box_xpath = '//form//h5'
    header_of_box = 'Scouts panel'
    # email = 'test_lala@gmail.com'
    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title
    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

