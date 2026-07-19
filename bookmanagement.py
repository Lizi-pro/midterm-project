import sys
import json
import re
import os
from datetime import datetime
class Item:    # ვქმნით მშობელ კლასს, რომ წიგნების გარდა სხვა მონაცემებზეც გამოვიყენოთ ჩვენი პროგრამა მომავალში
    def __init__(self, title, year):
        self.__title = title
        self.__year = year

    @property     # getter უზრუნველყოფს, რომ private არგუმენტებთან გვქონდეს წვდომა
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

class Book(Item):    # ვქმნით წიგნის კლასს, რომელსაც არგუმენტად ვამატეთ ავტორს, ხოლო დანარჩენ მონაცემებს იღებს მშობელი კლასისგან
    def __init__(self, title, author, year):
        super().__init__(title, year)
        self.__author = author

    @property
    def author(self):
        return self.__author

class BookManager:    # ვქმნით კლასს წიგნების სამართავად
    def __init__(self):
        self.books = []    # ვქმნით ცარიელ სიას, რომელშიც შემდგომში ჩაიწერება მონაცემები
        self.file = 'bookdata.json'

    def save_books(self):   # წიგნების სიას ვინახევთ json ფორმატში, რომ პროგრამის დახურვის შემდეგ მონაცემები არ დაიკარგოს
        data = []    # ვქმნით ცარიელ სიას, რომელშიც ჩაიწერება მონაცემები json ფორმატით, შემდგომში json-ის ფაილის შესაქმნელად
        for book in self.books:  # გადაგვაქვს მონაცემები json ფორმატში
            data.append({
                'title': book.title,
                'author': book.author,
                'year': book.year
            })

        with open(self.file, mode='w', encoding='utf-8') as f:    # ვხსნით json ფაილს და მასში ვწერთ ჩვენს მიერ სტრუქტურიზებულ მონაცემებს
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_books(self):
        try:
            with open(self.file, mode='r', encoding='utf-8') as f:
                old_data = json.load(f)    # მონაცემებს ვიღებთ json ფაილიდან და ვინახავთ პირვანდელ ფორმატში,
                for i in old_data:                            # პროგრამის ახლიდან გაშვებისას რომ არ დაიკარგოს
                    book = Book(i['title'], i['author'], i['year'])
                    self.books.append(book)
        except (json.JSONDecodeError, FileNotFoundError):
            print('ფაილის ჩატვირთვა ვერ მოხერხდა')

    def addbook(self, new_book):        # მომხმარებლის მიერ ხელით შეყვანილ წიგნს ვამატებთ ჩვენს ძველ სიას
        self.books.append(new_book)
        self.save_books()

    def seebooks(self):         # გამოგვაქვს მონაცემები ლამაზ ფორმატში მომხმარებლისთვის
        print(f"{'სათაური':<40}{'ავტორი':<40}{'გამოშვების წელი'}")
        length = 110
        print('=' * length)
        for book in self.books:
            print(f"{book.title:<40}{book.author:<40}{book.year}")
            print('-' * length)

    def findbook(self, find_title):         # ვეძებთ წიგნს სათაურის პირველი 5 ასოს შესაბამისობის მიხედვით
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
        else:            # როცა ვიპოვით შემდეგ გამოგვაქვს ლამად ფორმატში
            print(f"\n{'სათაური':<40}{'ავტორი':<40}{'გამოშვების წელი'}")
            print('=' * length)
            for book in self.books:    # ერთზე მეტი წიგნი თუა მაგ სათაურით ყველა რომ გამოგვიტანოს
                if find_title[:5] == book.title[:5]:
                    print(f"{book.title:<40}{book.author:<40}{book.year}")
                    print('-' * length)

manager = BookManager()     # ვქმნით ობიექტს bookmanager-ის ასამუშავებლად

if not os.path.exists('bookdata.json'):      # თუ პროგრამის გაშვებისას json ფაილი არ გვექნება, შეგვიქმნის თავდაპირველი მონაცემებით
    b1 = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 1200)
    b2 = Book("1984", "ჯორჯ ორუელი", 1949)
    b3 = Book("პატარა უფლისწული", "ანტუან დე სენტ-ეგზიუპერი", 1943)
    b4 = Book("დიდოსტატის მარჯვენა", "კონსტანტინე გამსახურდია", 1939)
    b5 = Book("გაზაფხული", "ვაჟა-ფშაველა", 1889)
    manager.addbook(b1)
    manager.addbook(b2)
    manager.addbook(b3)
    manager.addbook(b4)
    manager.addbook(b5)
else:
    manager.load_books()

choice = ''    # მომხმარებელს ვაძლევთ არჩევანს რა ოპერაციის განხორციელება უნდა
while choice != '0':
    choice = input('ახალი წიგნის დასამატებლად შეიყვანეთ 1, ყველა წიგნის სანახავად შეიყვანეთ 2, წიგნის მოსაძებნად არჩიეთ 3, ' \
    'გასასვლელად აირჩიეთ 0: ')
    if choice == '1':
        # ვალიდაციაში ვატარებთ მონაცემებს
        # სათაურის ვალიდაცია
        right_title = False
        while not right_title:
            title = input(f'\nშეიყვანეთ წიგნის სათაური: ')
            if not title.strip():
                a = input(f'\nსათაური არ შეიძლება იყოს ცარიელი, გასაგრძელებლად შეიყვანეთ 1, გასასვლელად 0: ')
                while a != '1' and a != '0':
                    a = input(f'\nშეიყვანეთ მხოლოდ 1 ან 0: ')
                if a == '0':
                    sys.exit()
            else:
                right_title = True
        # ავტორის ვალიდაცია
        author_pattern = r'[ა-ჰ\s\-]+'
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
        # გამოშვების წლის ვალიდაცია
        year_pattern = r'[0-9]+'
        right_year = False
        a = None
        while not right_year:
            year = input(f'\nშეიყვანეთ გამოშვების წელი: ')
            if not re.fullmatch(year_pattern, year):
                a = input(f'\nგამოშვების წელი უნდა შეიცავდეს მხოლოდ ციფრებს, გასაგრძელებლად შეიყვანეთ 1, გასასვლელად 0: ')
            elif int(year) > datetime.now().year:
                a = input(f'\nგამოშვების წელი არ უნდა იყოს მიმდინარე წელზე მეტი, გასაგრძელებლად შეიყვანეთ 1, გასასვლელად 0: ')
            else:
                right_year = True
            if a:
                while a != '1' and a != '0':
                    a = input(f'\nშეიყვანეთ მხოლოდ 1 ან 0: ')
                if a == '0':
                    sys.exit()

        new_book = Book(title, author, int(year))   # ვალიდაციის შემდეგ ვქმნით ობიექტს, რომელიც გადასცემს book კლასს სწორ მონაცემებს
        manager.addbook(new_book)     # addbook ფუნქციით ამ მონაცემებს ვამატებთ სიაში, რომელიც შემგომ გადავა json ფაილში
        print(f'\nწიგნი წარმატებით დაემატა\n')

    elif choice == '2':
        print(f'\nიხილეთ ყველა წიგნის დეტალური ინფორმაცია:\n')
        manager.seebooks()
    elif choice == '3':
        find_title = input(f'\nშეიყვანეთ წიგნის სათაური მის მოსაძებნად: ')
        manager.findbook(find_title)
    elif choice == '0':
        print(f'\nსისტემიდან წარმატებით გამოხვედით')
        sys.exit()
    else:
        print(f'\nშეიყვანეთ მხოლოდ 1, 2, 3 ან 0\n')

