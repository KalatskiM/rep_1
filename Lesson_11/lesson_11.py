# Первый класс
# Создайте класс book с атрибутами:
#     материал страниц
#     наличие текста
#     название книги
#     автор
#     кол-во страниц
#     ISBN
#     флаг зарезервирована ли книга или нет (True/False).
# Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
# Создайте несколько (штук 5) экземпляров разных книг.
# После создания пометьте одну книгу как зарезервированную.
# Распечатайте детали о каждой книге в таком виде:
# Если книга зарезервирована:
#     Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
# если не зарезервирована:
#     Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага
#
# Второй класс
# Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
#     предмет (типа математика, история, география),
#     класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервиров. слово),
#     наличие заданий (bool)
# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
#     Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:
#     Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9

class Book:
    material = 'бумага'
    text_exists = True

    def __init__(self, book_name, author, pages_number, isbn_code, reserved):
        self.book_name = book_name
        self.author = author
        self.pages_number = pages_number
        self.isbn_code = isbn_code
        self.reserved = reserved

    def print_book_info(self):
        to_print = f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.pages_number}, материал: {self.material}'
        print(f'{to_print}, зарезервирована') if self.reserved else print(f'{to_print}')

class SchoolBook(Book):
    task_exists = True

    def __init__(self, book_name, author, pages_number, isbn_code, reserved, study_subject, school_grade):
        super().__init__(book_name, author, pages_number, isbn_code, reserved)
        self.study_subject = study_subject
        self.school_grade = school_grade

    def print_school_book_info(self):
        to_print = f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.pages_number}, предмет: {self.study_subject}, класс: {self.school_grade}'
        print(f'{to_print}, зарезервирована') if self.reserved else print(f'{to_print}')

book_1 = Book('Идиот', 'Достоевский', '500', '123456789', False)
book_2 = Book('Война и мир', 'Толстой', '950', '234567891', False)
book_3 = Book('1984', 'Оруэлл', '462', '345678912', True)
book_4 = Book('Гордость и предубеждение', 'Остин', '360', '456789123', False)
book_5 = Book('Сто лет одиночества', 'Маркес', '100', '567891234', False)

book_1.print_book_info()
book_2.print_book_info()
book_3.print_book_info()
book_4.print_book_info()
book_5.print_book_info()

school_book_1 = SchoolBook('Алгебра', 'Яскевич', '150', '789456123', True, 'Математика', '7')
school_book_2 = SchoolBook('Физика для начинающих', 'Парадеев', '112', '123548', False, 'Физика', '5')
school_book_3 = SchoolBook('Английский язык для углубленного изучения', 'Деревяшкин', '341', '9562185', False, 'Английский язык', '11')
school_book_4 = SchoolBook('Органическая химия', 'Смоляк', '187', '68885674', False, 'Химия', '10')
school_book_5 = SchoolBook('Анатомия', 'Половинкина', '223', '4656216', False, 'Биология', '10')

school_book_1.print_school_book_info()
school_book_2.print_school_book_info()
school_book_3.print_school_book_info()
school_book_4.print_school_book_info()
school_book_5.print_school_book_info()
