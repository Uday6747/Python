# To print the count of every element in an array using User-Defined function

def count_array(arr):
    count = {}

    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for key, value in count.items():
        print(f"{key} - {value} times")


arr = [int(x) for x in input().split()]
count_array(arr)