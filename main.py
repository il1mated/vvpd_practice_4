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
    print("В разработке")


def sum_above_diagonal(array):
    print("В разработке")


def min_of_row_maxes(array):
    print("В разработке")


def replace_by_first_row_sum(array):
    print("В разработке")


def sum_positive_without_zeros(array):
    print("В разработке")


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