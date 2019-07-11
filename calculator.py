numbers = []
cont = "yes"
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
    for i in numbers:
        sub -= (i + 1)
    print(sub)
    
print(numbers)
