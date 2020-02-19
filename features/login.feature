@Login
Feature: Login

  Scenario Outline:Negative Login process
    Given the "LoginPageObject" page is open
    When the user sets the "text" value of element "email_address" to "<email_input>"
    And the user sets the "text" value of element "password" to "<password_input>"
    And the user clicks the "sign_in_button" where "class" has a value of "button btn btn-default button-medium"
    Then the "sign_in_button" element "ID" has a value of "SubmitLogin"
Examples:
  |               email_input              |      password_input      |
  |               wrongemail               |        74569852          |
  |     rowankirchner@kineticskunk.com     |      wrongpassword       |
  |               wrongemail               |      wrongpassword       |

Scenario Outline:Positive Login process
    Given the "LoginPageObject" page is open
    When the user sets the "text" value of element "email_address" to "<email_input>"
    And the user sets the "text" value of element "password" to "<password_input>"
    And the user clicks the "sign_in_button" where "class" has a value of "button btn btn-default button-medium"
    And the "HomePageObject" page is open
    Then the "search" element "ID" has a value of "search_query_top"


Examples:
  |               email_input              |      password_input      |
  |     rowankirchner@kineticskunk.com     |        74569852          |
