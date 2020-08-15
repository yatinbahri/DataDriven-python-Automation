class Locators(object):
    # Login Screen Locators

    username_textbox_xpath = "//android.widget.EditText[@content-desc='login_email_input']"
    password_textbox_xpath = "//android.widget.EditText[@content-desc='login_password_input']"
    sign_in_button_xpath = "//android.widget.TextView[@text='Sign in with email']"

    # Home Screen Locators

    leave_module_nav_xpath = "//android.widget.TextView[@text='Leaves']"
    home_validation_xpath = "//*[contains(@text,'Hey ')]"
    menu_icon_xpath = "//android.view.ViewGroup[@content-desc='home_hamburger_button']"

    # Hamburger Menu Locators

    logout_button_xpath = "//android.widget.TextView[@text='Log out']"
    confirmation_button_xpath = "//android.widget.TextView[@text='Yes']"