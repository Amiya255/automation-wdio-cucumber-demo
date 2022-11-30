Feature: Search Cause
      The User would like To Search for Causes In Easy Fund Raising Website 

    @findACause
    Scenario Outline: Verify Cause Search
        Given The user is on the Home Page        
        When  The user clicks the link 'Find A Cause'
        And   The user types <SearchItem> in SeachCause Input
        And   The user selects the nth <SuggestionNum> item from the suggestions
        And   The user clicks the SearchCause Button
        Then  The user should see the selected search cause in Search Item

        Examples:
            | TestID      | SearchItem | SuggestionNum |
            | Demo_TC001  |    can     |      3        |
            | Demo_TC002  |    abc     |      4        |
            | Demo_TC003  |    child   |      2        |