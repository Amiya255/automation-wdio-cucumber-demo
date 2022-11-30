import { Then } from "@wdio/cucumber-framework";

import SearchCausePage from '../../page-objects/search-cause-page';

Then(/^The user should see the selected search cause in Search Item/, async function () {  
   
 const searchCauseResult = await SearchCausePage.searchCauseResult;
    
  for (let i = 0; i < searchCauseResult.length; i++) {   
    expect(searchCauseResult[i]).toHaveTextContaining(this.selectedCause, { ignoreCase: true });    
  }
});
