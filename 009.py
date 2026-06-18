# #1 შექმენი თამაში
# შექმენით Character კლასი (სახელი, სიცოცხლე, ძალა)
# გააკეთეთ მემკვიდრეები: Warrior, Mage, Archer
# გამოიყენეთ super() რომ მშობლის კონსტრუქტორი გამოიძახოთ
# თამაში: ორი გმირი ებრძვის ერთმანეთს (attack() მეთოდი).
# Warrior სჯობს Mage-ს , Mage სჯობს Archer-ს, Archer სჯობს Warrior-ს
# ტესტირების დროს სცადე სამივე ვარიანტი, ანუ როცა ერთმანეთზე გააკეთებინებ შეტევას 1 უნდა
# დამარცხდეს და 1მა გაიმარჯვოს, ეს უნდა გამოიტანო ტერმინალში. ზედმეტი ვალიდაციები და
# პირობის შეცვლა არაა საჭირო. რაც პირობაში წერია ამ მონახაზით გააკეთეთ თავისუფლად.
print("-----------------------------------1-----------------------------------------\n")
import itertools
import random


class Character:
    def __init__(self,name,hp,stre):
        self.__name = name
        self.__hp = hp
        self.__stre = stre

    def attack(frst,sec):
        return frst > sec
    
    @property
    def name(self):
        return self.__class__.__name__

    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_hp(self):
        return self.__hp
    
    @property
    def get_stre(self):
        return self.__stre
   
    def attack(self, opponent):      
        if self.name == "Warrior" and opponent.name == "Mage":
            return True
        if self.name == "Mage" and opponent.name == "Archer":
            return True
        if self.name == "Archer" and opponent.name == "Warrior":
            return True
            
        # პირიქით
        if opponent.name == "Warrior" and self.name == "Mage":
            return False
        if opponent.name == "Mage" and self.name == "Archer":
            return False
        if opponent.name == "Archer" and self.name == "Warrior":
            return False
        # კლასები თანაბარია, ვადარებთ პარამეტრებს
        return (self.__hp + self.__stre) > (opponent.__hp + opponent.__stre)


class Warrior(Character):
    def __init__(self,name,hp,stre):
        super().__init__(name,hp,stre)

class Mage(Character):
    def __init__(self,name,hp,stre):
        super().__init__(name,hp,stre)

class Archer(Character):
    def __init__(self,name,hp,stre):
        super().__init__(name,hp,stre)  


warior = Warrior("მეომარი",150,40)
mage = Mage("ჯადოქარი",80,60)
mage1 = Mage("ჯადოქარი 1",85,60)
archer = Archer("მშვილდოსანი",100,50)

res = [(warior,mage,warior.attack(mage)), # Warrior vs Mage
       (mage,archer,mage.attack(archer)), # Mage vs Archer-ს
       (archer,warior,archer.attack(warior)), # Archer vs Warrior
       (mage,mage1,mage.attack(mage1)) # Mage vs Mage1
       ]

msg = ""
for i in res:
    if i[2]:
       msg = f"{i[0].get_name} vs {i[1].get_name}; გამარჯვებულია: {i[0].get_name}"
    else:
        msg = f"{i[0].get_name} vs {i[1].get_name}; გამარჯვებულია: {i[1].get_name}"  
    print(msg)     


# #2 პატარა პროგრამა მონსტრებზე
# თქვენი ვალია შექმნათ მონსტრების ქარხანა სადაც:
# შექმენით Monster კლასი.
# დაამატეთ classmethod create_from_level(level), რომელიც ქმნის მონსტრს სიძლიერის
# მიხედვით.
# სხვადასხვა level -> სხვადასხვა ტიპის მონსტრი.
# შექმენი მინიმუმ 10 მონსტრი რომლებსაც ექნებათ სახელები, სახელები არ უნდა იყოს ბოროტული :)
# (ეს მონსტრები ეხმარებიან ადამიანებს) “აქაც იგივე” არაა საჭირო ზედმეტი ვალიდაციები და პირობის
# ცვლილება. ამ მონახაზში იმუშავეთ თავისუფლად.
print("-----------------------------------2-----------------------------------------\n")
class Monster:
    def __init__(self,name,power):
        self.__name = name
        self.__power = power

    @classmethod
    def create_from_level(cls,level):
        power =  random.randint(10**(level-1),10**level-1)
        monsters = ["Medusa","Python","Minotaur","Cerberus","Hydra","Giants","Typhon","Sirens","Lamia","Sphinx"] 
        name = random.sample(monsters,k=1)
        return cls(name,power) 

    def __str__(self):
        return f" {self.__name} (PW: {self.__power})"   
    
## Print all Monsters   
for i in range(1,11):     
      m = Monster.create_from_level(i)
      print(m)

