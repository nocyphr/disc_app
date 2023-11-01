Feature: display_question

  In order to be able to answer my assessment
  As an applicant
  I want to see a multiple choice question
 
  Contributes to questionaire.keyfeature

  Scenario Outline: I see a multiple choice question
    Given the url 'http://localhost:8501/'
    When I visit the url
    Then the element <element> with text <text> is found

    Examples: 
    | element | text                            |
    | h2      | When faced with a challenge, I: |   