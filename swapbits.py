def totalFlips(number1, number2):
    flips = 0

    while(number1 > 0 or number2 > 0):
        n1 = (number1 & 1)
        n2 = (number2 & 2)
        if(n1 != n2):
           flips += 1

        number1 >>= 1
        number2 >>= 1

    return flips

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
print("The total number of bits to be flipped required")
print(totalFlips(num1, num2))