# #1 ამოცანა 1
# შექმენი კლასი BankAccount, რომელსაც ექნება:

# დახურული ატრიბუტები: __balance, __owner.

# მეთოდი deposit(amount) – თანხის დამატება.

# მეთოდი withdraw(amount) – თანხის გამოტანა (არ უნდა გადავიდეს მინუსში).

# მეთოდი get_balance() – მხოლოდ წაკითხვისთვის.

# დაწერე კოდი ისე, რომ მომხმარებელს პირდაპირ __balance-ზე წვდომა არ ჰქონდეს.
print("------------------------------------------1---------------------------------------------------------------")     
class BankAccount:    
    def __init__(self,balance, owner):
        self.__balance = balance
        self.__owner = owner

    ## Get Balance
    @property
    def get_balance(self):
     return self.__balance 

    ## Get Owner
    @property
    def get_owner(self):
        return self.__owner 
      
    ## Add deposit
    def deposit(self,amount):
        print(f"Add deposit {amount}")
        self.__balance += amount

    # Withdraw money
    def withdraw(self,amount):
            print(f"Withdraw money {amount}")
            if 0 < amount <= self.__balance:               
                self.__balance -= amount
            else:
                print(f"ანგარიშზე არ არის საკმარისი თანხა! {amount}") 
    # Defining the __str__ method
    def __str__(self):
        return f" მომხმარებელი '{self.__owner}' ბალანსი {self.__balance}" 

person1 = BankAccount(500,"Gela")
print(f"{person1}")
person1.deposit(50)
print(f"{person1}")
person1.withdraw(650)
print(f"{person1}")
person1.withdraw(350)
print(f"{person1}")   

# #2 ამოცანა 2
# შექმენი კლასი ShoppingCart, რომელსაც ექნება:

# ატრიბუტი items (სიაში პროდუქტების რაოდენობა).

# __len__() დააბრუნებს პროდუქტების რაოდენობას.

# __eq__() ორი კალათის შედარება – აბრუნებს True, თუ რაოდენობა ტოლია.

# გააკეთე 2 კალათა და შეადარე.
# გააკეთე 3 კალათა და შეადარე.
# გააკეთე 4 კალათა და შეადარე.
print("------------------------------------------2---------------------------------------------------------------")  
class ShoppingCart:
    def __init__(self,items):
        self.__items = items

    def __len__(self):
        return len(self.__items)  

    def __eq__(self, value):
        return len(self.__items) == value  

cart1 = ShoppingCart(["Apple","Pear","Peach"])
cart2 = ShoppingCart(["Orange","Grapefruit","Lemon","Mandarin"])
cart3 = ShoppingCart(["Blackberry","Blueberry","Raspberry","Strawberry"])
cart4 = ShoppingCart(["Banana","Avocado","Mango","Kiwi","Papaya"])

print(f" cart1 == cart2 = { cart1 == cart2} ")
print(f" cart1 == cart3 = { cart1 == cart3} ")
print(f" cart1 == cart4 = { cart1 == cart4} ")
print(f" cart2 == cart3 = { cart2 == cart3} ")
print(f" cart2 == cart4 = { cart2 == cart4} ")
print(f" cart3 == cart4 = { cart3 == cart4} ")

# #3 ამოცანა 3
# გამოიყენე @dataclass მოდული კლასის Book შესაქმნელად:

# ველები: title, author, year.

# დაამატე მეთოდი is_classic() → აბრუნებს True, თუ წელი < 1970.

# შექმენი რამდენიმე წიგნი და შეამოწმე ფუნქცია.
print("------------------------------------------3---------------------------------------------------------------")  
from dataclasses import dataclass
@dataclass
class Book:
    title: str
    author: str
    year: int
    ## Is classic
    def is_classic(self):
        return self.year < 1970
    
book1 = Book("Frankenstein","Mary Shelley",1818) 
book2 = Book("To Kill a Mockingbird","Harper Lee",1960)  
book3 = Book("Fear and Loathing in Las Vegas","Hunter S. Thompson",1971) 
book4 = Book("The Name of the Rose","Umberto Eco",1980)  
book5 = Book("Lolita","Vladimir Nabokov",1955) 

