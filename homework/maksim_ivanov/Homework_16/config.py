import os

import dotenv

dotenv.load_dotenv()

config = {
    'user': os.getenv('DB_USER'),
    'passwd': os.getenv('DB_PASSWD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_DATABASE')
}

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
