'''
print integers one to N, but print'Fizz' if an integer is divisible by three,
'Buzz' if integer divisible by five, and 'FizzBuzz' if integer is divisible by both
three and five
'''

try:
    n = int(input("Number: ").strip())

except ValueError:
    print("Value is not an integer")


for i in range(1, n + 1, 1):
    if i % 3 == 0:
        if i % 5 == 0:
            print(f"[{i}] FizzBuzz")
        else:
            print(f"[{i}] Buzz")
    elif i % 5 == 0:
        print(f"[{i}] Fizz")
    else:
        print(f"[{i}] {i}")

