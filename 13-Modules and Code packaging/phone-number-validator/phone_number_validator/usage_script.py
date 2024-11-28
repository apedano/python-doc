from phone_number_validator.validator import PhoneNumberValidator

def execute():
    """
            The key can be retrieved from https://app.numlookupapi.com/dashboard
            after the account activation
            Args:
                api_key (str): Your API key for the NumLookupAPI.
            """
    validator = PhoneNumberValidator(api_key="num_live_HZDprfkBzgikIUnTOagz9i9KHYPSMZvHhhwnllDF")
    is_valid1 = validator.validate("+15551234")
    is_valid2= validator.validate("+12069220880")
    is_valid3= validator.validate("2069220880", country_code="US")
    print(is_valid1) #expeted False
    print(is_valid2) #expeted True
    print(is_valid3) #expeted True