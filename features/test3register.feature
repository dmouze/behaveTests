Feature: User Registration

  Scenario Outline: User registers with success
    Given I am on the registration page in Super APP
    When I register with email "<email>" and password "<password>"
    Then The registration is successful

    Examples:
      | email             | password |
      | eve.holt@reqres.in| pistol   |
