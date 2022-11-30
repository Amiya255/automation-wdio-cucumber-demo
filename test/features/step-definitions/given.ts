import { Given} from "@wdio/cucumber-framework";
import HomePage from '../../page-objects/home-page';

Given(/^The user is on the Home Page/, async function () {
   await HomePage.open(); 
});
