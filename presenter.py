# -*- coding: cp1251 -*-
from models import notes

def create_note():
    note = {
        'title': input('Введіть заголовок: '),
        'text': input('Введіть текст: ')
        }
    return note

def list_elements(elements):
    for number, element in enumerate(elements, 1):
        print(f"{number}) {element['title']}")

def get_note(notes):
    list_elements(notes)
    number = input('Введіть номер замітки: ')
    if number.isdigit() and 0 < int(number) <= len(notes):
        note = notes[int(number) - 1]
        return note

def limit_page():
    print('====================================================')