from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Resources.screenLocators import Locators


class HamBurgerMenu(object):
    locator_obj = Locators()

    def __init__(self, driver):
        self.driver = driver

        # Local Variables
        self.logout_button_xpath = driver.find_element(By.XPATH, self.locator_obj.logout_button_xpath)

    def logout(self):
        self.driver.implicitly_wait(5)
        self.logout_button_xpath.click()
        self.driver.find_element(By.XPATH, self.locator_obj.confirmation_button_xpath).click()
        self.driver.implicitly_wait(5)

    def logout_validation(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.locator_obj.sign_in_button_xpath)))
            print('Found Login screen Element')
        except:
            print('Logout Validation Error - Login Element not found after logout')
