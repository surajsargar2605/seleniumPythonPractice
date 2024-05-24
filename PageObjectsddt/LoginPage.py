from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_by_id = 'Email'
    textbox_password_by_id = 'Password'
    button_login_by_xpath = '//button[@type="submit"]'
    button_logout_by_Link_text = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_by_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_by_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_by_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_by_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_by_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.button_logout_by_Link_text).click()
