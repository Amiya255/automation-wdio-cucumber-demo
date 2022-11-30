import { When } from "@wdio/cucumber-framework";
import HomePage from '../../page-objects/home-page';
import SupportCausePage from '../../page-objects/support-cause-page';


When(/^The user clicks the link 'Find A Cause'/, async function () {

  await HomePage.findACauseLink.click();

});

When(/^The user types(.*) in SeachCause Input/, async function (searchItem) {

  //Search cause , n digit letter as input   
  const searchCause = await SupportCausePage.searchCauseLink;
  searchCause.setValue(searchItem);
  //wait time for options to appear
  await browser.pause(5000);
  this.searchItem = searchItem;
});

When(/^The user selects the nth (.*) item from the suggestions/, async function (suggestionNum) {

  //Get all suggestions
  const causeSuggestionList = await SupportCausePage.searchSuggestions;
  suggestionNum = parseInt(suggestionNum);
  expect(causeSuggestionList.length).toBeGreaterThanOrEqual(suggestionNum);

  //Selected the nth suggested option
  const selectedCause = await causeSuggestionList[suggestionNum - 1].getText();

  const searchCause = await SupportCausePage.searchCauseLink;
  const backSpaces = new Array(this.searchItem.length).fill("Backspace");

  await searchCause.setValue(backSpaces);
  searchCause.setValue(selectedCause);

  this.selectedCause = selectedCause;
});

When(/^The user clicks the SearchCause Button/, async function () {

  //Click Search
  await SupportCausePage.submitSearchCauseLink.click();

  });
