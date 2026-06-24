n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
symbol = input("What you do(/,+,-,*,):")

if symbol=="/":
    if n2 == 0:
        print("Cannot divide by zero")
    else:
        print(f"Result:{n1/n2}")

elif symbol=="+":
    print(f"Result:{n1+n2}")

elif symbol=="-":
    print(f"Result:{n1-n2}")

elif symbol=="*":
    print(f"Result:{n1*n2}")
