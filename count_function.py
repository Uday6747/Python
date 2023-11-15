# This program is to print only the duplicate values and how many times it is repeated with User-Defined function.

def count_duplicates(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for key, value in count.items():
        if value > 1:
            print(f"{key} - {value} times")

arr = [int(x) for x in input().split()]
count_duplicates(arr)