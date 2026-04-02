'''Function1'''
def my_func(val,lista=[]):
    lista.append(val)
    print("value of lista is:",lista)
    return
my_func(42)
my_func(41)
my_func(40)


def my_func2(val,lista=None):
    if lista == None:
        lista = []
    lista.append(val)
    print("value of lista is:",lista)
    return
my_func2(42)
my_func2(41)
my_func2(40)