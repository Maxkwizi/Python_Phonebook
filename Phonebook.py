def input_surname():
    return input('Введите фамилию контакта: ').title()

def input_name():
    return input('Введите имя контакта: ').title()

def input_patronymic():
    return input('Введите отчество контакта: ').title()

def input_phone():
    return input('Введите телефон контакта: ')

def input_address():
    return input('Введите адрес (город) контакта: ').title()


def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic}: {phone} {address}\n\n'

def add_contact():
    contact_str = create_contact()
    with open("phonebook.txt", 'a', encoding='utf-8') as file:
        file.write(contact_str)

def create_list_contact():
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        all_contacts_str = file.read()
    return all_contacts_str.rstrip().split('\n\n')

def print_contacts():
    contacts_list = create_list_contact()
    for n, contact in enumerate(contacts_list, 1):
        print(n, contact)

def search_contact():
    print(
        'Возможные варианты поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчество\n'
        '4. По телефону\n'
        '5. По адресу(город)'
        )
    var = input('Выберите вариант поиска: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод!')
        var = input('Выберите вариант поиска: ')
    i_var = int(var) - 1

    search = input('Введите данные для поиска: ').title()
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    #print([contacts_str])
    contacts_list = contacts_str.rstrip().split('\n\n')
    #print(contacts_list)

    for str_contact in contacts_list:
        lst_contact = str_contact.replace(':', '').split()
        if search in lst_contact[i_var]:
            print(str_contact)

def copy_to_file():
    contacts_list = create_list_contact()
    print(print_contacts())
    number_contact_to_copy = int(input('Введите номер контакта для копирования: '))
    print()
    with open("copy_contacts.txt", 'a', encoding='utf-8') as file:
        file.write(f'{contacts_list[number_contact_to_copy - 1]}\n')

def interface():
    with open("phonebook.txt", 'a', encoding='utf-8'):
        pass

    var = 0
    while var != '5':
        print(
            'Возможные варианты:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Копировать контакт\n'
            '5. Выход'
            )

        print()
        var = input('выберите вариант действия: ')
        while var not in ('1', '2', '3', '4', '5'):
            print('некорректный ввод!')
            var = input('выберите вариант действия: ')
        print()

        match var:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                copy_to_file()
            case '5':
                print('До свидания')
        print()


if __name__ == '__main__':
    interface()