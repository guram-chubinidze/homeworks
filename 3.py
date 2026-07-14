import datetime

class ATM:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.log_file = "atm_log.txt"

    def _log(self, action):
        with open(self.log_file, "a", encoding="utf-8") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} | {action}\n")

    def show_balance(self):
        self._log(f"ბალანსის შემოწმება. მიმდინარე ბალანსი: {self.balance} GEL")
        print(f"\n[!] თქვენი მიმდინარე ბალანსია: {self.balance} GEL")

    def withdraw(self, amount):
        if amount > self.balance:
            self._log(f"გატანის მცდელობა: {amount} GEL (წარუმატებელი)")
            print("\n[!] შეცდომა: არასაკმარისი თანხა.")
        else:
            self.balance -= amount
            self._log(f"თანხის გატანა: {amount} GEL. დარჩენილია: {self.balance} GEL")
            print(f"\n[!] ოპერაცია შესრულდა. დარჩენილი ბალანსი: {self.balance} GEL")

    def deposit(self, amount):
        if amount > 1000:
            self._log(f"შემოტანის მცდელობა: {amount} GEL (ლიმიტის გადაჭარბება)")
            print("\n[!] შეცდომა: ერთჯერადად 1000-ზე მეტი თანხის შეტანა შეუძლებელია.")
        else:
            self.balance += amount
            self._log(f"თანხის შემოტანა: {amount} GEL. ახალი ბალანსი: {self.balance} GEL")
            print(f"\n[!] ოპერაცია შესრულდა. მიმდინარე ბალანსი: {self.balance} GEL")

# პროგრამის გაშვება
if __name__ == "__main__":
    atm = ATM(5000.0)
    
    print("====== ბანკომატის მენიუ ======")
    while True:
        # ჰორიზონტალური მენიუ
        print("\n1. ბალანსი | 2. გატანა | 3. შემოტანა | 4. გასვლა")
        choice = input("აირჩიეთ ბრძანება (1-4): ")
        
        if choice == "1":
            atm.show_balance()
        elif choice == "2":
            amount = float(input("შეიყვანეთ თანხა გატანისთვის: "))
            atm.withdraw(amount)
        elif choice == "3":
            amount = float(input("შეიყვანეთ თანხა შემოტანისთვის: "))
            atm.deposit(amount)
        elif choice == "4":
            atm._log("მომხმარებელი გამოვიდა სისტემიდან.")
            print("მადლობა, ნახვამდის!")
            break
        else:
            print("არასწორი არჩევანი, სცადეთ თავიდან.")