from doctest import testmod


def add(num1,num2):
    """This function adds two numbers
    >>>add(2,4)

     >>>add(0,-3)

    """
    return num1 + num2

if __name__ == "__main__":
    import doctest
    doctest,testmod()
