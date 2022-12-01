const { Given, When, Then } = require('@wdio/cucumber-framework');
const SimpleSearchPage = require('../../page-objects/simpleSearchPageObject');


Given(/^The user is on the Home Page/, async function () {
    
  await SimpleSearchPage.open();
 
});

When(/^The user clicks the link 'Find A Cause'/, async function () {

  await SimpleSearchPage.findACauseLink.click();

});

When(/^The user types(.*) in SeachCause Input/, async function (searchItem) {

  //Search cause , n digit letter as input   
  const searchCause = await SimpleSearchPage.searchCauseLink;
  searchCause.setValue(searchItem);
  //wait time for options to appear
  await browser.pause(5000);
  this.searchItem = searchItem;
});

When(/^The user selects the nth (.*) item from the suggestions/, async function (suggestionNum) {

  //Get all suggestions
  const causeSuggestionList = await SimpleSearchPage.searchSuggestions;

  suggestionNum = parseInt(suggestionNum);
  //validate if there are atleast n suggestions to pick from 
  expect(causeSuggestionList.length).toBeGreaterThanOrEqual(suggestionNum);

  //Selected the nth suggested option
  const selectedCause = await causeSuggestionList[suggestionNum - 1].getText();
  this.selectedCause = selectedCause;

  await causeSuggestionList[suggestionNum - 1].click();


});

When(/^The user clicks the SearchCause Button/, async function () {

  //Click Search
  await SimpleSearchPage.submitSearchCauseLink.click();

});


Then(/^The user should see the selected search cause in Search Item/, async function () {

  const searchCauseResult = await SimpleSearchPage.searchCauseResult;

  for (let i = 0; i < searchCauseResult.length; i++) {
    expect(searchCauseResult[i]).toHaveTextContaining(this.selectedCause, { ignoreCase: true });
  }
});

