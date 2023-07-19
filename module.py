from pathlib import Path
from copy import deepcopy

file_path = Path('modules', 'append_file.txt')

phone_book = {}
original_pb = {}


def next_id():
    if phone_book:
        return max(phone_book)+1
    return 1


def open_file():
    global original_pb
    with open(file_path, 'r', encoding='utf8') as file:
        contacts = file.readlines()
    for contact in contacts:
        uid, name, phone, comment = contact.strip().split(';')
        phone_book[int(uid)] = [name, phone, comment]
    original_pb = deepcopy(phone_book)


def add_contact(new: list[str]):
    phone_book[next_id()] = new


def save_file():
    with open(file_path, 'w', encoding='utf8') as file:
        contacts = []
        for uid, contact in phone_book.items():
            contacts.append(';'.join([str(uid), *contact]))
        contacts = '\n'.join(contacts)
        file.write(contacts)


def search_request(word: str) -> dict[int, list[str]]:
    result = {}
    for i, contact in phone_book.items():
        if word.lower() in ''.join(contact).lower():
            result[i] = contact
    return result


def change_contact(uid: int, new: list[str]) -> str:
    contact = phone_book.get(uid)
    for i in range(3):
        if new[i] != '':
            contact[i] = new[i]
    phone_book[uid] = contact
    return contact[0]


def delete_contact(uid: int) -> str:
    return phone_book.pop(uid)[0]
