import { setWorldConstructor } from "@wdio/cucumber-framework";
import chai from "chai";

class CustomWorld {
  selectedCause: string;
  constructor() {
    this.selectedCause = "";
  }
}

setWorldConstructor(CustomWorld);
