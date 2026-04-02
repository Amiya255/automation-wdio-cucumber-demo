import sys
import getpass


PIN = '0123'
LIMIT = 4

for tries in range(1,LIMIT):
    supplied_pin = getpass.getpass("Enter your PIN:")
    if supplied_pin == PIN:
        print('Well done, you remembered it!')
        print('..and after only', tries , 'attempts')
        break
    else:
        print('You had', tries,'tries and failed!')
