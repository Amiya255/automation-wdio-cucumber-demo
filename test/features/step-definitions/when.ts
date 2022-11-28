import { Given, When, Then } from "@wdio/cucumber-framework";
import chai from "chai";
import HomePage from '../../page-objects/home-page';
import SupportCausePage from '../../page-objects/support-cause-page';
import SearchCausePage from '../../page-objects/search-cause-page';

When(/^Click on Find A Cause/, async function () {
 
  // await HomePage.findACauseLink.click();
  //Click on Seach Cause link
  let ele = await $('div[data-testid="header-link"]:nth-child(2)');
  ele.click();
});

When(/^Type(.*) in SeachCause Input/, async function (searchItem) {
  
  //Search cause , n digit letter as input   
  //const searchCause = await SupportCausePage.searchCauseLink;
  let ele = await $("#sagc-hero-search-input");
  ele.setValue(searchItem);
  //wait time for options to appear
  await browser.pause(5000);
  this.searchItem = searchItem;
});

When(/^Select nth (.*) item from the suggestions/,async function (suggestionNum) {

  //Get all suggestions
  //const causeSuggestionList = await SupportCausePage.searchSuggestions;  
    let causeSuggestionList = await $$("#sagc-hero-search-input-auto-suggest > li > button:first-child");

    //validate if there are atleast n suggestions to pick from
    suggestionNum = parseInt(suggestionNum);
    expect(causeSuggestionList.length).toBeGreaterThanOrEqual(suggestionNum);

    //Selected the nth suggested option
    const selectedCause = await causeSuggestionList[suggestionNum - 1 ].getText();

    let ele = await $("#sagc-hero-search-input");
    //await ele.clearValue();
    //clearValue is not working as expected, hence using backSpaces to clear the input box

    const backSpaces = new Array(this.searchItem.length).fill("Backspace");

    await ele.setValue(backSpaces);
    ele.setValue(selectedCause);

    this.selectedCause = selectedCause;
  }
);

When(/^Click SearchCause Button/, async function () {
  let ele = await $("#sagc-hero-search-submit");
  await ele.click();
});
