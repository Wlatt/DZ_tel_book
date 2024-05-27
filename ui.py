from logger import input_data, print_data, update_data, delete_data

def interface():
    print('Привет, пользователь! Выберите требуемое действие: \n1 - Внести данные \n2 - Показать данные \n3 - Обновить данные \n4 - Удалить данные')
    command = int(input('Введите число для выбора действия: '))

    while command not in [1, 2, 3, 4]:
        print('Неправильное значение. Попробуйте еще раз')
        command = int(input('Введите значение: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        update_data()
    elif command == 4:
        delete_data()
