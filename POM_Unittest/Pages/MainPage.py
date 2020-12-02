from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators.Locators import locator as lc
from selenium.webdriver.support.ui import Select



class mainpage():
    def __init__(self,driver):
        self.driver = driver

    # verify the UI elements in main page
    def verify_homepage(context,computer_name,Introduced_Date,Discontinued_Date,Manufacturer):
        context.driver.find_element(By.PARTIAL_LINK_TEXT, lc.header_Plinktxt).is_displayed()
        context.driver.find_element(By.ID, lc.filterbyName_textfield_Id).is_displayed()
        context.driver.find_element(By.ID, lc.filerbyName_button_Id).is_displayed()
        context.driver.find_element(By.ID, lc.add_new_computer_Id)
        assert context.driver.find_element(By.LINK_TEXT, lc.computername_linktxt).text == computer_name
        assert context.driver.find_element(By.LINK_TEXT, lc.Introduced_linktxt).text == Introduced_Date
        assert context.driver.find_element(By.LINK_TEXT, lc.Discontinued_linktxt).text == Discontinued_Date
        assert context.driver.find_element(By.LINK_TEXT, lc.company_linktxt).text == Manufacturer

    # select computer from the table and click on the computer name to open Edit computer page
    def select_computer(context, computer_name):
        table = context.driver.find_element(By.XPATH, lc.table_xpath)
        rows = table.find_elements(By.TAG_NAME, lc.row_tag_name)
        for row in rows:
            if row.find_elements(By.TAG_NAME, "td")[0].text == computer_name:
                row.find_element(By.PARTIAL_LINK_TEXT, computer_name).click()
                break

    # Update the company name for the selected computer, since its a drop down used Select class methods
    # Using select class method we can select the element from drop down by value, index or visible text
    def change_company(context, company_name):
        Select(context.driver.find_element(By.ID, lc.company_dropdown_Id)).select_by_visible_text(company_name)

    # Save the update
    def click_save_button(context):
        context.driver.find_element(By.XPATH, lc.save_button_xpath).click()

    # Verify the update is reflected in the list
    def verify_companyName(context, company_name, computer_name):
        table = context.driver.find_element(By.XPATH, lc.table_xpath)
        rows = table.find_elements(By.TAG_NAME, lc.row_tag_name)
        for row in rows:
            if row.find_elements(By.TAG_NAME, "td")[0].text == computer_name:
                assert row.find_elements(By.TAG_NAME, "td")[3].text == company_name
