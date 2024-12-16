def personal_sum(*numbers):
    a = 0
    incorrect_data = 0

    # Unpack if the argument is a single list or tuple
    if len(numbers) == 1 and isinstance(numbers[0], (list, tuple)):
        numbers = numbers[0]

    for i in numbers:
        try:
            if isinstance(i, (int, float)):
                a += i
            else:
                raise TypeError(f"Некорректный тип данных для подсчёта суммы - {i}")
        except TypeError as exp:
            print(exp)
            incorrect_data += 1

    return a, incorrect_data


def calculate_average(*numbers):
    # Handle single string or incorrect type input
    if len(numbers) == 1 and isinstance(numbers[0], str):
        # Treat string as individual characters
        numbers = list(numbers[0])
    elif len(numbers) == 1 and isinstance(numbers[0], (list, tuple)):
        numbers = numbers[0]
    elif not isinstance(numbers[0], (list, tuple)):
        print("В numbers записан некорректный тип данных")
        return None

    total_sum, incorrect_data = personal_sum(*numbers)
    correct_count = len(numbers) - incorrect_data

    if correct_count == 0:
        print("Нет корректных чисел для вычисления среднего значения.")
        return 0

    average = total_sum / correct_count
    return average


# Test cases
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
