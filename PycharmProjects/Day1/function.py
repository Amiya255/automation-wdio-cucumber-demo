# create funcion

def say_hello():
    print('#'*30)
    print("Hello World!")
    print("Bonjour")
    print("Happy April Fools Day!!")


def say_hello_return_greeting(name):
    msg = f"Welcome {name}. How are you today?"
    return msg

#call the function
say_hello()
# say_hello()
# say_hello()

message = say_hello_return_greeting("Amiya")
print(message)
print(message.upper())

print(say_hello_return_greeting("Bob"))

name = "Charlie"
print(say_hello_return_greeting(name))