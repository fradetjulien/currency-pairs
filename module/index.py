import click
import pycountry
import pandas as pd
from forex_python.converter import CurrencyRates

def is_currency_code(currency_codes):
    '''
    Recover the official list of currency code and then check if the arguments are correct
    '''
    currency_code_list = []
    for item in list(pycountry.currencies):
        currency_code_list.append(str(item).split(',')[0][-4:-1])
    for currency_code in currency_codes:
        if currency_code not in currency_code_list:
            print("Insert a correct currency code please.")
            return False
    return True

def find_conversion_rates(currency_codes):
    '''
    Find and store all conversion rates
    '''
    currency = CurrencyRates()
    arguments_length = len(currency_codes)
    index = 0
    value = []
    conversion_rates = {}
    position = 0
    while position < arguments_length:
        index = 0
        while index < arguments_length:
            value.append(round(float(currency.get_rate(currency_codes[position], currency_codes[index])), 5))
            index = index + 1
        conversion_rates[currency_codes[position]] = value.copy()
        value.clear()
        position = position + 1
    return conversion_rates

def display_rates(conversion_rates, currency_codes):
    '''
    Display a datatable in the CLI showing all conversion rates
    '''
    data_frame = pd.DataFrame(conversion_rates, columns=currency_codes, index=currency_codes, dtype=float)
    print(data_frame)

@click.group()
def cli():
    '''
    Currency Matrix
    '''

@cli.command('convert')
@click.argument('currency_codes', nargs=-1)
def convert_currencies(currency_codes):
    '''
    Display conversion rates of currency codes
    '''
    if is_currency_code(currency_codes):
        conversion_rates = find_conversion_rates(currency_codes)
        display_rates(conversion_rates, currency_codes)

if __name__ == '__main__':
    cli()