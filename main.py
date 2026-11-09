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
    print("Тут будет функция")


def functions_menu(array):
    print("Тут будет функция")


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