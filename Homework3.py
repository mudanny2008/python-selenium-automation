
#1. Below The Arithmetical Mean
#When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
#Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

#0(n)
def below_ar_mean(arr):
    arr_mean = sum(arr) /len(arr)
    print(arr_mean)
    final_list = []
    for num in arr:
        if num < arr_mean:
            final_list.append(num)

    return final_list

list_to_test = [1, 3, 5, 6, 4, 10, 2, 3]
print(below_ar_mean(list_to_test))



#2. Two Lowest Elements
#When given a list of elements, find the two lowest elements.
#They can be equal to each other or different.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

#0(logN)
def find_two_lowest_elements(arr):
    arr.sort()
    return arr[:2]

list = [198, 3, 4, 9, 10, 9, 2]

print(list)
print(find_two_lowest_elements(list))


