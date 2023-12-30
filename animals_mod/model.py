import json

animals_reestr = {}
path = 'animals_reestr.json'


def open_file():
    global animals_reestr
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            animals_reestr = json.load(file)
        return True
    except:
        return False


def save_file():
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(animals_reestr, file, ensure_ascii=False)
        return True
    except:
        return False


def search(word: str) -> dict[int:dict[str, str, str, str]]:
    result = {}
    for index, note in animals_reestr.items():
        if word.lower() in ' '.join(note.values()).lower():
            result[index] = note
    return result


def check_id():
    if animals_reestr:
        return max(list(map(int, animals_reestr))) + 1
    return 1


def add_note(new: {int: dict[str, str, str, str]}):
    note = {check_id(): new}
    animals_reestr.update(note)


def change_note(index, new: {int: dict[str, str, str, str]}):
    if index.isdigit() and int(index) in list(map(int, animals_reestr)):
        note = {index: new}
        animals_reestr.update(note)
        return new.get('name')


def remove_note(index):
    if str(index).isdigit() and index in list(map(int, animals_reestr)):
        name = animals_reestr.pop(str(index))
        return name.get('name')