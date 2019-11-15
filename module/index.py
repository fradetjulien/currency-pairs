import click
import pycountry
from forex_python.converter import CurrencyRates

def is_currency_code(currency_codes):
    currency_code_list = []
    for item in list(pycountry.currencies):
        currency_code_list.append(str(item).split(',')[0][-4:-1])
    for currency_code in currency_codes:
        if currency_code not in currency_code_list:
            print("Insert a correct currency code please.")
            return False
    return True

def find_conversion_rate(currency_codes):
    
    return

@click.group()
def cli():
    '''
    '''

@cli.command('convert')
@click.argument('currency_codes', nargs=-1)
def convert_currencies(currency_codes):
    if is_currency_code(currency_codes):
        find_conversion_rate(currency_codes)
        return

if __name__ == '__main__':
    cli()