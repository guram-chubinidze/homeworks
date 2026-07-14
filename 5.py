import re
import string

class RegistrationErrorBuilder:
    def __init__(self):
        self.errors = []

    def add_error(self, message):
        self.errors.append(message)
        return self

    def has_errors(self):
        return len(self.errors) > 0

    def get_errors(self):
        return " | ".join([e.strip() for e in self.errors])

class User:
    def __init__(self, name):
        self.name = name
        self.email = "user@mail.ge"
        self.username = "John"
        self.password = "Qwerty123"
        self.builder = RegistrationErrorBuilder()
        self.punctuation = set(string.punctuation)
        self.max_length = 10

    def validate(self):
        if not self.name:
            self.builder.add_error("ველი ცარიელია")
            return self.builder

        # ვალიდაციის ლოგიკა
        if any(char in self.punctuation for char in self.name):
            self.builder.add_error("შეიცავს პუნქტუაციას")
        
        if not re.fullmatch(r'[a-z]+', self.name):
            if re.search(r'[A-Z]', self.name): self.builder.add_error("დიდი ასოები")
            if re.search(r'[0-9]', self.name): self.builder.add_error("ციფრები")
            if re.search(r'[^\x00-\x7F]', self.name): self.builder.add_error("არალათინური სიმბოლოები")
        
        if " " in self.name: self.builder.add_error("სფეისი")
        if len(self.name) > self.max_length: self.builder.add_error("ძალიან გრძელი")
        if any(ord(c) < 32 for c in self.name): self.builder.add_error("საკონტროლო სიმბოლოები")
        if '\x00' in self.name: self.builder.add_error("NULL byte")
        
        return self.builder

def main():
    while True:
        print("\n--- [ 1: რეგისტრაცია ] [ 2: გასვლა ] ---")
        choice = input("აირჩიეთ ოფცია: ").strip()

        if choice == '1':
            name = input("შეიყვანეთ სახელი: ")
            user = User(name)
            error_builder = user.validate()

            if error_builder.has_errors():
                print(f"შეცდომები: {error_builder.get_errors()}")
            else:
                print(f"რეგისტრაცია წარმატებულია! მონაცემები: სახელი: {user.name}, ელ-ფოსტა: {user.email},  ზედმეტსახელი: {user.username}")
                break # რეგისტრაციის შემდეგ ციკლი წყდება
        
        elif choice == '2':
            print("პროგრამა დაიხურა.")
            break
        else:
            print("არასწორი არჩევანი, სცადეთ თავიდან.")

if __name__ == "__main__":
    main()