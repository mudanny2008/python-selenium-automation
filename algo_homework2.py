#Even First
#Your input is an array of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input array).
#Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

arr = [7, 3, 5, 6, 4, 10, 3, 2]
def segregateEvenOdd(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        while (arr[left] % 2 == 0 and left < right):
            left += 1
        while (arr[right] % 2 == 1 and left < right):
            right -= 1

        if (left < right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right = right - 1

segregateEvenOdd(arr)
print(arr)



# 2.    Increment a Number
# Write a program that takes as input an array of digits encoding a nonnegative decimal integer D and updates the array to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

vect = [1, 2, 9]
def number(a):
    n = len(a)

    a[n - 1] += 1
    carry = a[n - 1] / 10
    a[n - 1] = a[n - 1] % 10

    for i in range(n - 2, -1, -1):
        if (carry == 1):
            a[i] += 1
            carry = a[i] / 10
            a[i] = a[i] % 10

    if (carry == 1):
        a.insert(0, 1)
number(vect)

print(vect)

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

total_sum = 0
for i in range(1, 1000):
    if (i % 3 == 0 or i % 5 == 0):
        total_sum = total_sum + i
print(total_sum)
