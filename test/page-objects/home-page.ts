class HomePage {
    open() {
        return browser.url('https://www.easyfundraising.org.uk/');
    }

    get findACauseLink() {
        return $('div[data-testid="header-link"]:nth-child(2)');
        
    }
}

export default new HomePage();