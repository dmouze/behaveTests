Feature: User Login

  Scenario Outline: User logs in with valid login and password
    Given I am on the login page in Super APP
    When I log in with email "<email>" and password "<password>"
    Then The login is successful

    Examples:
      | email             | password |
      | eve.holt@reqres.in| pistol   |
