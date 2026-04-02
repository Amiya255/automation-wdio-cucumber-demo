var = input("Please enter an integer:")

if var.isdecimal():
    print("Success")
    var = int(var)
else:
    print("Failed")

for i in range(var, -1, -2):
    print(i)