print(f"book1 = {book1}\n is classic = {book1.is_classic()}\nbook2 = {book2}\n is classic = {book2.is_classic()}") 
print(f"book3 = {book3}\n is classic = {book3.is_classic()}") 
print(f"book4 = {book4}\n is classic = {book4.is_classic()}\nbook5 = {book5}\n is classic = {book5.is_classic()}") 


# #4 ამოცანა 4
# შექმენი კლასი Person, რომელსაც ექნება __del__() მეთოდი, რომელიც ბეჭდავს "Person removed" როცა ობიექტი წაიშლება.
# შექმენი ობიექტი, შემდეგ წაშალე del-ით და ნახე როგორ რეაგირებს garbage collector.
print("------------------------------------------4---------------------------------------------------------------")  
import gc
gc.disable()
#
gc.collect() 
# gc.set_debug(gc.DEBUG_LEAK)
class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        self.linked = None
        print(f"Person: {self.__name}, {self.__age} Created")       

    # def __str__(self):
    #    return f"Person: {self.__name}, {self.__age} Created"
    
    def __del__(self):
        print(f"Person removed by __del__ {self}")

p1 = Person("Giorgi",27)
p2 = Person("Ana",35)

# p1.linked = p2 # ესენი დავამატე და აქ გამოჩნდა
# p2.linked = p1 # ესენი დავამატე და აქ გამოჩნდა
# ## ახლა ჩანს რომ ეს del ქმნის უსარგებლო ელემენტებს

del p1
del p2

collected_objects = gc.collect() 
# ამ ფაილში არ მუშაობს? ვერ გავიგე - სხვა ფაილში აქ მიბრუნებს რომ რაღაც რაოდენობის ფაილები წაშალა, აქ სულ 0 ია
# გავიგე dataclass უნდა გავთიშო ეგ ურევს
# ამ კლასით არაფერი არ იქმნება, უფრო სწორად იქმნება და იშლება ეგრევე, ამ კლასის გარეშეც 21 უსარგებლო ელემენტს აბრუნებს 
# with del  
# Person removed by __del__ <__main__.Person object at 0x000001DCAC0086E0>
# Person removed by __del__ <__main__.Person object at 0x000001DCAC00C690>
# Garbage Collector-მა იპოვა და წაშალა 21 უსარგებლო ელემენტი.
# without del
# with del 
# Garbage Collector-მა იპოვა და წაშალა 21 უსარგებლო ელემენტი.
# Person removed by __del__ <__main__.Person object at 0x00000171405586E0>
# Person removed by __del__ <__main__.Person object at 0x000001714055C690>
# __del__ ფუნქცია ყველა უსარგებლო ელემენტს არ შლის,  gc.collect() თვითონ იძახებს ამ ფუნქციასაც

print(f"Garbage Collector-მა იპოვა და წაშალა {collected_objects} უსარგებლო ელემენტი.")






               

# #5 ამოცანა 5
# შექმენი კლასი Temperature, რომელსაც ექნება:

# დახურული ატრიბუტი __celsius.

# get და set property °C-სთვის.

# fahrenheit property (read-only), რომელიც აბრუნებს °F.

# შექმენი ობიექტი, შეცვალე °C და შეამოწმე °F ავტომატურად იცვლება თუ არა.
print("------------------------------------------5---------------------------------------------------------------")  
class Temperature:

    def __init__(self,celsius):
        self.__celsius = celsius

    @property
    def get_celsius(self):
        return str(self.__celsius)+"°C"
    
    @get_celsius.setter
    def get_celsius(self,celsius):
        self.__celsius = celsius

    @property
    def get_fahrenheit(self):
        return str(int(self.__celsius*9/5)+32)+"°F"    

tmp1 = Temperature(20)   
print(tmp1.get_celsius)
print(tmp1.get_fahrenheit) 
tmp1.get_celsius = 25
print(tmp1.get_celsius)
print(tmp1.get_fahrenheit)    

# #6 ამოცანა 6
# შექმენი კლასი CustomList, რომელიც:

# ინახავს ელემენტებს.

# __getitem__() – აბრუნებს ელემენტს ინდექსით.

