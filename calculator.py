numbers = []
cont = "yes"
print("welcome to the calc: ")
print(" _____________________")
print("|  _________________  |")
print("| | JO           0. | |")
print("| |_________________| |")
print("|  ___ ___ ___   ___  |")
print("| | 7 | 8 | 9 | | + | |")
print("| |___|___|___| |___| |")
print("| | 4 | 5 | 6 | | - | |")
print("| |___|___|___| |___| |")
print("| | 1 | 2 | 3 | | x | |")
print("| |___|___|___| |___| |")
print("| | . | 0 | = | | / | |")
print("| |___|___|___| |___| |")
print("|_____________________|")
op = input("What operation would you like to do? ") 
while cont == "yes":
    numbers.append(int(input("what is the next number? ")))
    cont = input("yes or no, would you like to calculate more numbers? ")
if op == "add":
    sums = 0
    for i in numbers:
        sums += i
    print(sums)
if op == "multiply":
    mult = 1
    for i in numbers:
        mult *= i
    print(mult)
if op == "subtract":
    sub = numbers[0]
    for i in range(1,len(numbers)):
        sub -= numbers[i]
    print(sub)
if op == "divide":
    div = numbers[0]
    for i in range(1,len(numbers)):
        div /= numbers[i]
    print(div)
if op == "exponents":
    exp = numbers[0]
    for i in range(1,len(numbers)):
        exp **= numbers[i]
    print(exp)
print(numbers)