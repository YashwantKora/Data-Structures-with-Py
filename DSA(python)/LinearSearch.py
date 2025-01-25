# def LinearSearch(data, n, key):
#     for i in range(0, n):
#         if data[i] == key:
#             return i
#     return -1

# key = 1
# array = [3,5,1,2,6,4,7,9,8]
# n = len(array)
# result =LinearSearch(array, n, key)

# if result == -1:
#     print("Element not found in the given array")
# else:
#     print("Element found at index: ", result)

def LinearSearch(data, n, key):
    for i in range(0, n):
        if data[i] == key:
            return i
    return -1
key = 1
array = [1,2,3,4,5,6,7,8,9]
n = len(array)
result = LinearSearch(array, n, key)

if result == -1:
    print("Element not found in the given array!")
else:
    print("Element found at index:", result)