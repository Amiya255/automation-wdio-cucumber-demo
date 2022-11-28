import { Given, When, Then } from "@wdio/cucumber-framework";
import chai from "chai";

Then(/^Result Items should have Serch Item/, async function () {
  const searchCauseResult = await $$(
    'div[data-testid="cause_details"] p[data-testid="title"]'
  );
  console.log("Result List length", searchCauseResult.length);
  console.log("Selected Cause ", this.selectedCause);
  for (let i = 0; i < searchCauseResult.length; i++) {
    console.log(
      "Search Cause Result ",
      i,
      await searchCauseResult[i].getText()
    );
    expect(searchCauseResult[i]).toHaveTextContaining(this.selectedCause, {
      ignoreCase: true,
    });
    //  chai.expect(searchCauseResult)
  }
});
