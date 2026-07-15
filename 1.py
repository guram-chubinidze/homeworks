class Book:
    """წიგნის ობიექტი, რომელიც მხოლოდ აღწერს წიგნს."""
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __eq__(self, other):
        # წიგნები ითვლება ერთნაირად, თუ სათაური და ავტორი ემთხვევა
        if not isinstance(other, Book):
            return False
        return self.title.lower() == other.title.lower() and self.author.lower() == other.author.lower()

    def __hash__(self):
        # საჭიროა იმისათვის, რომ შევადაროთ 
        return hash((self.title.lower(), self.author.lower()))

    def __str__(self):
        return f"\"{self.title}\" - {self.author} ({self.year})"


class Library:
    """ბიბლიოთეკა, რომელიც მართავს წიგნების მარაგს."""
    def __init__(self):
        self.inventory = {}  # ფორმატი: {Book_object: quantity}

    def add_book(self, title: str, author: str, year: int, amount: int = 1):

        new_book = Book(title, author, year)
        
        if new_book in self.inventory:
            self.inventory[new_book] += amount
        else:
            self.inventory[new_book] = amount

        print(f"\n✔️ წიგნი \"{title}\" წარმატებით დაემატა. რაოდენობა: {self.inventory[new_book]}")
    
    def search_by_title(self, query: str):
        print(f"\n--- ძებნის შედეგი: '{query}' ---")
        found = False
        # ვეძებთ ლექსიკონის (inventory) გასაღებებში (Book ობიექტებში)
        for book in self.inventory.keys():
            if query.lower() in book.title.lower():
                qty = self.inventory[book]
                status = f"{qty} კოპია" if qty > 0 else "ხელმიუწვდომელია"
                print(f"📖 {book} -> [{status}]")
                found = True
        if not found:
            print("❌ წიგნი ამ სათაურით ვერ მოიძებნა.") 

    def display_all_books(self):
        print("\n--- ბიბლიოთეკაში არსებული წიგნები ---\n")
        if not self.inventory:
            print("ბიბლიოთეკა ცარიელია.")
            return
        
        for i, (book, qty) in enumerate(self.inventory.items(), start=1):
            status = f"{qty} კოპია" if qty > 0 else "ხელმიუწვდომელია"
            print(f"{i}. {book} -> [{status}]")

    def borrow_book(self, index: int):
        # ლექსიკონიდან წიგნის მისაღებად სიად ვაქცევთ (დროებით)
        books_list = list(self.inventory.keys())
        if 0 <= index < len(books_list):
            book = books_list[index]
            if self.inventory[book] > 0:
                self.inventory[book] -= 1
                print(f"\n📚 თქვენ გაიტანეთ: {book.title}.")
                print(f"დარჩენილია: {self.inventory[book]}")
            else:
                print("\n❌ ეს წიგნი გატანილია!")
        else:
            print("\n❌ არასწორი არჩევანი!")


if __name__ == "__main__":
    my_library = Library()
    # საწყისი დამატება   
    my_library.add_book("ვაიმე, ჩემო ვენახო", "რეზო ჭეიშვილი", 1987, 1),
    my_library.add_book("აკა მორჩილაძე", "სანტა ესპერანსა", 2006, 3),
    my_library.add_book("კასი — ყველაზე ლამაზი გოგო", "ჩარლზ ბუკოვსკი", 1983, 1),
    my_library.add_book("ოსტატი და მარგარიტა", "მიხეილ ბულგაკოვი", 1967, 1),
    my_library.add_book("მექანიკური ფორთოხალი", "ენტონი ბერჯისი", 1962, 3),
    my_library.add_book("მებრძოლთა კლუბი", "ჩაკ პალანიკი", 1996, 4),
    my_library.add_book("ტრამალის მგელი", "ჰერმან ჰესე", 1927, 2),
    my_library.add_book("ოქროს ტაძარი", "იუკიო მისიმა", 1956, 1),
    my_library.add_book("ქალი ქვიშაში", "კობო აბე", 1962, 1),
    my_library.add_book("ქუჩის ბიჭები", "პიერ პაოლო პაზოლინი", 1956, 2)

    while True:
        print("\n====== მინი-ბიბლიოთეკის მენიუ ======")
        print("1. სიის ნახვა | 2. წიგნის დამატება | 3. ძებნა | 4. გატანა | 5. გასვლა")
        
        action = input("\nაირჩიეთ (1-5): ")
        
        if action == "1":
            my_library.display_all_books()
            
        elif action == "2":
            title = input("სათაური: ")
            author = input("ავტორი: ")
            year = int(input("გამოცემის წელი: "))
            qty = int(input("რამდენი კოპიის დამატება გსურთ?: "))
            my_library.add_book(title, author, year, qty)
            
        elif action == "3":
            query = input("შეიყვანეთ სათაურის ნაწილი: ")
            my_library.search_by_title(query)
            
        elif action == "4":
            my_library.display_all_books()
            choice = int(input("\nაირჩიეთ ნომერი: "))
            my_library.borrow_book(choice - 1)
            
        elif action == "5":
            break
      