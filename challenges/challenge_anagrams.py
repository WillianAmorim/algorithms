def merge_sort_string(string):
    if len(string) <= 1:
        return string

    meio = len(string) // 2
    left_half = string[:meio]
    right_half = string[meio:]

    left_sorted = merge_sort_string(left_half)
    right_sorted = merge_sort_string(right_half)

    sorted_string = merge(left_sorted, right_sorted)

    return sorted_string


def merge(left, right):
    merged = ""
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged += left[i]
            i += 1
        else:
            merged += right[j]
            j += 1

    merged += left[i:]
    merged += right[j:]

    return merged


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    first_sorted = merge_sort_string(first_string)
    second_sorted = merge_sort_string(second_string)

    if len(first_sorted) < 1 != len(second_sorted) < 1:
        return (first_sorted, second_sorted, False)
    if first_sorted == second_sorted:
        return (first_sorted, second_sorted, True)
    else:
        return (first_sorted, second_sorted, False)
