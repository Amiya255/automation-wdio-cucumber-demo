from example_function import calculate_vat, print_my_name , calculate_vat2

print(__name__)
print_my_name()

price = 29.99
result = calculate_vat()

print(f'The gross price of £{price} is a net price of £{result[0]} and VAT of £{result[1]}')

price = 72.95
net, vat = calculate_vat(price)

print(f'The gross price of £{price} is a net price of £{net} and VAT of £{vat}')


help(example_function)
help(calculate_vat)
help(calculate_vat2)