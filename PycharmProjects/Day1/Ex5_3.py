import random

lotto = set()

while len(lotto)<6:
    num=random.randint(1,50)
    lotto.add(num)

print("Lottery numbers =",lotto)