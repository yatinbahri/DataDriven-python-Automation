


def desired_capabilities(self):
    return dict (platformName= 'Android',
            deviceName= '8UEDU18714000545',
            remote_url= 'http://localhost:4723/wd/hub',
            platform_version='8.0.0',
            appActivity= 'com.MainActivity',
            appPackage= 'com.staging',
            automationName= 'uiautomator2')
