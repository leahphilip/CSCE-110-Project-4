start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
a, b = 0, 1
fibonacci_numbers = []
while a <= end:
    if (
        a >= start
    ):
        fibonacci_numbers.append(a)
    a, b = b, a + b
print(f"The {len(fibonacci_numbers)} Fibonacci numbers between {start} and {end} are:")
for num in fibonacci_numbers:
    print(num, end=" ")
print()
print(60*"*")
