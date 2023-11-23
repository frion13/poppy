# Задача No1
# Дан список целых чисел numbers. Необходимо
# написать в императивном стиле процедуру для сортировки числа в списке в порядке убывания. 
# Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):
    n = len(numbers)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True
        
        if not swapped:
            break
    
    return numbers


numbers_to_sort = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = sort_list_imperative(numbers_to_sort)
print("Отсортированный массив в порядке убывания:", sorted_numbers)



# 2Написать точно такую же процедуру, но в декларативном стиле

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


numbers_to_sort = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = sort_list_declarative(numbers_to_sort)
print("Отсортированный массив в порядке убывания:", sorted_numbers)

