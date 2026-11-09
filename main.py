import random


def input_size():
    """
    Функция, запрашивающая
    размер двумерного массива.
    """
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))

    return rows, cols


def create_manual(rows, cols, array):
    """
    Функция, которая создает массив
    с ручным вводом элементов.
    """
    array = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f'Элемент [{i}][{j}]: ')))
        array.append(row)

    return array


def create_auto(rows, cols):
    """
    Функция, создающая массив
    из случайных чисел от 0 до 100
    """
    array = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(0,100))
        array.append(row)

    return array


def create_array(rows, cols, array):
    """
    Функция которая предлагает
    выбрать способ создания массива.
    """
    if rows == 0:
        print("Сначала введите размер массива")
        return array

    print('1) Вручную')
    print('2) Автоматически')
    print('3) Назад')

    choice = input('Выберите способ: ').strip()

    if choice == '1':
        array = create_manual(rows, cols)

    elif choice == '2':
        array = create_auto(rows, cols)

    return array


def print_array(array):
    """
    Функция которая
    выводит массив
    на экран
    """
    if array == []:
        print('Массив еще не был создан')
    else:
        for row in array:
            print(*row, sep='\t')

def print_diagonals(array):
    """
    Функция №7. Выводит главную
    и побочную диагонали массива.
    """
    size = min(len(array), len(array[0]))
    main_diag = []
    side_diag = []
    for i in range(size):
        main_diag.append(array[i][i])
        side_diag.append(array[i][len(array[0]) - 1 - i])

    print("Главная диагональ:", *main_diag)
    print("Побочная диагональ:", *side_diag)


def sum_above_diagonal(array):
    """
    Функция №9. Считает сумму элементов,
    расположенных выше главной диагонали.
    """
    total = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            if j > i:
                total += array[i][j]

    print("Сумма элементов выше главной диагонали:", total)


def min_of_row_maxes(array):
    """
    Функция №26. Находит минимальный элемент
    среди максимальных элементов строк.
    """
    maxes = []
    for row in array:
        maxes.append(max(row))

    min_value = min(maxes)
    row_index = maxes.index(min_value)
    col_index = array[row_index].index(min_value)

    print("Максимумы строк:", *maxes)
    print("Минимальный из них:", min_value)
    print("Строка:", row_index + 1, "Столбец:", col_index + 1)


def replace_by_first_row_sum(array):
    """
    Функция №29. Заменяет элементы, меньшие
    суммы первой строки, на эту сумму.
    """
    first_sum = sum(array[0])
    print("Сумма первой строки:", first_sum)

    for row in array:
        for x in row:
            if x < first_sum:
                print(first_sum, end="\t")
            else:
                print(x, end="\t")
        print()


def sum_positive_without_zeros(array):
    """
    Функция №31. Считает в строках
    сумму положительных элементов
    без нулей 
    """
    total = 0

    for row in array:
        if 0 not in row:
            for x in row:
                if x > 0:
                    total += x

    print("Сумма положительных элементов в строках:", total)

def functions_menu(array):
    """
    Функция, которая выводит меню
    функций работы с массивом.
    """
    flag = True
    if array == []:
        print("Сначала создайте массив")
        return

    while flag:
        print("\nа. Напечатать главную и побочную диагонали")
        print("б. Сумма элементов выше главной диагонали")
        print("в. Минимальный из максимумов строк и его индексы")
        print("г. Заменить элементы меньше суммы первой строки на эту сумму")
        print("д. Сумма положительных элементов в строках без нулей")
        print("е. Назад")
        choice = input("Выберите функцию: ")

        if choice == "а":
            print_diagonals(array)
        elif choice == "б":
            sum_above_diagonal(array)
        elif choice == "в":
            min_of_row_maxes(array)
        elif choice == "г":
            replace_by_first_row_sum(array)
        elif choice == "д":
            sum_positive_without_zeros(array)
        elif choice == "е":
            flag = False

        input("Нажмите Enter, чтобы вернуться назад")


def main():
    """
    Главная функция
    с меню программы.
    """
    rows = 0
    cols = 0
    array = []
    flag = True

    while flag:
        print("\n1. Ввод размера массива")
        print("2. Создание массива")
        print("3. Просмотр массива")
        print("4. Выполнение функций")
        print("5. Выход")
        choice = input("Выберите пункт: ")

        if choice == "1":
            rows, cols = input_size()
            array = []
        elif choice == "2":
            array = create_array(rows, cols, array)
        elif choice == "3":
            print_array(array)
        elif choice == "4":
            functions_menu(array)
        elif choice == "5":
            flag = False
            print("Программа завершена.")
            


if __name__ == "__main__":
    main()