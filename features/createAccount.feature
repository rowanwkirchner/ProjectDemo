@CreateAccount

Feature: CreateAccount

  Scenario Outline: Create account process
    Given the "HomePageObject" page is open
    And the user sets the "text" value of element "create_email" to "<email_input>"
    And the user clicks the "create_button" where "class" has a value of "btn btn-default button button-medium exclusive"

    Given the "CreateAccountPageObject" page is open
    And the user clicks the "mrs_radio_btn" where "class" has a value of "radio"
    And the user sets the "text" value of element "firstname" to "<firstname_input>"
    And the user sets the "text" value of element "lastname" to "<lastname_input>"
    #And the user sets the "text" value of element "email" to "<email1_input>"
    And the user sets the "text" value of element "password" to "<password_input>"

    #And the user selects the value "<state>" from the "address_state" list

    #And the user selects the value "<state>" from the "button_select" list

    #And the user sets the "text" value of element "address_firstname" to "<firstname_input>"
    #And the user sets the "text" value of element "address_lastname" to "<lastname_input>"
    And the user sets the "text" value of element "address_company" to "<company_input>"
    And the user sets the "text" value of element "address" to "<address_input>"
    And the user sets the "text" value of element "address_line2" to "<address_line2_input>"
    And the user sets the "text" value of element "address_city" to "<city_input>"
    #And the user clicks the "button_select_state" where "class" has a value of "selector"
    And the user clicks the "button_select" where "id" has a value of "uniform-id_state"
    And the user sets the "text" value of element "address_zip" to "<zip_input>"

    And the user clicks the "address_country" where "id" has a value of "uniform-id_country"
    #And the user selects the value "<country>" from the "address_country" list
    And the user sets the "text" value of element "address_mobile_number" to "<mobile_input>"
    #And the user sets the "text" value of element "address_used" to "<email_input>"
    And the user clicks the "register_button" where "class" has a value of "btn btn-default button button-medium"



Examples:
    | email_input                   |firstname_input| lastname_input | password_input  | company_input | address_input    | address_line2_input | city_input | zip_input |country             | mobile_input |
    |  mpLwando@gmail.com           |Sinazo         | Hlalele        | sinawo#         | Kineticskunk  | groove building  | claremont           | Cape town  | 10001     | United state       |0732027291    |