# #3 მარტივი კაზინო თამაში
# შექმენით SlotMachine კლასი.
# გამოიყენეთ staticmethod შემთხვევითი სიმბოლოების დასაგენერირებლად.
# გამოიყენეთ classmethod from_difficulty(level) -> უფრო რთული დონის სლოტები
# მოთამაშე მოიგებს თუ სამივე სიმბოლო დაემთხვევა.
print("-----------------------------------3-----------------------------------------\n")
class SlotMachine:

    def __init__(self,level):        
        self.__level  = level
        self.__combos = None
        #                 x500   x50    x30   x20    x10    x5    x5     x5            
        self.__symbols = ['🚀', '⭐', '🍀', '💎', '✨', '🌍', '🎯', '⚡']  
        self.__weights = [ 5,    10,    15,   20,    50,   75,    75,    75 ]
        self.__win =    ["x500","x50","x30"  ,"x20","x10","x5",  "x5",  "x5"]        

    @staticmethod
    def list_all_syms(symbols,w):          
      
       combos = random.choices(symbols, weights=w, k=3)
       ## Check random Win
       if len(set(combos)) == 1:            
             combos = random.choices(symbols, weights=w, k=3)       
       return combos
    
    # Spin 
    def spin(self):
         self.__combos = self.list_all_syms(self.__symbols,self.__weights)
         rdInt = random.randint(1, 100)
         # Max Win %
         max_win_pec = 55
         # % by Level
         perc = max_win_pec - self.__level*5 # detect win % 
         is_winning_spin = rdInt <= perc # detect Win   
         msg = f"  rand = {rdInt}\n  perc = {perc}%\n  Win Status = {is_winning_spin} You Lost\n"             
         if is_winning_spin:
        # თუ მოგებაა, ვირჩევთ 1 შემთხვევით სიმბოლოს და ვამრავლებთ 3-ზე
           win_sym = random.choice(self.__combos)
           idx = self.__symbols.index(win_sym)
           self.__combos = [win_sym]*3 
           msg = f"  rand = {rdInt}\n  perc = {perc}%\n  Win Status = {is_winning_spin} You Win {self.__win[idx]}\n"        
         print(msg)                 
         return self.__combos        

    @classmethod
    def from_difficulty(cls,level):
        if level > 10:
             level = 10
        return cls(level)
    
    def __str__(self):
        return f" {self.__combos}\n------------------" 
    
## Test
for i in range(1,10):     
      game = SlotMachine.from_difficulty(i)
      spin = game.spin()
      print(f" {game}")
# აუცილებლად გატესტეთ, სცადეთ რამოდენიმე ვარიანტის გაშვება.

# #4 გმირის ქულების სისტემა
# შექმენით Hero კლასი.
# private health, private score.
# staticmethod random_event() -> შემთხვევითი მოვლენა (ქულა ემატება ან ჯანმრთელობა
# აკლდება).

# classmethod from_name(cls, name) -> ქმნის გმირს სახელით.
# მემკვიდრე SuperHero -> დამატებითი ძალა.
# super() გამოიძახეთ მშობლის კონსტრუქტორისთვის.
# თამაში გრძელდება სანამ გმირის health > 0.
print("-----------------------------------4-----------------------------------------\n")
class Hero:
    def __init__(self,name = None,health = None,score = None):

        self.name = name if name is not None else "Hero"
        self.__health = health if health is not None else 101
        self.__score = score if score is not None else 0

    @staticmethod
    def random_event():
        return random.choice([True, False]) 
    
    @classmethod
    def from_name(cls, name):        
        return cls(name)
    
    @property
    def get_health(self):
        return self.__health
    
    @get_health.setter
    def get_health(self,val):
         self.__health += val   
    
    @property
    def get_score(self):
        return self.__score  

    @get_score.setter
    def get_score(self,val):
         self.__score += val  
   
    
class SuperHero(Hero):
    def __init__(self, health=None, score=None):
        super().__init__(health, score) 
        
    # Add Health    
    def addHealth(self):
        self.get_health += self.get_health

