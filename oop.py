from abc import ABC, abstractmethod
import logging

# ლოგირების კონფიგურაცია (დაჯავშნები ჩაიწერება ფაილში "bookings.log")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bookings.log", encoding="utf-8"),
        logging.StreamHandler()  # კონსოლშიც რომ გამოჩნდეს
    ]
)

# ოთახების ენუმი
class RoomType:
    SINGLE = "Single"
    DOUBLE = "Double"
    SUITE = "Suite"

# ==========================================
# 1. ოთახის ინტერფეისი და კლასი
# ==========================================
class IRoom(ABC):
    room_number: int
    room_type: str
    price_per_night: float
    is_available: bool
    max_guests: int
    
    @abstractmethod
    def book_room(self):     
        pass

    @abstractmethod
    def release_room(self):     
        pass

    @abstractmethod
    def calculate_price(self, nights: int) -> float:     
        pass


class Room(IRoom): 
    def __init__(self, room_number: int, room_type: str, price_per_night: float, is_available: bool, max_guests: int):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = is_available
        self.max_guests = max_guests

    # დაჯავშნა
    def book_room(self):
        if self.is_available: # ამოწმებს თავისუფალია თუ არა
            self.is_available = False # უცვლის სტატუს ოთახს
            return True # აბრუნებს რომ დაიჯავშნა
        return False
    
    # ოთახის გათავისუფლება
    def release_room(self):
        self.is_available = True # უცვლის სტატუს ოთახს
    
    # გადასახდელი თანხის კალკულაცია
    def calculate_price(self, nights: int) -> float:
        return self.price_per_night * nights # აბრუნებს დღეები*ფასზე

    def __str__(self):
         status = "თავისუფალია" if self.is_available else "დაკავებულია"
         return f"ოთახი {self.room_number} ({self.room_type}) - {self.price_per_night}₾/ღამე | სტატუსი: {status} | მაქს. სტუმარი: {self.max_guests}"


# ==========================================
# 2. მომხმარებლის ინტერფეისი და კლასი
# ==========================================
class ICustomer(ABC):
    name: str
    budget: float 
    booked_rooms: list 
    reward_points: int 
    
    @abstractmethod
    def add_room(self, room: Room):     
        pass

    @abstractmethod
    def remove_room(self, room: Room):     
        pass

    @abstractmethod
    def pay_for_booking(self, total_price: float) -> bool:     
        pass

    @abstractmethod
    def show_booking_summary(self) -> str:     
        pass


