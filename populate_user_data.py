"""
    data = [('<username>','<password>'),]
"""

data = [
['gui@2020.com','19000001'],
['gti@2020.com','19000002'],
['gai@2020.com','19000003'],
['gri@2020.com','19000004'],
['gui@2020.com','19000005'],
['gti@2020.com','19000006'],
['gai@2020.com','19000007'],
['gri@2020.com','19000008'],
['gui@2020.com','19000009'],
['gti@2020.com','19000010'],
['gai@2020.com','19000011'],
['gri@2020.com','19000012'],
['gui@2020.com','19000013'],
]

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','que.settings')

import django
django.setup()

from quiz.models import Student

def populate_user_data(data):
    for d in data:
        usrnm = d[1]
        psswrd = d[0]

        entry = Student(username=usrnm)
        entry.set_password(psswrd)
        entry.save()

populate_user_data(data)
print('done')