# -*- coding: cp1251 -*-
import re

#def a():
#    def a2():
#        def a3():
#            def b():
#                print('Hello World')
#            return b
#        return a3
#    return a2

#print(a()()()())

#try:
#    1 / 0
#except Exception as e:
#    print(e)

#def str_worker(text):
#    if type(text) != str:
#        raise ValueError('Введено некорректні дані потрібно внести стрічку')
#    # збирає дані секунд 10
#    # бере отриману стрічку
#    # модифікує отриманими даними
#    return text

#str_worker(3)


#def try_decorator(action):
#    def wrapper(*args,**kwargs):
#        try:
#            return action(*args,*kwargs)
#        except Exception as e:
#            print(e)
#    return wrapper


#@try_decorator
#def action():
#    data = []
#    print(data[4])

#action()


#text = """
#000-000-00-00  User 1   Data user1  000-000-00-04 000-000-00-05
#001-000-00-00 User 2   Data user1
#002-000-00-00 User 3   Data user1
#003-000-00-00 User 4   Data user1  000-000-00-03 000-000-00-02
#"""

#pattern = "\d\d\d-\d\d\d-\d\d-\d\d"
#print(re.findall(pattern, text))

#pattern = "\d{3}-\d{3}-\d{2}-\d{2}"
#print(re.findall(pattern,text))


#text2 = """
#User 1
#Admin 2
#User 3
#Admin 4
#User 5
#Admin 6
#"""

## Сформувати правило того що шукаємо
#pattern = "User ."
##pattern = "\d{3}-\d{3}-\d{2}-\d{2}"
#print(re.findall(pattern,text2))
