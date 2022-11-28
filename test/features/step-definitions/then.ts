import { Given, When, Then } from "@wdio/cucumber-framework";
import chai from "chai";
import SearchCausePage from '../../page-objects/search-cause-page';

Then(/^Result Items should have Search Item/, async function () {  
  
  //const searchCauseResult = await SearchCausePage.searchCauseResult;
  const searchCauseResult = await $$('div[data-testid="cause_details"] p[data-testid="title"]' ); 
  
  for (let i = 0; i < searchCauseResult.length; i++) {   
    expect(searchCauseResult[i]).toHaveTextContaining(this.selectedCause, { ignoreCase: true });    
  }
});
