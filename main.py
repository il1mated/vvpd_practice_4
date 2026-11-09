import random


def input_size():
    """
    Функция, запрашивающая
    размер двумерного массива.
    """
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))

    return rows, cols


def create_array(rows, cols, array):
    print("Тут будет функция")
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