from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Resources.screenLocators import Locators


class HomeScreen(object):
    locator_obj = Locators()

    def __init__(self, driver):
        self.driver = driver

        # Local Variables
        self.leave_module_nav_xpath = driver.find_element(By.XPATH, self.locator_obj.leave_module_nav_xpath)
        self.home_validation_xpath = driver.find_element(By.XPATH, self.locator_obj.home_validation_xpath)
        self.menu_icon_xpath = driver.find_element(By.XPATH, self.locator_obj.menu_icon_xpath)

    # Home element validation
    def home_element_validation(self):
        self.driver.implicitly_wait(5)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.locator_obj.home_validation_xpath)))
            print('Found Home element!')
            return True
        except:
            print('Can not find the Home element')


    # Navigation to Leave Module
    def navigate_to_leave_module(self):
        self.leave_module_nav_xpath.click()

    # Click on Hamburger Menu
    def click_on_hamburger_menu(self):
        self.driver.implicitly_wait(5000)
        self.menu_icon_xpath.click()
