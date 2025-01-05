def currency_converter(from_currency, to_currency, amount):
    exchange_rate = {
        'USD_TO_INR': 74.50,
        'INR_TO_USD': 0.013,
        'USD_TO_EUR': 0.85,
        'EUR_TO_USD': 1.18,
        'USD_TO_GBP': 0.75,
        'GBP_TO_USD': 1.33,
        'EUR_TO_GBP': 0.88,
        'GBP_TO_EUR': 1.14
    }
    
    # Normalize currency codes to uppercase
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    
    # Validate amount
    if amount < 0:
        return None, "Amount must be a positive number."
    
    # Construct conversion key
    conversion_key = f'{from_currency}_TO_{to_currency}'
    print(f"Constructed conversion key: {conversion_key}")

    # Perform conversion
    if conversion_key in exchange_rate:
        converted_amount = amount * exchange_rate[conversion_key]
        return converted_amount, None  # No error message
    else:
        return None, f'Sorry, conversion from {from_currency} to {to_currency} is not supported.'