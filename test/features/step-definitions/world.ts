import { setWorldConstructor } from "@wdio/cucumber-framework";
import chai from "chai";

class CustomWorld {
  selectedCause: string;
  searchItem: string;
  constructor() {
    this.selectedCause = "";
    this.searchItem = "";
  }
}

setWorldConstructor(CustomWorld);
