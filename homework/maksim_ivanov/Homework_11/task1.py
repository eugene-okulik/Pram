from models import Book, TextBook


book1 = Book('Война и мир', 'Лев Толстой', 1300)
book2 = Book('Преступление и наказание', 'Фёдор Достоевский', 600)
book3 = Book('Евгений Онегин', 'Александр Пушкин', 280)
book4 = Book('Отцы и дети', 'Иван Тургенев', 300)
book5 = Book('Мастер и Маргарита', 'Михаил Булгаков', 500)
book2.reserved = True

for book in [book1, book2, book3, book4, book5]:
    print(book)

textbook1 = TextBook('Математика. Алгебра и начала анализа', 'Никольский', 400, 'Математика', 10)
textbook2 = TextBook('Русский язык. Теория и практика', 'Бархударов', 320, 'Русский язык', 8)
textbook3 = TextBook('История России. С древнейших времен до конца XIX века', 'Арсентьев', 350, 'История', 6)
textbook4 = TextBook('Биология. Общая биология. Базовый уровень', 'Каменский', 340, 'Биология', 10)
textbook5 = TextBook('Химия. Органическая химия', 'Габриелян', 200, 'Химия', 11)
textbook5.reserved = True

for textbook in [textbook1, textbook2, textbook3, textbook4, textbook5]:
    print(textbook)
