class SupportCausePage {
  get searchCauseLink() {
    return $("#sagc-hero-search-input");
  }

  get searchSuggestions() {
    return $$("#sagc-hero-search-input-auto-suggest > li > button:first-child");
  }

  get submitSearchCauseLink() {
    return $("#sagc-hero-search-input");
  }
}

export default new SupportCausePage();