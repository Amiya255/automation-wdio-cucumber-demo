"""
This module provids
"""


def calculate_vat(gross, vat_percentage=20):
    """
    This function uses a default vat % of 20%
    """

    net = gross/(1+(vat_percentage/100))
    vat = gross - net
    return [f'{net:05.2f}', f'{vat:05.2f}']


def calculate_vat2(gross: 'float', vat_percentage: 'float' = 20) -> 'list':
    """
Gross SHould be a float
vat_percentage should be float
     """
    net = gross/(1+(vat_percentage/100))
    vat = gross - net
    return [f'{net:05.2f}', f'{vat:05.2f}']

def calculate_vat3(gross, *, vat_percentage= 20, message = 'sumary') -> 'list':
    """
this function uses a default vat % of 20%
message
     """
    net = gross/(1+(vat_percentage/100))
    vat = gross - net
    return [f'{net:05.2f}', f'{vat:05.2f}']


def print_my_name():
    print(f'I a example_functon.py and my name is {__name__}')

def main():
    result = calculate_vat(27.80)
    print(result)

    print(calculate_vat(50))
    print(calculate_vat(120))
    calculate_vat2(20,17.5)
    #print(n,v)
    print(calculate_vat3(100))
    print(calculate_vat3(gross=120, message='Info', vat_percentage=10))

if __name__ == "__main__":
    print(__name__)
    main()