from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators.Locators import locator as lc
from selenium.webdriver.support.ui import Select
import time


class AddNewComputerPage():
    def __init__(self,driver):
        self.driver = driver

    # Click Add a new Computer button
    def click_Add_new_computer(context):
        context.driver.find_element(By.ID,lc.add_new_computer_Id).click()
        #sleep is introduced to give some time to launch the Add new computer page and all the UI elements are loaded
        time.sleep(2)

    # Verify all the UI elements is as per requirement
    def verify_addNewComputerUI(context):
        assert context.driver.find_element(By.XPATH,lc.heading_label_xpath).text == "Add a New Computer"
        assert context.driver.find_element(By.XPATH,lc.computername_label_xpath).text == "Computer Name"
        assert context.driver.find_element(By.ID,lc.computername_textfield_id).get_attribute("type") == "text"
        assert context.driver.find_element(By.XPATH, lc.introduced_label_xpath).text == "Introduced Date"
        assert context.driver.find_element(By.ID, lc.intro_date_textfield_id).get_attribute("type") == "text"
        assert context.driver.find_element(By.XPATH, lc.discont_date_label_xpath).text == "Discontinued Date"
        assert context.driver.find_element(By.ID, lc.discont_textfield_id).get_attribute("type") == "text"
        assert context.driver.find_element(By.XPATH, lc.company_label_xpath).text == "Manufacturer"
        assert context.driver.find_element(By.ID, lc.company_dropdown_Id).get_attribute("type") == "text"
        assert context.driver.find_element(By.XPATH,lc.addComputer_button_xpath).text == "Add Computer"
        assert context.driver.find_element(By.XPATH,lc.cancel_button_xpath).text == "Cancel"

    # Enter Computer Name
    def Enter_computerName(context,ComputerName):
        context.driver.find_element(By.ID,lc.computername_textfield_id).send_keys(ComputerName)

    # Enter Introduced Date
    def Enter_IntroducedDate(context,IntroducedDate):
        context.driver.find_element(By.ID,lc.intro_date_textfield_id).send_keys(IntroducedDate)

    # Enter Discontinued Date
    def Enter_DiscontinuedDate(context,DiscontinuedDate):
        context.driver.find_element(By.ID,lc.discont_textfield_id).send_keys(DiscontinuedDate)

    # Enter Manufacturer name
    # Manufacturer is not free input/text field as per requirement
    def Enter_Manufacturer(context,Manufacturer):
        Select(context.driver.find_element(By.ID, lc.company_dropdown_Id)).select_by_visible_text(Manufacturer)

    def click_Add_computer(context):
        context.driver.find_element(By.XPATH,lc.addComputer_button_xpath).click()
        context.driver.implicitly_wait(3)

    # validate the computername is added to app
    # In table the code checks for the all the values in the 1st column if there is matching name it wll return True
    def verify_computer_add(context,ComputerName):
        table = context.driver.find_element(By.XPATH, lc.table_xpath)
        rows = table.find_elements(By.TAG_NAME, lc.row_tag_name)
        for row in rows:
            if row.find_elements(By.TAG_NAME, "td")[0].text == ComputerName:
                 assert True

    # delete the newly added computer to avoid repetition
    def delete_computer(context,ComputerName):
        context.driver.find_element(By.PARTIAL_LINK_TEXT, ComputerName).click()
        context.driver.find_element(By.XPATH,lc.delete_button_xpath).click()
        time.sleep(2)


