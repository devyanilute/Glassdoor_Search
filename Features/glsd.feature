Feature: Search
  Scenario: Verify that user is able to login and search
    Given Open the browser and enter valid URL and click on continue with email
    And Enter the password and click on signin
    Then Enter the text in search textfield
    And Click on search button1
    Then Click on list search bar9
    And Select the job option
    And Click on search button2
    And Navigate to back page01
    Then Click on list search bar8
    And select the companies option
    And Click on search button3
    And Navigate to back page02
    Then Click on list search bar7
    And Select the salaries option
    And Click on search button4
    And Navigate to back page03
    Then Click on list search bar6
    And Select the interviews option
    And Click on search button5
    And Navigate to back page04
    Then Click on Location bar
    And Enter the location
    Then Click on search button6
    And Close the browser
