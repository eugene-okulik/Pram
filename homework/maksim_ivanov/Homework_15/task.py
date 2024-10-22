from random import randint as randint

import mysql.connector as mysql

config = {
    'user': 'st-onl',
    'passwd': 'AVNS_tegPDkI5BlB2lW5eASC',
    'host': 'db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    'port': 25060,
    'database': 'st-onl'
}

db = mysql.connect(**config)
cursor = db.cursor(dictionary=True)

# 1.
add_student_query = ("INSERT INTO `students` (name, second_name) "
                     "VALUES (%(name)s, %(second_name)s)")

student = {
    'name': 'Anna',
    'second_name': 'Vasileva',
}

cursor.execute(add_student_query, student)  # type: ignore
student['id'] = cursor.lastrowid  # type: ignore

# 2.
books = [
    ('Book1', student['id']),
    ('Book2', student['id']),
    ('Book3', student['id']),
    ('Book4', student['id'])
]

add_book_query = "INSERT INTO `books` (title, taken_by_student_id) VALUES (%s,%s)"
cursor.executemany(add_book_query, books)

# 3.
group = {
    'title': 'Группа 135',
    'start_date': '01.09.2022',
    'end_date': '01.05.2025'
}

add_group_query = ("INSERT INTO `groups` (title, start_date, end_date) "
                     "VALUES (%(title)s, %(start_date)s, %(end_date)s)")
cursor.execute(add_group_query, group)  # type: ignore
group['id'] = cursor.lastrowid  # type: ignore

update_group_for_student_query = f"UPDATE `students` SET group_id = {group['id']} where id = {student['id']}"

cursor.execute(update_group_for_student_query)

4.
subjets = (
    {'title': 'Предмет 1'},
    {'title': 'Предмет 2'},
    {'title': 'Предмет 3'},
)
add_subjet_query = ("INSERT  INTO `subjets` (title) "
                    "VALUES (%(title)s)")
for subjet in subjets:
    cursor.execute(add_subjet_query, subjet)  # type: ignore
    subjet['id'] = cursor.lastrowid  # type: ignore
#  5.
lessons = (
    {
        'title': 'Занятие 1'
    },
    {
        'title': 'Занятие 2'
    },
)
all_lesson_id = []
add_lesson_query = ("INSERT INTO `lessons` (title, subject_id) "
                    "VALUES (%s, %s)")
for subjet in subjets:
    for lesson in lessons:
        cursor.execute(add_lesson_query, (f'{subjet["title"]} {lesson["title"]}', subjet["id"]))
        all_lesson_id.append(cursor.lastrowid)

# 6.
add_mark_query = ("INSERT  INTO `marks` (value, lesson_id, student_id) "
                  "VALUES (%s, %s, %s)")
for lesson_id in all_lesson_id:
    mark = randint(3,5)
    cursor.execute(add_mark_query, (mark, lesson_id, student['id']))



get_marks_for_student_query = f"SELECT * from marks WHERE student_id = {student['id']}"
cursor.execute(get_marks_for_student_query)
marks: list = cursor.fetchall()
for mark in marks:
    print(mark)

get_books_for_student_query = f"SELECT * from books WHERE taken_by_student_id = {student['id']}"
cursor.execute(get_books_for_student_query)
books_for_student: list = cursor.fetchall()
for book in books_for_student:
    print(book)

all_information_query = f'''
    SELECT s.name, s.second_name, g.title AS GROUP_, b.title AS BOOK, l.title AS LESSON_TITLE, m.value AS MARK, s2.title AS LESSON
    FROM students s JOIN `groups` g ON s.group_id = g.id
    JOIN books b ON s.id = b.taken_by_student_id
    JOIN marks m ON s.id = m.student_id
    JOIN lessons l ON m.lesson_id = l.id
    JOIN subjets s2 ON l.subject_id = s2.id
    WHERE s.id={student['id']};
'''

cursor.execute(all_information_query)
all_data: list = cursor.fetchall()
for data in all_data:
    print(data['name'],
          data['second_name'],
          data['GROUP_'],
          data['BOOK'],
          data['LESSON_TITLE'],
          data['MARK'],
          data['LESSON'])
db.commit()
db.close()
