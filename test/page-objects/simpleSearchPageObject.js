class SimpleSearchPage {
  open() {
    return browser.url("https://www.easyfundraising.org.uk/");        
  }
 

  get findACauseLink() {
    return $("a[href='/support-a-good-cause/']");
  }

  get searchCauseLink() {
    return $("#sagc-hero-search-input");
  }

  get searchSuggestions() {
    return $$("#sagc-hero-search-input-auto-suggest > li > button:first-child");
  }

  get submitSearchCauseLink() {
    return $("#sagc-hero-search-submit");
  }

  get searchCauseResult() {
    return $$('div[data-testid="cause_details"] p[data-testid="title"]');
  }
}

module.exports = new SimpleSearchPage();
