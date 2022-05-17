def Inversion_count(array):
    n = len(array)
    if n == 1:
        return 0

    def split_count(array):
        if len(array) == 1:
            return 0

        if len(array)%2 == 0:
            left_array, right_array = array[0:int(len(array)/2)], array[int(len(array)/2):len(array)+1]

        else:
            left_array, right_array = array[0:round(int(len(array)/2))], array[round(int(len(array)/2)):len(array)+1]

        split_inversions = 0
        left_sorted = left_array[:]
        right_sorted = right_array[:]
        left_sorted.sort()
        right_sorted.sort()

        i, j = 0, 0
        while i != len(left_sorted) and j != len(right_sorted):
            if left_sorted[i] > right_sorted[j]:
                split_inversions = split_inversions + len(left_sorted) - i
                j = j + 1
            else:
                i = i + 1
                
        split_inversions = split_inversions + split_count(left_array) + split_count(right_array)
        return split_inversions
    return split_count(array)
    