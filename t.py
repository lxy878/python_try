import math as ma
# Print out format with variables by using f"{VARIABLE}"
##word = "World"
##print(f"Hello, {word}")

# Typecasting int(), str(), float(), bool()
##integer = 5
##double = 2.1
##boolean = False
##string = "Hi"
##print(bool(integer))

# input()
##data = input("Enter:")
##print("Input is", data)

# Math functions round(), abs(), pow() and import math
##double = 2.6
##print(round(double)) # 3
##print(ma.floor(double))

# If..elif..else
##input_str=input("Enter a number:")
##try:
##    number = int(input_str) # also use str.isdigit()
##    if number>0:
##        print("Positive")
##    elif number==0:
##        print("Zero")
##    else:
##        print("Negative")
##except ValueError:
##    print("Input is Not a Number")

# useful functions:
# len()
# str.find() -- find the index of first character on the targeted substring
##print("name of someone".find("name"))
# str.rfind() -- find in reverse order
# str.capitalize()
# str.upper() && str.lower()
# str.isdigit()
# str.isalpha() -- check if full alphas in the string
# str.count('') -- count the targeted characters
# str.replace(target, replace)
# help(str) -- show all functions of string

##username= input("enter a name:")
##if len(username)>12 or len(username)<1:
##    print("name is empty or is greater than 12")
##elif username.find(" ")>=0:
##    print("name has spaces")
##elif not username.isalpha():
##    print("name has numbers")
##else:
##    print(f"entered name is {username}")
    
# indexing str[start:end:step] step: continuously collect different characters follow steps

# format spacifier(number only): {value:flags} flags are formats insert to the value. flags can be characters, operators or number
##n = -3.1415926
##print(f"{n:.2f}")
##print(f"{n:>12}")
##print(f"{n:10,.5f}")

# while loop

# for loop: range(start,end,step), reversed(), str
##for i in range(1,10):
##    print(i)
##for c in "abc":
##    print(c)

# Countdown
##import time
##try:
##    time_in_sec = int(input("enter a number for sec:"))
##    sleep_speed = int(input("enter a speed for sleep:"))
##    for i in range(time_in_sec,0,-1):
##        sec = i%60
##        min = int(i/60)%60
##        hour = int(i/3600)
##        print(f"{hour:02}:{min:02}:{sec:02}")
##        time.sleep(1/sleep_speed)
##    print("wake up")
##except ValueError:
##    print("input is not number")

# List [], Set {}, Tuple ()- unchangable list but faster.
##list = ['apple','apple', 'pear', 'peach']
##set = set(list)
##print(set)

# 2D
##row = list()
##matr = list()
##for i in range(1,10):
##    row.append(str(i))
##    if i%3==0:
##        matr.append(row)
##        row = list()
##matr.append(['*', '0', '#'])
##print(matr)

# Dictiionary {key:value}, dict.items() = key,value

# Random: guessing number
##import random
##guess_answer = random.randint(1, 100)
##user_guess = 0
##while not user_guess==guess_answer:
##    user_guess = input(f"guess a number between {1} and {100}:")
##    if not user_guess.isdigit():
##        print("Invalid Number");
##        continue
##    user_guess = int(user_guess)
##    if user_guess<1 or user_guess>100:
##        print("Invalid Number");
##        continue
##    if user_guess>guess_answer:
##        print("too high")
##    elif user_guess<guess_answer:
##        print(f"too low, try to guess anther number between {1} and {100}:")
##print("You got it")

# Functions - pass by default, keyword, arbitrary: (*args || **keywordargs)
##def foo1(price, default=0):
##    return price*(1-default)
##print(foo1(10,.2))
##
##def foo2(keyword1, keyword2):
##    print(f"keyword1: {keyword1}, keyword2: {keyword2}")
##foo2(keyword2="abc", keyword1=123)
##
##def foo3(*nums):
##    print(type(nums))
##    for num in nums:
##        print(num)
##foo3(1,2,3,4)
##
##def foo4(**keywordargs):
##    print(type(keywordargs))
##    for kwarg in keywordargs:
##        print(f"key={kwarg}")
##foo4(keyword1="abc", keyword2=123, key3="a1")

# Iterables - example: for n in nums

# Membership operators - in || not in
##def not_contains(n, *nums):
##    return n not in nums
##print(not_contains(-1,1,2,3,4,5))

# List comprehension: [expression FOR value IN iterable IF condition]
##evens = [ n for n in range(1,10) if n%2==0]
##print(evens)

# Match...Case only work >= 3.10
##def check(n):
##    match n:
##        case 1:
##            print(1)
##        case 2:
##            print(2)
##        case _:
##            print("nothing")
##check(3)

# Module - help("MODULE_NAME")/p("MODULE_NAME")
##from math import pi
##import exampleModule as em
##em.printout()

# Variable scope - levels of execution, local, enclosed(=inner functions), global, built-in

# Main program: use __name__, one of dunder functions, as main so the current file can run alone like a main program 
##def show_balance(balance):
##    print(f"Your balance is ${balance:.2f}.")
##
##def deposit():
##    try:
##        return float(input("Enter a number to deposit:"))
##
##    except ValueError:
##        print("The input is not valid to deposit")
##        return 0
##
##def withdraw(balance):
##    try:
##        withdrow = float(input("Enter a number to withdraw:"))
##        if withdrow>balance:
##            print("There are not enough to withdraw")
##            return 0
##        return withdrow
##    except ValueError:
##        print("The input is not valid to withdraw")
##        return 0;
##    pass
##def main():
##    balance = 100.00
##    running = True
##    while running:
##        task = input("Enter d to deposit, w to withdraw, sb to show balance or q to quit:")
##        if task.isdigit():
##            print("Numbers are not valid")
##            continue
##        task = task.lower()
##        if task == 'w':
##            balance-=withdraw(balance)
##        elif task == 'q':
##            running = False
##        elif task == 'd':
##            balance+=deposit()
##        elif task == 'sb':
##            show_balance(balance)
##        else:
##            print("Input is not valid")
##    pass
##if __name__=="__main__":
##    main()



# Python Naming Convention -
# single underscore(_NAME): local use but not inforce ?
# dunder functions(__NAME__): the instences of a class behave in certain situations 
# double usderscore(__NAME): private use inforced ?
