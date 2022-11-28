Feature: Search Cause

    @findACause
    Scenario Outline: Cause Search Functionality
        Given Home Page is opened
        When Click on Find A Cause
        And Type <SearchItem> in SeachCause Input
        And Select nth <SuggestionNum> item from the suggestions
        And Click SearchCause Button
        Then Result Items should have Search Item

        Examples:
            | TestID      | SearchItem | SuggestionNum |
            | Demo_TC001  |    can     |      3        |
            | Demo_TC001  |    abc     |      4        |
            | Demo_TC001  |    child   |      2        |