from Resources import XLUtil
from Resources.baseSpecification import BaseSpecification
from POM.loginScreen import *
from POM.homeScreen import *
from POM.hamBurgerMenu import *
import unittest


class LoginTest(BaseSpecification):
    def test_LoginToEmployee(self):

        path = "<file_path.xlsx>"

        rows = XLUtil.getRowCount(path, 'Login')

        for r in range(2, rows + 1):
            username = XLUtil.readData(path, 'Login', r, 1)
            driver = self.driver
            loginscreen = LoginToEmployee(driver)
            loginscreen.enter_username(username)
            password = XLUtil.readData(path, 'Login', r, 2)
            loginscreen.enter_password(password)

            loginscreen.click_sign_in()
            try:
                homeScreen = HomeScreen(driver)

                Result = homeScreen.home_element_validation()

                if Result:
                    print ("Test Passed")
                    XLUtil.writeData(path, 'Login', r, 3, "Test Passed")
                    homeScreen.click_on_hamburger_menu()
                    hamBurgerMenu = HamBurgerMenu(driver)
                    hamBurgerMenu.logout()
                else:
                    print("Test failed")
                    XLUtil.writeData(path, 'Login', r, 3, "Test Failed")
            except:
                print("Test failed")
                XLUtil.writeData(path, 'Login', r, 3, "Test Failed")


if __name__ == '__main__':
    unittest.main()
