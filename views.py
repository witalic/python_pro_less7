# -*- coding: cp1251 -*-
from presenter import *

while True:
    choice = input("""1 create
2 list
3 read
4 update
5 delete
6 exit:""")
    if choice == '1':
        note = create_note()
        notes.append(note)
    if choice == '2':
        list_elements(notes)
    if choice == '3':
        note = get_note(notes)
        print(note)
    if choice == '4':
        note = get_note(notes)
        note.update(create_note())
    if choice == '5':
        note = get_note(notes)
        notes.remove(note)
    if choice == '6':
        break
    limit_page()