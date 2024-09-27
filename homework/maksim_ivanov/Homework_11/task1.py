class Book:
    material = 'Бумага'
    presence_of_text = True
    title: str
    autor_name: str
    count_pages: int
    ISBN = ''
    reserved = False

    def __init__(self, title, autor_name, count_pages):
        self.title = title
        self.autor_name = autor_name
        self.count_pages = count_pages

    def __str__(self):
        return (f'Название: {self.title}, Автор: {self.autor_name}, страниц: {self.count_pages}, '
                f'материал: {self.material}{", зарезервирована" if self.reserved else ""}')


class TextBook(Book):
    school_subject: str
    group: int
    task = True

    def __init__(self, title, autor_name, count_pages, school_subject, group):
        super().__init__(title, autor_name, count_pages)
        self.school_subject = school_subject
        self.group = group

    def __str__(self):
        return (f'Название: {self.title}, Автор: {self.autor_name}, страниц: {self.count_pages}, '
                f'предмет: {self.school_subject}, класс: {self.group}{", зарезервирована" if self.reserved else ""}')


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
