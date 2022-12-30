# -*- coding: cp1251 -*-

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
        pass
    if choice == '3':
        pass
    if choice == '4':
        pass
    if choice == '5':
        pass
    if choice == '6':
        break
