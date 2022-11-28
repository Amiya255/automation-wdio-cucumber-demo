import { Given, When, Then } from "@wdio/cucumber-framework";
import chai from "chai";
import HomePage from '../../page-objects/home-page';

Given(/^Home Page is opened$/, async function () {
  await browser.url("https://www.easyfundraising.org.uk");
  //await HomePage.open;
  console.log("Opened Browser successfully");
  await browser.pause(2000);
});
