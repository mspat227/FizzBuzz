'''
print integers one to N, but print'Fizz' if an integer is divisible by three,
'Buzz' if integer divisible by five, and 'FizzBuzz' if integer is divisible by both
three and five
'''
#get the number from the user and raise error if value not a int
try:
    n = int(input("Number: ").strip())

except ValueError:
    print("Value is not an integer")

#loop through numbers till n starting from one 
for i in range(1, n + 1, 1):
    #if number divide by three 
    if i % 3 == 0:
        #and same number divide by five too
        if i % 5 == 0:
            print(f"[{i}] FizzBuzz")
        else:
            print(f"[{i}] Buzz")
    elif i % 5 == 0:
        print(f"[{i}] Fizz")
    else:
        print(f"[{i}] {i}")
        
#this is Fizz buzz to use as a interview problem set as junior level

