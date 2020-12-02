Feature: Add new Computer to Computer Database app

#Common Steps that need to executed for all the scenarios
  Background:common steps
    Given Launch chrome browser
    When open Computer Database homepage

# this scenario outline adds details of 2 computer to app, verifies whether its added successfully and delete it
  Scenario Outline: Add a new computer in app
    Then I click Add new computer button
    When I enter <ComputerName> as Name
    Then I enter <IntroducedDate> as Introduced Date
    Then I enter <DiscontinuedDate> as Discontinued date
    And I enter <Manufacturer> as Manufacturer
    And Click Add computer button
    Then I verify that computer <ComputerName> is added
    Then I delete <ComputerName> from the app
    And close browser
    Examples:
    | ComputerName | IntroducedDate | DiscontinuedDate | Manufacturer |
    | "ABC1"       | "1985-12-01"   | "2025-12-01"     |  "RCA"       |
    | "ABC2"       | "1991-11-30"   | "2030-10-20"     |  "Sony"      |

  #Validates the UI of Add new computer page, since fails because UI is not as per requirement
  Scenario: Add new computer UI validation
    Then I click Add new computer button
    Then I verify Add a computer page UI
    And close browser