# __setitem__() – ცვლის ელემენტს.

# __iter__() – Iterable უნდა იყოს.

# გამოიყენე for ციკლში შენი CustomList.
print("------------------------------------------6---------------------------------------------------------------")  
class CustomList:
      def __init__(self,item):
          self.__item = item      
      
      def __getitem__(self,idx):
          return self.__item[idx]
      
      def __setitem__(self,item):
          print(f"Change {self.__item} to {item}")
          self.__item = item

      def __iter__(self):        
          return  iter(self.__item) 
# Create CustomList
cl1 = CustomList(["Apple","kiwi"])
# Print First El From CustomList
print(cl1.__getitem__(0)) 
# Change CustomList
cl1.__setitem__(["Banana","Orange","Lemon"]) 
# Print First El From CustomList
print(cl1.__getitem__(0)) 
# print CustomList
for i in cl1:
    print(f"type = {type(i)} {i}")
       

# #7 ამოცანა 7
# შექმენი კლასი Refrigerator, რომელსაც ექნება:

# ატრიბუტი items (სია).

# __contains__() – აბრუნებს True, თუ პროდუქტი მაცივარშია ("milk" in fridge).

# __str__() – "Fridge with N items".

# __del__() – "Fridge unplugged!".

# დაამატე პროდუქტები, შეამოწმე "milk" in fridge, დაბეჭდე ობიექტი და ბოლოს წაშალე.
print("------------------------------------------7---------------------------------------------------------------")  
class Refrigerator:
      def __init__(self,items):
            self.__items = items

      @property
      def get_items(self):
            return self.__items
      
      @get_items.setter
      def get_items(self,item):
            self.__items.append(item)
      
      def __contains__(self,item):
            return item in self.__items
      
      def __str__(self):
            return f"Fridge with {len(self.__items)} items"
      
      def __del__(self):
            return print(f"Fridge unplugged!")
      
rf = Refrigerator(["Yogurt","Eggs","Butter","Cheese"])
print(rf)
print(f"Orange in Refrigerator = {rf.__contains__("Orange")}") 
print(f"Eggs in Refrigerator = {rf.__contains__("Eggs")}")
rf.get_items = "Milk"
print(f"Milk in Refrigerator = {rf.__contains__("Milk")}") 
print(rf.get_items)
del rf

      
                  

# #8 ამოცანა 8
# შექმენი კლასი FunnyCalculator, რომელსაც ექნება:

# __add__() – აბრუნებს "Why are you adding numbers? Just buy a calculator".

# __mul__() – აბრუნებს "Multiplication is too mainstream...".

# __truediv__() – თუ გაყოფ 0-ზე, ბეჭდავს "ZeroDivisionError? Nah, let’s just say infinity"

# __str__() – "I’m the funniest calculator in Python!".

# ცადე calc + 5, calc * 2, 10 / calc და ნახე რა მოხდება.
print("------------------------------------------8---------------------------------------------------------------")  
class FunnyCalculator:     
    def __add__(self,num):
        return f"Why are you adding numbers? Just buy a calculator"
    def __mul__(self,num):
        return f"Multiplication is too mainstream..."
    def __truediv__(self, num):
        return f"ZeroDivisionError? Nah, let’s just say infinity {num}"
    def __rtruediv__(self,num):
        return f"ZeroDivisionError? Nah, let’s just say infinity {num}"
    def __str__(self):
        return f"I\’m the funniest calculator in Python!"
    # ეს მეთოდი მუშაობს & ნიშანზე
    def __and__(self, text):
        return f"Logical AND with '{text}'? Always True... just like your bad math skills."
    def __matmul__(self,mail):
        return f"აქ მგონი ყველაფერი მუშაობს! {mail}"
    
calc = FunnyCalculator()
print(calc+5) #FunnyCalculator()__add__(5)
print(calc*2) #FunnyCalculator()__mul__(2)
print(calc/0) #FunnyCalculator()__truediv__(0)
print(10/calc) #FunnyCalculator()__rtruediv__(10)
print(calc & "something") #FunnyCalculator()__and__("something")
print(calc @ "my@mail.me") #FunnyCalculator()__matmul__("my@mayl.me")
    