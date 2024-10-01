import datetime
import os


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            yield line


def get_data_from_line(line: str) -> tuple:
    num_date, operation = line.split(' - ')
    date_str = num_date.split('. ')[1]
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    return date, operation


for line in read_file(data_file_path):
    date, operation = get_data_from_line(line)
    if 'распечатать эту дату, но на неделю позже.' in operation:
        result = date + datetime.timedelta(weeks=1)
    elif 'распечатать какой это будет день недели' in operation:
        result = days[date.weekday()]
    elif 'распечатать сколько дней назад была эта дата' in operation:
        result = (datetime.date.today() - date.date()).days
    print(result)
