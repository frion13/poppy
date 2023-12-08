import random
import math


def generate_random_array(length, min_val, max_val):
    return [random.uniform(min_val, max_val) for _ in range(length)]


def calculate_pearson_correlation(arr1, arr2):
    n = len(arr1)
    sum_arr = sum
    sum_of_squares = lambda arr: sum(val ** 2 for val in arr)
    sum_of_products = lambda arr1, arr2: sum(val1 * val2 for val1, val2 in zip(arr1, arr2))
    numerator = n * sum_of_products(arr1, arr2) - sum_arr(arr1) * sum_arr(arr2)
    denominator = math.sqrt(
        (n * sum_of_squares(arr1) - sum_arr(arr1) ** 2) * (n * sum_of_squares(arr2) - sum_arr(arr2) ** 2)
    ) or 1
    return numerator / denominator


array1 = generate_random_array(10, 1, 10)
array2 = generate_random_array(10, 1, 10)

print('Массив 1:', array1)
print('Массив 2:', array2)

correlation = calculate_pearson_correlation(array1, array2)
print('Корреляция Пирсона:', correlation)
