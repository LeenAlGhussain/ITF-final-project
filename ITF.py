print("_________________________________________________________________________Welcome to the Library System_________________________________________________________________________")
class Book:
    def __init__(self, book_id, title, author, level):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.level = level
        self.available = True

class Member:
    def __init__(self, member_id, name, email, level):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.level = level
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def edit_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                member.name = input("* Enter new member:")
                member.email = input("* Enter the new member email:")
                member.level = input("* Enter the new member level (A/B/C):")
                print("Member details updated successfully.")
                return
        print("Member ID is Invalid!")

    def display_members(self):
        if not self.members:
            print("No members in the library.")
        else:
            print("Members in Library:")
            print("  ID       |       Name           |       Email              |       Level")
            for member in self.members:

                print(f"  {member.member_id}        |       {member.name}           |       {member.email}       |       {member.level}")

    def delete_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print("Member deleted successfully.")
                return
        print("Invalid member ID.")

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def display_books(self):
        if self.books:
            print("Books in Library:")
            print(" ID   |       Title       |       Author         |     Level  |   Availability")
            for book in self.books:
                availability = "Available" if book.available else "Not Available"
                print(f" {book.book_id}    |        {book.title}         |        {book.author}           |      {book.level}      |    {availability}")
        else:
            print("No books in the library.")

    def borrow_book(self, member_id, book_id):
        member = None
        book = None
        for mem in self.members:
            if mem.member_id == member_id:
                member = mem
                break
        for boo in self.books:
            if boo.book_id == book_id:
                book = boo
                break
        if not member:
            print("Invalid member ID.")
            return
        if not book:
            print("Invalid book ID.")
            return
        if not book.available:
            print("Book is not available.")
            return
        if member.level < book.level or member.level > book.level:
            print("#This Book is not appropriate for you.")
            return
        member.borrowed_books.append(book)
        book.available = False
        print("Book borrowed successfully.")

    def return_book(self, member_id, book_id):
        member = None
        book = None
        for mem in self.members:
            if mem.member_id == member_id:
                member = mem
                break
        for bk in self.books:
            if bk.book_id == book_id:
                book = bk
                break
        if not member:
            print("Invalid member ID.")
            return
        if not book:
            print("Invalid book ID.")
            return
        if book.available:
            print("Book is already available.")
            return
        if book in member.borrowed_books:
            member.borrowed_books.remove(book)
            book.available = True
            print("Book returned successfully.")
        else:
            print("Member did not borrow this book.")


member_id = 0
book_id = 0
library = Library()
member_id += 1
book_id+=1
while True:
    print("1: Add Member")
    print("2: Edit Member")
    print("3: Show Members")
    print("4: Delete Member")
    print("5: Add Book")
    print("6: Show Books")
    print("7: Borrow Book")
    print("8: Return Book")
    print("9: Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("* Enter member name: ")
        email = input("* Enter member email: ")
        level = input("* Enter the member level (A/B/C): ")
        if level == 'a' or 'A' or 'b' or 'B' or 'C' or 'c':
            member = Member(member_id, name, email, level.upper())
            library.add_member(member)
            print("# Member added successfully")
            member_id += 1
            print("____________________________________")
        elif not level:
            print("Invalid level ! ")
            level = input("*  please enter the member level again (A/B/C): ")

        else:
            print("Invalid member level!")

    elif choice == 2:
        index = int(input("* Enter the member ID: "))
        library.edit_member(index)
        print("____________________________________")

    elif choice == 3:
        library.display_members()
        print("____________________________________")

    elif choice == 4:
        member_id = int(input("* Enter the member ID to delete: "))
        library.delete_member(member_id)
        print("____________________________________")

    elif choice == 5:
        title = input("* Enter book title: ")
        author = input("* Enter book author: ")
        level = input("* Enter the book level (A/B/C): ")
        if level == 'a' or 'A' or 'b' or 'B' or 'C' or 'c':
            book = Book(book_id, title, author, level)
            library.add_book(book)
            book_id += 1
            print("____________________________________")
        else:
            print("Invalid book level!")

    elif choice == 6:
        library.display_books()
        print("____________________________________")
    elif choice == 7:
        member_id = int(input("* Enter the member ID: "))
        book_id = int(input("* Enter the book ID: "))
        library.borrow_book(member_id, book_id)
        print("____________________________________")
    elif choice == 8:
        member_id = int(input("* Enter the member ID: "))
        book_id = int(input("* Enter the book ID: "))
        library.return_book(member_id, book_id)
        print("____________________________________")
    else:
        break
