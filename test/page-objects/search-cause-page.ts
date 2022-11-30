class SearchCausePage {
  get searchCauseResult() {
    return $$('div[data-testid="cause_details"] p[data-testid="title"]');
  }
}

export default new SearchCausePage();
