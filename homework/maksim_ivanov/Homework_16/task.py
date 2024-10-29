import csv
from typing import List, Dict

import mysql.connector as mysql

from config import config, data_path


def get_data_from_csv(path: str) -> List:
    with open(path, newline='') as csv_file:
        file_data = csv.DictReader(csv_file)
        data = []
        for row in file_data:
            data.append(row)
    return data


def get_data_from_db(config: Dict) -> List:
    query = '''
        select name, second_name, `groups`.title as group_title, `books`.title as subject_title, 
        `lessons`.title lesson_title, `marks`.value mark_value from students
        left join `groups` on `groups`.id = students.id
        left join `books` on books.taken_by_student_id = students.id
        left join `marks` on marks.id = students.id
        left join `lessons` on lessons.id= marks.lesson_id
        left join `subjets` on subjets.id = lessons.subject_id
    '''
    db = mysql.connect(**config)
    cusor = db.cursor(dictionary=True)
    cusor.execute(query)
    data = cusor.fetchall()
    db.close()
    return data


csv_data = get_data_from_csv(data_path)
db_data = get_data_from_db(config)
no_match = list(filter(lambda x: x not in db_data, csv_data))

print('Нет совпадений в БД:')
for row in no_match:
    print(row)

