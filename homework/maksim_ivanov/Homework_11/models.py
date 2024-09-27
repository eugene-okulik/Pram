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