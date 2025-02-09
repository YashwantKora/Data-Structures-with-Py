# def MergeSort(data):
#     if len(data) > 1:
#         mid = len(data) // 2
#         left = data[:mid]
#         right = data[mid:]
#         MergeSort(left)
#         MergeSort(right)
#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#                 data[k] = left[i]
#                 i += 1
#             else:
#                 data[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             data[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             data[k] = right[j]
#             j += 1
#             k += 1
# array = [3,5,1,2,6,4,7,9,8]
# MergeSort(array)
# print(array)

def MergeSort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        MergeSort(left)
        MergeSort(right)
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
array = [2,4,6,8,1,3,5,7,9]
MergeSort(array)
print(array)
