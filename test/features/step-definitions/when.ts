import { Given, When, Then } from "@wdio/cucumber-framework";
import chai from "chai";

When(/^Click on Find A Cause/, async function () {
  let ele = await $('div[data-testid="header-link"]:nth-child(2)');
  ele.click();
});

When(/^Type(.*) in SeachCause Input/, async function (searchItem) {
  let ele = await $("#sagc-hero-search-input");
  ele.setValue(searchItem.trim());
  await browser.pause(5000);
});

When(/^Select nth (.*) item from the suggestions/,async function (suggestionNum) {
    let causeSuggestionList = await $$("#sagc-hero-search-input-auto-suggest > li > button:first-child");

    //validate if there are atleast n suggestions to pick from
    suggestionNum = parseInt(suggestionNum.trim());
    expect(causeSuggestionList.length).toBeGreaterThanOrEqual(suggestionNum);

    //Selected the 3rd suggested option
    const selectedCause = await causeSuggestionList[suggestionNum - 1 ].getText();

    let ele = await $("#sagc-hero-search-input");
    //await ele.clearValue();
    //clearValue is not working as expected, hence using backSpaces to clear the input box

    const backSpaces = new Array(10).fill("Backspace");

    await ele.setValue(backSpaces);
    ele.setValue(selectedCause);

    this.selectedCause = selectedCause;
  }
);

When(/^Click SearchCause Button/, async function () {
  let ele = await $("#sagc-hero-search-submit");
  await ele.click();
});
