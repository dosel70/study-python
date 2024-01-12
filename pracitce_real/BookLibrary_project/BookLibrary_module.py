class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True  # 도서의 대출 가능 여부를 나타내는 플래그

    def __str__(self):
        return f"Book(title='{self.title}', author='{self.author}', publication_year={self.publication_year}, available={self.is_available})"


class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)
        print(f"{book.title}이(가) 도서관에 추가되었습니다.")

    def remove_book(self, book_title):
        for book in self.book_list:
            if book.title == book_title:
                self.book_list.remove(book)
                print(f"{book.title}이(가) 도서관에서 삭제되었습니다.")
                return
        print(f"{book_title}이(가) 도서관에 없습니다.")

    def borrow_book(self, book_title):
        for book in self.book_list:
            if book.title == book_title:
                if book.is_available:
                    book.is_available = False
                    print(f"{book.title}을(를) 대출했습니다.")
                else:
                    print(f"{book.title}은(는) 이미 대출 중입니다.")
                return
        print(f"{book_title}이(가) 도서관에 없습니다.")

    def return_book(self, book_title):
        for book in self.book_list:
            if book.title == book_title:
                if not book.is_available:
                    book.is_available = True
                    print(f"{book.title}을(를) 반납했습니다.")
                else:
                    print(f"{book.title}은(는) 이미 도서관에 있습니다.")
                return
        print(f"{book_title}이(가) 도서관에 없습니다.")

    def display_books(self):
        if not self.book_list:
            print("현재 도서관에 도서가 없습니다.")
            return

        print("도서 목록:")
        for book in self.book_list:
            print(book)


# 사용 예시
library = Library()

# 도서 추가
book1 = Book("파이썬 기초", "홍길동", 2022)
book2 = Book("자바 프로그래밍", "이순신", 2021)

library.add_book(book1)
library.add_book(book2)

# 도서 대출 및 반납
library.borrow_book("파이썬 기초")
library.return_book("파이썬 기초")

# 현재 도서 목록 출력
library.display_books()
