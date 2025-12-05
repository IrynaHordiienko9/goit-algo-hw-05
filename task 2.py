def binary_search_with_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] >= target:
            upper_bound = arr[mid]
            right = mid - 1
        else:
            left = mid + 1

    return iterations, upper_bound


sorted_array = [0.5, 1.2, 2.8, 3.3, 4.7, 5.0, 6.6]
target_value = 3.0

result = binary_search_with_upper_bound(sorted_array, target_value)
print(f"Array: {sorted_array}")
print(f"Target value: {target_value}")
print(f"Result: (iterations, upper bound) = {result}")