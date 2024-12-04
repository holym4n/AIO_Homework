try:
    unsorted_data = input('Введите числа через запятую: ')
    data = [int(num) for num in unsorted_data.split(',')]

    def calculate_average():
        global data
        avg = sum(data) / len(data)
        return avg

    average = calculate_average()
    print(f'Среднее значение чисел: {average}')
except ValueError:
    print('Ошибка: Ввод должен содержать числа, разделенные запятой.')