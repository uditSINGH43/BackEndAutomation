
Feature: Github API Validation
  # Enter feature description here

  Scenario: Session management check
  Given I have github auth credentials
  When i hit getRepo API of github
  Then status code of response should be 200
    # Enter steps here