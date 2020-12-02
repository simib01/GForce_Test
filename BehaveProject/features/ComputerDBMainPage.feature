#python version - 3.7
#selenium version 3.141
#IDE PyCharm Community Edition 2019.1.1
#command to run ComputerDBMainPage.feature "behave features\ComputerDBMainPage.feature"  in BehaveProject directory
#command to run ComputerDBMainPage.feature "behave features\AddNewComputer.feature"  in BehaveProject directory
#command to run all feature files "behave features\

Feature: Computer Database app Main page

#Common Steps that need to executed for all the scenarios
  Background:common steps
    Given Launch chrome browser
    When open Computer Database homepage

 #Verify Computer Database Mainpage
  Scenario: Computer Database browser based app is launched and verify the main page
    Then verify that the homepage UI elements
    And close browser

  #Update the company name for a selected computer and validate the same
  Scenario: Udapte existing computer details
    Then Select "ACE" computer from the list
    Then I change company name by "IBM"
    And I Click Save this computer
    Then I verify company name is updated as "IBM" for computer "ACE"
    And close browser

