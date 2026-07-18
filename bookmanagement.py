import sys
import json
import re
class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    @property
    def title(self):
        return self.__title if len(self.__title) <= 45 else self.__title[:45] + '...'

    @property
    def author(self):
        return self.__author if len(self.__author) <= 35 else self.__author[:35] + '...'

    @property
    def year(self):
        return self.__year

class BookManager:
    def __init__(self):
        self.books = []
        self.file = 'bookdata.json'

    def save_books(self):
        data = []
        for book in self.books:
            data.append({
                'title': book._Book__title,
                'author': book._Book__author,
                'year': book.year
            })

        with open(self.file, mode='w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_books(self):
        with open(self.file, mode='r', encoding='utf-8') as f:
            old_data = json.load(f)
            for i in old_data:
                book = Book(i['title'], i['author'], i['year'])
                self.books.append(book)

    def addbook(self, new_book):
        self.books.append(new_book)
        self.save_books()

    def seebooks(self):
        print(f'{'სათაური':<50}{'ავტორი':<40}{'გამოშვების წელი'}')
        length = 110
        print('=' * length)
        for book in self.books:
            print(f'{book.title:<50}{book.author:<40}{book.year}')
            print('-' * length)

    def findbook(self):
        found = False
        length = 110

        while not found:
            for book in self.books:
                if find_title[:5] == book.title[:5]:
                    found = True
                    break  # for-ის break
            else:
                print(f'\nწიგნი ვერ მოიძებნა\n')
                break  # while-ის break
        else:
            print(f'\n{'სათაური':<50}{'ავტორი':<40}{'გამოშვების წელი'}')
            print('=' * length)
            for book in self.books:
                if find_title[:5] == book.title[:5]:
                    print(f'{book.title:<50}{book.author:<40}{book.year}')
                    print('-' * length)

manager = BookManager()
loaddata = manager.load_books()

b1 = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", "1200")
b2 = Book("1984", "ჯორჯ ორუელი", "1949")
b3 = Book("პატარა უფლისწული", "ანტუან დე სენტ-ეგზიუპერი", "1943")
b4 = Book("დიდოსტატის მარჯვენა", "კონსტანტინე გამსახურდია", "1939")
b5 = Book("გაზაფხული", "ვაჟა-ფშაველა", "1889")

# manager.addbook(b1)
# manager.addbook(b2)
# manager.addbook(b3)
# manager.addbook(b4)
# manager.addbook(b5)

a = ''
while a != '0':
    choice = input('ახალი წიგნის დასამატებლად შეიყვანეთ 1, ყველა წიგნის სანახავად შეიყვანეთ 2, წიგნის მოსაძებნად არჩიეთ 3, ' \
    'გასასვლელად აირჩიეთ 0: ')
    if choice == '1':
        title = input(f'\nშეიყვანეთ წიგნის სათაური: ')

        author_pattern = r'[ა-ჰ\s]+'
        right_author = False
        while not right_author:
            author = input(f'\nშეიყვანეთ ავტორი: ')
            if not re.fullmatch(author_pattern, author):
                a = input(f'\nავტორის სახელი უნდა შეიცავდეს მხოლოდ ქართულ ასოებს, გასაგრძელებლად შეიყვანეთ 1, გასასვლელად 0: ')
                while a != '1' and a != '0':
                    a = input(f'\nშეიყვანეთ მხოლოდ 1 ან 0: ')
                if a == '0':
                    sys.exit()
            else:
                right_author = True

        year_pattern = r'[0-9]+'
        right_year = False
        while not right_year:
            year = input(f'\nშეიყვანეთ გამოშვების წელი: ')
            if not re.fullmatch(year_pattern, year):
                a = input(f'\nგამოშვების წელი უნდა შეიცავდეს მხოლოდ ციფრებს, გასაგრძელებლად შეიყვანეთ 1, გასასვლელად 0: ')
                while a != '1' and a != '0':
                    a = input(f'\nშეიყვანეთ მხოლოდ 1 ან 0: ')
                if a == '0':
                    sys.exit()
            else:
                right_year = True

        new_book = Book(title, author, year)
        manager.addbook(new_book)
        print(f'\nწიგნი წარმატებით დაემატა\n')

    elif choice == '2':
        print(f'\nიხილეთ ყველა წიგნის დეტალური ინფორმაცია:\n')
        manager.seebooks()
    elif choice == '3':
        find_title = input(f'\nშეიყვანეთ წიგნის სათაური მის მოსაძებნად: ')
        manager.findbook()
    elif choice == '0':
        print(f'\nსისტემიდან წარმატებით გამოხვედით')
        sys.exit()
    else:
        print(f'\nშეიყვანეთ მხოლოდ 1, 2, 3 ან 0\n')

