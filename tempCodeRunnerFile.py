def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, 10):  # Выводим таблицу умножения до 9
            result = i * j
            print(f"{i} * {j} = {result}", end="  ")
        print()  # Переходим на новую строку после каждого i

# Пример использования
n_value = int(input("Введите число n: "))
multiplication_table(n_value)