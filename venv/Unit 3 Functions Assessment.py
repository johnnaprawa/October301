import random
#  Task 1
def doubleeven(n):
    if (n % 2) == 0:
        n = n *2
        return(n)
    else:
        return(-1)
print(doubleeven(5))

#  Task 2
def grade(percent):
    if percent >= 60 and percent <= 69:
        return("You have a C")
    if percent >= 70 and percent <= 79:
        return("You have a B")
    if percent >= 80:
        return("YOU HAVE AN A")
print(grade(82))

#  Task 3
def largestNum(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return(num1)
    elif (num2 >= num1) and (num2 >= num3):
        return(num2)
    else:
        return(num3)
print(largestNum(8,9,10))

#  Task 4
Dice = int(input("how many sides are on your die?"))
NumRolls = int(input("how many times would you like to roll"))
def sumDice(Dice, NumRolls):
    Sumrolls = 0
    for x in range(NumRolls):
        Sumrolls = Sumrolls + random.randint(1,Dice)
    return Sumrolls

print(sumDice(Dice,NumRolls))