class Customer(ICustomer):
    def __init__(self, name: str, budget: float, booked_rooms: list = None, reward_points: int = 0):
        self.name = name
        self.budget = budget
        self.booked_rooms = booked_rooms if booked_rooms is not None else []
        self.reward_points = reward_points     
   
    # ოთახების დაჯავშნა
    def add_room(self, room: Room):     
        if room not in self.booked_rooms: # თუ უკვე არ არის დაჯავშნილი
            self.booked_rooms.append(room) # დაამატოს

    # ჯავშანის გაუქმება
    def remove_room(self, room: Room):     
        if room in self.booked_rooms: # თუ არსებობს ეს ოთახი ჩემ დაჯავშნილებში
            self.booked_rooms.remove(room)

    # გადახდა 
    def pay_for_booking(self, total_price: float) -> bool:     
        if self.budget >= total_price: # საკმარისი ბიუჯეტის შემთხვევაში
            self.budget -= total_price # აკლდება ბიუჯეტს
            # ქულების დაგროვების სისტემა: ყოველ გადახდილ 10 ლარზე 1 ქულა
            earned_points = int(total_price // 10) # ეს ცალკე უნდა გავიტანო ქულა
            self.reward_points += earned_points # დაგროვილი ქულები
            return True # წარმატებული გადახდა
        return False # არასაკმარისი თანხე
    
    # მომხმარებილს  დაჯავშნილი ოთახები
    def show_booking_summary(self) -> str:     
        if not self.booked_rooms: # ცარიელის შემთხვევაში
            return f"მომხმარებელს {self.name} არ აქვს აქტიური დაჯავშნები."
        
        summary = f"მომხმარებელი: {self.name} | ბიუჯეტი: {self.budget}₾ | ქულები: {self.reward_points}\nდაჯავშნილი ოთახები:\n"
        for r in self.booked_rooms: # აქ დაამატებს ყველა ჯავშანს
            summary += f"  - {r}\n"
        return summary


# ==========================================
# 3. სასტუმროს ინტერფეისი და კლასი
# ==========================================
class IHotel(ABC):
    name: str 
    rooms: list 
    bookings_log: list
    
    @abstractmethod
    def show_available_rooms(self, room_type: str = None) -> list:     
        pass

    @abstractmethod
    def book_room_for_customer(self, customer: Customer, room_number: int, nights: int) -> bool:     
        pass

    @abstractmethod
    def calculate_total_booking(self, room_number: int, nights: int) -> float:     
        pass

    @abstractmethod
    def log_booking(self, customer: Customer, room: Room, total_price: float):     
        pass

    @abstractmethod
    def cancel_booking(self, customer: Customer, room_number: int) -> bool:     
        pass


class Hotel(IHotel):
    def __init__(self, name: str, rooms: list = None):
        self.name = name
        self.rooms = rooms if rooms is not None else []
        self.bookings_log = []

    #  თავისუფალი ოთახების ჩვენება
    def show_available_rooms(self, room_type: str = None) -> list:
        available = [r for r in self.rooms if r.is_available] # აქ დავაბრუნებთ თავისუფალ ოთახებს რუმის კლასიდან
        if room_type:
            available = [r for r in available if r.room_type == room_type] # აქ კონკრეტული ტიპის თავისუფალ ოთახებს დააბრუნებს
        return available
    
    # აქ დათვლის გადასახდელ თანხას
    def calculate_total_booking(self, room_number: int, nights: int) -> float:
        for r in self.rooms: # სასტუმროს ყველა ოთახს დაატრიალებს
            if r.room_number == room_number: # ოთახის ნომერს შეამოწმებს თუ გვაქვს
                return r.calculate_price(nights) # აქ გადაეცემა დღეების რაოდენობა და ეს დაგვიბრუნებს დღე* ოთახის ფასზე
        return 0.0
    
    # ლოგირება 
    def log_booking(self, customer: Customer, room: Room, total_price: float):
        log_message = f"Customer: {customer.name} | Room: {room.room_number} | Price: {total_price}₾ | Points: {customer.reward_points}"
        self.bookings_log.append(log_message) # ლისტში ამატებს ლოგს
        logging.info(f"წარმატებული ჯავშანი -> {log_message}")

    # მომხმარებელი ჯავშნის ოთახს
    def book_room_for_customer(self, customer: Customer, room_number: int, nights: int) -> bool:
        # 1. ვეძებთ ოთახს ნომრის მიხედვით
        target_room = None
        for r in self.rooms: # ოთახებს ვატრიალებთ
            if r.room_number == room_number: # თუ გვაქვს ეს ოთახის ნომერი
                target_room = r # მიმდინარეს მიანიჭებს ოთახის კლასს
                break

        # ოთახის ნომერზე შემოწმება
        if not target_room:
            print("ოთახი ამ ნომრით ვერ მოიძებნა!")
            return False

        # 2. ვამოწმებთ, თავისუფალია თუ არა
        if not target_room.is_available:
            print("ოთახი უკვე დაკავებულია!")
            return False

        # 3. ვითვლით ფასს და ვამოწმებთ ბიუჯეტს
        total_price = target_room.calculate_price(nights) # მიაკითხავს მიმდინარე ოთახის ფასის დათვლას
        if customer.budget < total_price: 
            print(f"არასაკმარისი ბიუჯეტი! საჭიროა: {total_price}₾, მომხმარებელს აქვს: {customer.budget}₾")
            return False

        # 4. ხდება გადახდა და დაჯავშნა
        if customer.pay_for_booking(total_price):
            target_room.book_room() # მიაკითხავს მიმდინარე ოთახის დაჯავშნას
            customer.add_room(target_room) # დაამატებს მიმდინარე ოთახს მომხმარებლის ჯავშნებში
            self.log_booking(customer, target_room, total_price) # დაამატებს ლოგების ლისტში
            return True
        
        return False 
    
    # ჯავშნის გაუქმება
    def cancel_booking(self, customer: Customer, room_number: int) -> bool:
        # ვეძებთ ოთახს მომხმარებლის დაჯავშნილ სიებში
        target_room = None
        for r in customer.booked_rooms:
            if r.room_number == room_number: # ვეძებთ ჩვენ დაჯავშნილებში ოთახს
                target_room = r
                break

        # ამოწმებს თუ გვაქვს
        if target_room: 
            target_room.release_room() # აუქმებს ჯავშანს უცვლის სტატუსს ოთახს
            customer.remove_room(target_room) #  შლის მომხმარებლის ჯავშნებიდან
            cancel_msg = f"გაუქმდა ჯავშანი -> მომხმარებელი: {customer.name}, ოთახი: {room_number}"
            self.bookings_log.append(cancel_msg) # ლოგების ლისტში ამატებს
            logging.info(cancel_msg) # ლოგი ფაილში
            return True
        
        print("მომხმარებელს ეს ოთახი დაჯავშნილი არ აქვს!")
        return False
        
 # ოოპ ტერმინალში   
def run_hotel_system():
    # 1. საწყისი მონაცემების შექმნა
    rooms = [
        Room(101, RoomType.SINGLE, 80.0, True, 1),
        Room(102, RoomType.SINGLE, 100.0, True, 1),
        Room(201, RoomType.DOUBLE, 150.0, True, 2),
        Room(202, RoomType.DOUBLE, 180.0, True, 2),
        Room(301, RoomType.SUITE, 300.0, True, 4),
        Room(302, RoomType.SUITE, 450.0, True, 4),
    ]
    hotel = Hotel("Grand Tbilisi Hotel", rooms)
    
    print("👋 მოგესალმებით სასტუმროს მართვის სისტემაში!")
    name = input("გთხოვთ, შეიყვანოთ თქვენი სახელი: ")
    try:
        budget = float(input("შეიყვანეთ თქვენი ბიუჯეტი (₾): "))
    except ValueError:
        budget = 500.0
        print("არასწორი ფორმატი. ავტომატურად მოგენიჭათ ბიუჯეტი: 500.0₾")
        
    customer = Customer(name=name, budget=budget)

    # მთავარი მენიუს ციკლი
    while True:
        # ჰორიზონტალური მენიუ ტერმინალისთვის
        print("\n" + "="*80)
        print(" [1] ოთახის დაჯავშნა  |  [2] ჩემი დაჯავშნები  |  [3] ჯავშნის გაუქმება  |  [4] გასვლა ")
        print("="*80)
        
        choice = input("აირჩიეთ სასურველი მოქმედება (1-4): ").strip()

        if choice == "1":
            print("\n--- 1. მოთხოვნის დაფიქსირება ---")
            print("აირჩიეთ სასურველი ოთახის ტიპი:")
            print(f"1. {RoomType.SINGLE} | 2. {RoomType.DOUBLE} | 3. {RoomType.SUITE} | 4. ნებისმიერი")
            
            type_choice = input("თქვენ აირჩიეთ რიცხვი : ").strip()
            selected_type = None
            if type_choice == "1":
                selected_type = RoomType.SINGLE
            elif type_choice == "2":
                selected_type = RoomType.DOUBLE
            elif type_choice == "3":
                selected_type = RoomType.SUITE

            try:
                nights = int(input("რამდენი ღამით გსურთ დარჩენა?: "))
                if nights <= 0: raise ValueError
            except ValueError:
                print("❌ არასწორი დღეების რაოდენობა!")
                continue

            # 2. სისტემა ეძებს და აჩვენებს თავისუფალ ოთახებს
            print("\n--- 2. თავისუფალი ოთახების ძებნა ---")
            available_rooms = hotel.show_available_rooms(selected_type)
            
            if not available_rooms:
                print("❌ სამწუხაროდ, არჩეული ტიპის თავისუფალი ოთახი ამჟამად არ არის.")
                continue

            print("ხელმისაწვდომი ოთახები:")
            for r in available_rooms:
                total_price = r.calculate_price(nights)
                print(f"  👉 ოთახი №{r.room_number} ({r.room_type}) | ფასი 1 ღამე: {r.price_per_night}₾ | ჯამური ფასი ({nights} ღამე): {total_price}₾")

            # 3. მომხმარებელი ირჩევს კონკრეტულ ოთახს
            try:
                room_num = int(input("\nშეიყვანეთ იმ ოთახის ნომერი, რომლის დაჯავშნაც გსურთ: "))
            except ValueError:
                print("❌ არასწორი ოთახის ნომერი!")
                continue

            # ვამოწმებთ, საერთოდ არსებობს თუ არა ეს ოთახი ჩვენს ნაჩვენებ სიაში
            chosen_room = next((r for r in available_rooms if r.room_number == room_num), None)
            if not chosen_room:
                print("❌ ასეთი თავისუფალი ოთახი სიაში არ არის!")
                continue

            # 4. 5. 6. 7. სისტემა ამოწმებს ბიუჯეტს, ახდენს გადახდას, რიცხავს ქულებს და ინახავს ლოგში
            total_cost = chosen_room.calculate_price(nights)
            print(f"\n--- 3. ბიუჯეტის შემოწმება და გადახდა ---")
            print(f"საჭირო თანხა: {total_cost}₾ | თქვენი მიმდინარე ბიუჯეტი: {customer.budget}₾")
            
            confirm = input(f"ნამდვილად გსურთ ოთახი №{room_num}-ის დაჯავშნა? (y/n): ").strip().lower()
            if confirm == 'y' or confirm == 'yes':
                # book_room_for_customer თავის თავში აკეთებს ბიუჯეტის შემოწმებას, 
                # თანხის ჩამოჭრას, ქულების დარიცხვას, ოთახის ფლაგის შეცვლას და ფაილში ლოგირებას!
                success = hotel.book_room_for_customer(customer, room_num, nights)
                if success:
                    print(f"\n🎉 გილოცავთ! ოთახი №{room_num} წარმატებით დაიჯავშნა!")
                    print(f"💰 დარჩენილი ბიუჯეტი: {customer.budget:.2f}₾")
                    print(f"⭐ დაგროვილი ქულები: {customer.reward_points} pts")
                else:
                    print("\n❌ დაჯავშნა ვერ განხორციელდა (არასაკმარისი ბიუჯეტი ან ოთახი დაკავებულია).")
            else:
                print("ჯავშანი გაუქმებულია.")

        elif choice == "2":
            # მომხმარებლის მიმდინარე სტატუსი
            print("\n--- ჩემი დაჯავშნების სტატუსი ---")
            print(customer.show_booking_summary())

        elif choice == "3":
            # 8. დაჯავშნის გაუქმება
            print("\n--- ჯავშნის გაუქმება ---")
            if not customer.booked_rooms:
                print("თქვენ არ გაქვთ აქტიური ჯავშნები.")
                continue
                
            print("თქვენი აქტიური ჯავშნები:")
            for r in customer.booked_rooms:
                print(f"  • ოთახი №{r.room_number} ({r.room_type})")
                
            try:
                room_to_cancel = int(input("\nშეიყვანეთ გასაუქმებელი ოთახის ნომერი: "))
                success = hotel.cancel_booking(customer, room_to_cancel)
                if success:
                    print(f"✔️ ჯავშანი გაუქმდა. ოთახი №{room_to_cancel} ისევ თავისუფალია.")
                else:
                    print("❌ გაუქმება ვერ მოხერხდა.")
            except ValueError:
                print("❌ არასწორი ნომერი.")

        elif choice == "4":
            print("\nგმადლობთ, რომ სარგებლობთ ჩვენი სისტემით! ნახვამდის! 😊")
            break
        else:
            print("❌ არასწორი არჩევანი, გთხოვთ სცადოთ თავიდან (1-4).")    
            
# გაშვება           
run_hotel_system()
