import time

from PageObjectsddt.LoginPage import LoginPage
from Utilities.readProperties import readconfig
from Utilities.customLogger import Loggen
from Utilities import XLUtils


class Test_loginpageDDT_001:
    baseURL = readconfig.getapplicationURL()
    path = ".//TestData//LoginData.xlsx"
    logger = Loggen.Loggen()

    def testLoginpage_ddt(self, setup):
        self.logger.info("************Test_loginpageDDT_001************")
        self.logger.info("************Verify testLoginpage************")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            actual_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if actual_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info('*****Passed*****')
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info('******Failed*****')
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif actual_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info('*****Failed*****')
                    self.lp.clickLogout()
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info('******Passed*****')
                    self.lp.clickLogout()
                    lst_status.append("Pass")
            if 'Fail' not in lst_status:
                self.logger.info("*****login DDT test passed")
                self.driver.close()
                assert True
            else:
                self.logger.info("*****login DDT test Failed")
                self.driver.close()
                assert False
        self.logger.info("************End of Test_loginpageDDT_001*****************")
