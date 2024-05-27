from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"\nДоступные форматы хранения данных: \n\n"
                    f"Вариант 1 - Колонка: \n"
                    f"{name}\n{surname}\n{phone}\n{address} \n\n"
                    f"Вариант 2 - В строчку: \n"
                    f"{name};{surname};{phone};{address} \n\n"
                    f"Укажите какой формат вы хотите использовать - 1 или 2: "))
    while var != 1 and var != 2:
        print('Неправильное значение. Попробуйте еще раз.')
        var = int(input('Введите значение: '))
    if var == 1:
        with open('data1v.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    elif var == 2:
        with open('data2v.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name}; {surname}; {phone}; {address}\n\n')

def print_data():
    print('Проверка содержимого файла data1v.csv: ')
    with open('data1v.csv', 'r', encoding='utf-8') as f:
        data_1 = f.readlines() # читаем все строки
        data_1_list = []
        j = 0
        for i in range(len(data_1)):
            if data_1[i] == '\n' or i == len(data_1) - 1:
                data_1_list.append(''.join(data_1[j:i+1])) # добавлем срезы в список
                j = i
    print(''.join(data_1_list)) # выводим в виде строки

    print('Проверка содержимого файла data2v.csv: ')
    with open('data2v.csv', 'r', encoding='utf-8') as f:
        data_2 = f.readlines() # читаем все строки
    print(*data_2) # распаковка списка и вывод

def update_data():
    file_choice = input('Выберите файл для обновления данных (1 - data1v.csv, 2 - data2v.csv): ')
    name = input('Введите имя для обновления: ')
    new_name = input('Введите новое имя: ')
    file_name = 'data1v.csv' if file_choice == '1' else 'data2v.csv'
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
    with open(file_name, 'w', encoding='utf-8') as f:
        for line in data:
            if name in line:
                f.write(line.replace(name, new_name))
            else:
                f.write(line)

def delete_data():
    file_choice = input('Выберите файл для удаления данных (1 - data1v.csv, 2 - data2v.csv): ')
    name = input('Введите имя для удаления: ')
    file_name = 'data1v.csv' if file_choice == '1' else 'data2v.csv'
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
    with open(file_name, 'w', encoding='utf-8') as f:
        if file_choice == '1':
            i = 0
            while i < len(data):
                if name in data[i]:
                    i += 4  # пропустить следующие 3 строки
                else:
                    f.write(data[i])
                i += 1
        else:
            for line in data:
                if name not in line:
                    f.write(line)
