import { setWorldConstructor } from "@wdio/cucumber-framework";

class CustomWorld {
  selectedCause: string;
  SearchItem: string;
  constructor() {
    this.selectedCause = "";
    this.SearchItem = "";
  }
}

setWorldConstructor(CustomWorld);
