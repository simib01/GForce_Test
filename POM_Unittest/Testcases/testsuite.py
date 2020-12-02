#Automation using Python Unittest framework
#command to run python testsuite.py in POM_Unittest\Testcases diretory

import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
sys.path.append("C:/Users/simib/PycharmProjects/POM_Unittest")
from Pages.MainPage import mainpage
from Pages.AddNewComputerPage import AddNewComputerPage


class testcase(unittest.TestCase):

    baseURL = "http://computer-database.herokuapp.com/computers"
    computer_name = "Computer name"
    Introduced_Date = "Introduced"
    Discontinued_Date = "Discontinued"
    Manufacturer = "Company"
    #chrome driver is downloaded and save in Driver folder for running selenium APIs
    driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")

    @classmethod
    def setUpClass(self):
        #Launch the computer database application
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = mainpage(self.driver)
        self.addComputer = AddNewComputerPage(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

##Main Page test cases
    #Test case to verify Main page UI Header
    def test_MainPage(self):
        self.lp.verify_homepage(self.computer_name,self.Introduced_Date,self.Discontinued_Date,self.Manufacturer)

    #Test case to verfify Update computer details
    def test_UpdateCompanyName(self):
        self.lp.select_computer("ACE")
        self.lp.change_company("Nokia")
        self.lp.click_save_button()
        self.lp.verify_companyName("ACE","Nokia")

#Add New computer Test cases
    #Test case to verify Add new computer functionality
    def test_AddComputer(self):
        self.addComputer.click_Add_new_computer()
        self.addComputer.Enter_computerName("ABC1")
        self.addComputer.Enter_IntroducedDate("1985-12-01")
        self.addComputer.Enter_DiscontinuedDate("2025-12-01")
        self.addComputer.Enter_Manufacturer("RCA")
        self.addComputer.click_Add_computer()
        self.addComputer.verify_computer_add("ABC1")
        self.addComputer.delete_computer("ABC1")

    #Test case to verify Add new Computer UI
    def test_AddComputerUI(self):
        self.addComputer.verify_addNewComputerUI()

#Generate HTML report for test cases in Reports folder
html_report_dir = '..\Reports'

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))