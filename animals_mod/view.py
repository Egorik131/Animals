import text
from datetime import datetime


def menu() -> int:
    print(text.main_menu[0])
    for i in range(1, len(text.main_menu)):
        print(f'\t{i}. {text.main_menu[i]}')
    while True:
        select = input(text.select_menu)
        if select.isdigit() and 0 < int(select) < int(len(text.main_menu)):
            return int(select)
        print(text.input_error)


def show_notes(reestr: dict[int:dict[str, str, str, str]], message):
    if reestr:
        max_name = []
        max_type = []
        max_birth_date = []
        max_commands = []
        max_create_time = []
        for note in reestr.values():
            max_name.append(len(note.get('name')))
            max_type.append(len(note.get('type')))
            max_birth_date.append(len(note.get('birth_date')))
            max_commands.append(len(note.get('commands')))
            max_create_time.append(len(note.get('create_time')))
        size_name = max(max_name)
        size_type = max(max_type)
        size_birth_date = max(max_birth_date)
        size_commands = max(max_commands)
        size_create_time = max(max_create_time)
        print('\n' + '=' * (size_name + size_type + size_birth_date + size_commands + size_create_time + 7))
        for index, note in reestr.items():
            print(f'{index:>5}.'
                  f'{note.get("name"):<{size_name + 1}}'
                  f'{note.get("type"):<{size_type + 1}}'
                  f'{note.get("birth_date"):<{size_birth_date + 1}}'
                  f'{note.get("commands"):<{size_commands + 1}}'
                  f'{note.get("create_time"):<{size_create_time + 1}}')
        print('=' * (size_name + size_type + size_birth_date + size_commands + size_create_time + 7) + '\n')

    else:
        print_message(message)


def input_show_note_id():
    return int(input(text.input_note_index))

def show_note(reestr: dict[int:dict[str, str, str, str]], index):
    result = {}
    if str(index).isdigit() and index in list(map(int, reestr)):
        result[0] = reestr.get(str(index))
        for i, cnt in result.items():
            print('\n' + '=' * 100)
            print(f'{index:>5}. '
                  f'{cnt.get("name"):<{int(len(cnt.get("name"))+2)}}'
                  f'{cnt.get("type"):<{int(len(cnt.get("type"))+10)}}'
                  f'{cnt.get("birth_date"):<{int(len(cnt.get("birth_date"))+10)}}'
                  f'{cnt.get("commands"):<{int(len(cnt.get("commands"))+10)}}'
                  f'{cnt.get("create_time"):<{int(len(cnt.get("create_time"))+10)}}')
            return print('=' * 100 + '\n')
    print('=' * 100 + '\n')
    print('Ошибка ввода, указанный ID номер отсутствует в реестре\n')
    print('=' * 100 + '\n')


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def add_note():
    name = input('Введите кличку животного: ')
    type = input('Введите животное (cat, dog, hamster, horse, camel, donkey): ')
    birth_date = input('Введите дату рождения животного: ')
    commands = input('Введите команды животного / что животное умеет: ')
    create_time = str(datetime.now().replace(microsecond=0))
    new = {'name': name, 'type': type, 'birth_date': birth_date, 'commands': commands, 'create_time': create_time}
    return new


def search_word() -> str:
    return input(text.search_word)


def change_note():
    name = input('Введите кличку животного: ')
    type = input('Введите животное (cat, dog, hamster, horse, camel, donkey): ')
    birth_date = input('Введите дату рождения животного: ')
    commands = input('Введите команды животного / что животное умеет: ')
    create_time = str(datetime.now().replace(microsecond=0))
    new = {'name': name, 'type': type, 'birth_date': birth_date, 'commands': commands, 'create_time': create_time}
    return new

def input_change_id():
    return str(input(text.input_chgindex))

def input_del_id():
    return int(input(text.input_delindex))

def input_start_date():
    start = input(text.input_start_date)
    try:
        start_date = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        print(start_date.date())
        return start_date
    except:
        print("Введена некорректная дата. Введите повторно.")
        return input_start_date()

def input_end_date():
    end = input(text.input_end_date)
    try:
        end_date = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        print(end_date.date())
        return end_date
    except:
        print("Введена некорректная дата. Введите повторно.")
        return input_end_date()

def show_notes_filter(reestr: dict[int:dict[str, str, str, str]], index_start, index_end):
        count = 0
        for index, note in reestr.items():
            temp_date = datetime.strptime(note.get("create_time"), '%Y-%m-%d %H:%M:%S')
            if temp_date > index_start and temp_date < index_end:
                count += 1
                print(f'{index:>5}.'
                    f'{note.get("name"):<20}'
                    f'{note.get("type"):<30}'
                    f'{note.get("birth_date"):<30}'
                    f'{note.get("commands"):<30}'
                    f'{note.get("create_time"):<40}')
        if count == 0:
            print('\n' + '=' * len(text.error_message))
            print(text.error_message)
            print('=' * len(text.error_message) + '\n')