class Fight():
    def __init__(self,hero1,hero2):        
        self.__h1 = hero1
        self.__h2 = hero2
       
    
    def start(self):  
        
        game_round = 0
        while self.__h1.get_health >= 0 and self.__h2.get_health >= 0:
                  
                  st1 = self.__h1.random_event()
                  st2 = self.__h2.random_event()
                  game_round += 1

                  if st1 and st2: # თუ 2 ვე True
                        self.__h1.get_score = 50
                        self.__h2.get_score = 50
                        msg = f"ამ რაუნდში გამარჯვებული არ არის +50 ქულა თითოეულს\n"
                        msg += f" {self.__h1.name}  health = {self.__h1.get_health} score = {self.__h1.get_score}\n"
                        msg += f" {self.__h2.name}  health = {self.__h2.get_health} score = {self.__h2.get_score}\n"
                  elif not st1 and not st2: # თუ 2 ვე False   
                        self.__h1.get_health = -25
                        self.__h2.get_health = -25
                        msg = f"ამ რაუნდში გამარჯვებული არ არის -25 ჯანმრთელობა თითოეულს\n"
                        msg += f" {self.__h1.name}  health = {self.__h1.get_health} score = {self.__h1.get_score}\n"
                        msg += f" {self.__h2.name}  health = {self.__h2.get_health} score = {self.__h2.get_score}\n"
                  elif st1 > st2:
                        self.__h1.get_score = 100
                        self.__h2.get_health = -50 
                        msg = f"ამ რაუნდის გამარჯვებულია {self.__h1.name}  health = {self.__h1.get_health} score = {self.__h1.get_score}\n"
                        msg += f" ამ რაუნდში დამარცხდა {self.__h2.name} health = {self.__h2.get_health} score = {self.__h2.get_score}"
                  elif st1 < st2:
                        self.__h2.get_score = 100
                        self.__h1.get_health = -50
                        msg = f"ამ რაუნდის გამარჯვებულია  {self.__h2.name} health = {self.__h2.get_health} score = {self.__h2.get_score}\n"
                        msg += f" ამ რაუნდში დამარცხდა {self.__h1.name} health = {self.__h1.get_health} score = {self.__h1.get_score}"
                                              
                  print(f"რაუნდი = {game_round}\n {msg}\n --------- ")
        else:
                       if self.__h1.get_health > self.__h2.get_health:
                        print(f"{game_round} რაუნდში ბრძოლაში გამარჯვებულია {self.__h1.name} health = {self.__h1.get_health} score = {self.__h1.get_score}")  
                        print(f"{game_round} რაუნდში ბრძოლაში  დამარცხდა {self.__h2.name} health = {self.__h2.get_health} score = {self.__h2.get_score}")
                       else:
                        print(f"{game_round} რაუნდში ბრძოლაში  გამარჯვებულია {self.__h2.name} health = {self.__h2.get_health} score = {self.__h2.get_score}") 
                        print(f"{game_round} რაუნდში ბრძოლაში დამარცხდა {self.__h1.name} health = {self.__h1.get_health} score = {self.__h1.get_score}")  
                        

    
    
he1 = Hero.from_name("ავთანდილი")
print(f"h1 {he1.name} healt= {he1.get_health} -- score = {he1.get_score}")
he2 = SuperHero.from_name("ტარიელი")
print(f"h2 {he2.name} health = {he2.get_health} -- score = {he2.get_score}")
he2.addHealth()
he3 = Hero("ფრიდონი")
print(f"h2 {he2.name} health = {he2.get_health} -- score = {he2.get_score}")
print(f"h3 {he3.name} health = {he3.get_health} -- score = {he3.get_score}\n ")

fg = Fight(he2,he3)

gm1 = fg.start()
# #5 პროგრამა კარტზე
# Card კლასი (rank, suit).
# Deck კლასი -> private cards list.
# classmethod create_standard_deck() აბრუნებს სტანდარტულ 52 კარტიან დასტას.
# staticmethod shuffle(cards) აურევს კარტებს.
# მოთამაშე იღებს 5 კარტს და ამოწმებს, აქვს თუ არა “მარტივი კომბინაცია” (მაგ: ორი ერთნაირი)
# აუცილებლად გატესტეთ კოდი, შეასრულეთ მხოლოდ პირობაში მოცემული ვარიანტი, არაა საჭირო
# დამატება.
print("-----------------------------------5-----------------------------------------\n")
class Card:
    def __init__(self):
        self.__suit = ['♠', '♥', '♦', '♣'] 
        self.__rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    @property
    def get_rank(self):
        return self.__rank

    @property
    def get_suit(self):
        return self.__suit    

class Desc:
    def __init__(self,cards):
        self.__cards = self.shuffle(cards)  


    @staticmethod 
    def shuffle(cards):
        return random.shuffle(cards)
    
    @classmethod
    def create_standard_deck(cls,cards):        
        deck_tuples = list(itertools.product(cards.get_rank, cards.get_suit))
        return deck_tuples
    
    ## Check
    def check_comb(crd):        
        return len(set(crd)) != len(crd)   
    
card = Card()
sdeck = Desc.create_standard_deck(card) 


# shuffle = Desc.shuffle(sdeck)
my_card = random.sample(sdeck,k=5)

my_card_show = [f"{mc[0]} {mc[1]} " for mc in my_card]
# my_card_suits = [card[1] for card in my_card]
my_card_ranks = [sdeck[0] for sdeck in my_card]

# check_suits = Desc.check_comb(my_card_suits)
check_ranks = Desc.check_comb(my_card_ranks)
# suit = {check_suits},
print(f" კომბინაცია  rank = {check_ranks}, ჩემი კარტი {my_card_show} \n")  