class ObjectRepository(object):
    # LAUNCH PAGE
    SELECT_COUNTRY_CURRENCY_BY_ID = "customerCurrency"
    LINK_REGISTER_BY_LINKTEXT = "Register"
    TXT_SEARCH_ITEM_BY_ID = "small-searchterms"
    BUTTON_SEARCH_ITEM_BY_CSS = ".search-box-button"

    # REGISTER PAGE
    RADIO_GENDERS_BY_CSS = ".forcheckbox"
    TXT_FIRSTNAME_BY_ID = "FirstName"
    TXT_LASTNAME_BY_ID = "LastName"
    SELECT_DAY_BY_NAME = "DateOfBirthDay"
    SELECT_MONTH_BY_NAME = "DateOfBirthMonth"
    SELECT_YEAR_BY_NAME = "DateOfBirthYear"
    TXT_EMAIL_BY_ID = "Email"
    CHECKBOX_NEWSLETTER_BY_ID = "Newsletter"
    TXT_PASSWORD_BY_ID = "Password"
    TXT_CONFIRM_PASSWORD_BY_ID = "ConfirmPassword"
    BUTTON_REGISTER_BY_ID = "register-button"
    LABEL_REGISTRATION_SUCCESS_BY_CSS = ".page-body .result"
    BUTTON_REGISTER_CONTINUE_BY_CSS = ".register-continue-button"

    # SEARCH PAGE
    LABEL_SEARCH_ITEMS_BY_XPATH = "//div[@class='search-results']//h2/a"
    LABEL_NO_SEARCH_ITEMS_BY_CSS = ".no-result"
