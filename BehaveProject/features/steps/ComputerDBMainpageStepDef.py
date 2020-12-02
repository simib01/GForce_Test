from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators.locatorRepo import locatorRepo as lc
from selenium.webdriver.support.ui import Select
import time

#defined variable to valide the label. Defined here separatley instead of hardcode inside the test step because
# these labels may change later on so we only to modify here without touching the code
computer_name ="Computer name"
Introduced_Date = "Introduced"
Discontinued_Date = "Discontinued"
Manufacturer = "Company"

#launch chrome browser and maximize window
@given('Launch chrome browser')
def launch_browser(context):
    context.driver=webdriver.Chrome()
    context.driver.maximize_window()

#launch the application
@when(u'open Computer Database homepage')
def homepage(context):
    context.driver.get("http://computer-database.herokuapp.com/computers")
    context.driver.implicitly_wait(1)

#verify the UI elements in main page
@then(u'verify that the homepage UI elements')
def verify_homepage(context):
    context.driver.find_element(By.PARTIAL_LINK_TEXT,lc.header_Plinktxt).is_displayed()
    context.driver.find_element(By.ID,lc.filterbyName_textfield_Id).is_displayed()
    context.driver.find_element(By.ID,lc.filerbyName_button_Id).is_displayed()
    context.driver.find_element(By.ID,lc.add_new_computer_Id)
    assert context.driver.find_element(By.LINK_TEXT,lc.computername_linktxt).text == computer_name
    assert context.driver.find_element(By.LINK_TEXT, lc.Introduced_linktxt).text == Introduced_Date
    assert context.driver.find_element(By.LINK_TEXT, lc.Discontinued_linktxt).text == Discontinued_Date
    assert context.driver.find_element(By.LINK_TEXT, lc.company_linktxt).text == Manufacturer

#select computer from the table and click on the computer name to open Edit computer page
@then(u'Select "{computer_name}" computer from the list')
def select_computer(context,computer_name):
   table = context.driver.find_element(By.XPATH,lc.table_xpath)
   rows = table.find_elements(By.TAG_NAME,lc.row_tag_name)
   for row in rows:
       if row.find_elements(By.TAG_NAME, "td")[0].text == computer_name:
           row.find_element(By.PARTIAL_LINK_TEXT,computer_name).click()
           break

#Update the company name for the selected computer, since its a drop down used Select class methods
#Using select class method we can select the element from drop down by value, index or visible text
@then(u'I change company name by "{company_name}"')
def change_company(context,company_name):
    Select(context.driver.find_element(By.ID, lc.company_dropdown_Id)).select_by_visible_text(company_name)

#Save the update
@step(u'I Click Save this computer')
def click_save_button(context):
    context.driver.find_element(By.XPATH, lc.save_button_xpath).click()
    time.sleep(2)

#Verify the update is reflected in the list
@then('I verify company name is updated as "{company_name}" for computer "{computer_name}"')
def verify_companyName(context,company_name,computer_name):
    table = context.driver.find_element(By.XPATH, lc.table_xpath)
    rows = table.find_elements(By.TAG_NAME, lc.row_tag_name)
    for row in rows:
        if row.find_elements(By.TAG_NAME, "td")[0].text == computer_name:
            assert row.find_elements(By.TAG_NAME, "td")[3].text == company_name

#close browser
@step(u'close browser')
def close_browser(context):
    context.driver.quit()



