# 1. Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits in all numbers from 1 to n.
#Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15



# O(n)
n = int(input('Enter a number: '))

result = 0

for number in range(1, n+1):
    result += number

print(result)

# 2. Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.

# O(1)
a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))

if a > b and a > c:
    print('a is the greatest')

elif b > a and b > c:
    print('b is the greatest')

else:
    print('c is the greatest')


# 3. Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

# O(n)
number = input('Enter an number: ')

odd_numbers = 0
even_numbers = 0


for (digit) in number:
    if int(digit) % 2 == 0:
        even_numbers += 1

    else:
        odd_numbers += 1

print('The number has', even_numbers, 'even_numbers')
print('The number has', odd_numbers, 'odd_numbers')



