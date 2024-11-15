def merge_sort(l: list) -> list:
    """
    Merge sort implementation for sorting lists.
    """
    if len(l) <= 1:
        # array with 1 or less elements is always sorted
        return l

    else:
        left_l = merge_sort(l[0:round(len(l)/2)])
        right_l = merge_sort(l[round(len(l)/2):])

        sorted_array = []
        left_size = len(left_l)
        right_size = len(right_l)
        left_idx = 0
        right_idx = 0
        while left_size + right_size != len(sorted_array):
            print(sorted_array)
            if left_idx == left_size:
                # left array no more entries, empty right one
                sorted_array.append(right_l[right_idx])
                right_idx += 1
            elif right_idx == right_size:
                # right array no more entries, empty left one
                sorted_array.append(left_l[left_idx])
                left_idx += 1
            elif left_l[left_idx] < right_l[right_idx]:
                sorted_array.append(left_l[left_idx])
                left_idx += 1
            else:
                sorted_array.append(right_l[right_idx])
                right_idx += 1

        return sorted_array
