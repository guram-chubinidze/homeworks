# #1 ლაბირინთი
# გვაქვს მოცემული მსგავსი ლაბირინთი:
# maze = [
# ["S", ".", "#", ".", "."],
# ["#", ".", "#", ".", "#"],
# [".", ".", ".", ".", "."],
# ["#", "#", "#", ".", "#"],
# [".", ".", ".", ".", "E"]
# ]
# S -> არის საწყისი წერტილი
# E -> არის საბოლოო წერტილი
# # -> არის კედელი
# . -> არის გზა, რომელიც უნდა გაიაროს მომხმარებელმა
# თქვენი მიზანია დაწეროთ ლოგიკა სადაც მომხმარებელს შეეკითხებით რომელ მხარეს უნდა წასვლა:
# მაღლა, დაბლა, მარცხნივ, მარჯვნივ. თუ სწორად აირჩევს უნდა უთხრა რომ სწორად მიდის და კიდევ
# ჰკითხო ახლა რომელ მხარეს უნდა წასვლა, არასწორი გზის არჩევის შემთხვევაში უნდა დააწყებინო
# თავიდან თამაში და ისევ ჰკითხო სად წავა, თუ გავა ბოლოში უნდა დაუწერო რომ “შენ გაიარე
# ლაბირინთი” ვალიდაცია არაა საჭირო მომხმარებელს სწორად შეჰყავს სიტყვები.
print("--------------------------------------- 1 ------------------------------------------------\n")

class Labyrinth:
    def __init__(self):
        self.__maze = [["S", ".", "#", ".", "."],
                     ["#", ".", "#", ".", "#"],
                     [".", ".", ".", ".", "."],
                     ["#", "#", "#", ".", "#"],
                     [".", ".", ".", ".", "E"]]        
        self.__game_vars = {"way":"","vstep":0,"hstep":0,"status":"თამაშის დასაწყისი"}     

    # ხატავს ისრებს და ცვლის ინდექსებს ინპუტის მიხედვით
    def check_way(self,i_user):        
        if i_user == "l":
          self.__game_vars["hstep"] -= 1
          self.__game_vars["way"] += f"{chr(0x2190)} "
        elif i_user == "r":
          self.__game_vars["hstep"] += 1
          self.__game_vars["way"]+= f"{chr(0x2192)} "
        elif i_user == "u":
          self.__game_vars["vstep"] -= 1
          self.__game_vars["way"] += f"{chr(0x2191)} "
        elif i_user == "d":
          self.__game_vars["vstep"] += 1
          self.__game_vars["way"] += f"{chr(0x2193)} " 
        elif i_user == "e":
              print(f"თამაშის დასასრული!")
              exit()
        else:
           exit() 
        self.check_step()     

    # აქ ამოწმებს ნაბიჯებს
    def check_step(self):
      # საზღვრებს რო არ გაცდეს (წრეზე ივლის)  
      if self.__game_vars["vstep"] > 4 : self.__game_vars["vstep"] = 0 
      elif self.__game_vars["vstep"] < 0 : self.__game_vars["vstep"] = 4 
      if self.__game_vars["hstep"] > 4 : self.__game_vars["hstep"] = 0 
      elif self.__game_vars["hstep"] < 0 : self.__game_vars["hstep"] = 4

      # აქ ამოწმებს სად არის უკვე ინდექსებით  
      statusGame = self.__maze[self.__game_vars["vstep"]][self.__game_vars["hstep"]]   
      if statusGame == "#":  
        print(f"თქვენ დამარცხდით!\n-------------------------------------\nახალი თამაში\n")
        self.__game_vars = {"way":"","vstep":0,"hstep":0,"status":"თამაშის დასაწყისი"}  # თავიდან დაწყება       
      elif statusGame == "E":
        print("შენ გაიარე ლაბირინთი!\nთამაშის დასასრული!")
        exit()
      elif statusGame == "S":
        self.__game_vars["status"] = f"ახლა ისევ საწყის წერტილთან ხარ"
      elif statusGame == ".":
        self.__game_vars["status"] = f"სწორად მიდიხარ!" 
      else:
        print(f"თქვენ დამარცხდით! (აქეთ გზა აღარ არის)")    
      
    # თამაშის გაშვება
    def start(self):        
          print(f"{self.__game_vars["status"]}")
          while True:                 
                i_user = input('აირჩიეთ მიმართულება(l - მარცხნივ,r - მარჯვნივ, d - ქვემოთ, u - ზემოთ, e - დასრულება): ')
                self.check_way(i_user)
                print(f"{self.__game_vars["way"]}") # სიმბოლო  
                print(f"{self.__game_vars["status"]}") # ტექსტი  

game = Labyrinth()
game.start()
                   
     
                              



# #2 თამაში 1 VS 1
# თქვენი მიზანია შექმნათ თამაში სადაც ორი ადამიანი ეჯიბრება ერთმანეთს, მომხმარებელს უნდა
# ჰქონდეს 5-დან 1 მებრძოლის არჩევა: “გიგანტი”, “სწრაფი”, “მოქნილი”, “აქილევსი” & “პითონისტი”,
# თითოეულს გაუკეთეთ 3 შესაძლებლობა იგივე skill მაგალითად: ცეცხლის სროლა, ყონულის და ა.შ.
# სიცოცხლეები განსხვავებული უნდა ჰქონდეთ და ასევე დარტყმის ძალებიც.
# ჯერ პირველი მოთამაშეს ვარჩევინებთ გმირს, შემდეგ მეორეს (ერთნაირის არჩევა შეუძლიათ), მერე
# იწყებს პირველი მოთამაშე და ირჩევს ამ გმირზე რა სკილებიცაა იქიდან ერთს და ესვრის მეორეს,
# ასევე აკეთებს მეორე მოთამაშეც, ყოველ სროლაზე უნდა გამოუტანო დარჩენილი სიცოცხლე
# მოთამაშეს.
print("--------------------------------------- 2 ------------------------------------------------\n")
# მებრძოლები
# with open('warriors.json', 'r', encoding="utf-8") as jsfile:
#         warriors = json.load(jsfile)
warriors = [
  {
    "name"  : "გიგანტი",
    "health": 301,
    "skills": [
      {"name": "ქვის ფარი", "val":  50},
      {"name": "ქვის სროლა",                 "val": 100},
      {"name": "მიწისძვრა",                  "val": 150}
    ]
  },
  {
    "name"  : "სწრაფი",
    "health": 201,
    "skills": [
      {"name": "გაუჩინარება", "val":  75},
      {"name": "x2 დარტმა", "val": 125},
      {"name": "აკრობატიკა","val": 175}
    ]
  },
  {
    "name"  : "მოქნილი",
    "health": 201,
    "skills": [
      {"name": "ავტომატი", "val":  90},
      {"name": "ნაღმი","val": 300},
      {"name": "დრონი","val": 275}
    ]
  },
  {
    "name"  : "აქილევსი",
    "health": 501,
    "skills": [
      {"name": "მშვილდი","val": 30},
      {"name": "ხმალი","val": 50},
      {"name": "შუბი", "val": 75}
    ]
  },
  {
    "name"  : "პითონისტი",
    "health": 1,
    "skills": [
      {"name": "ასრულებს თამაშს","val": 0},
      {"name": "სქილის რევერსი","val": 1},
      {"name": "-99% სიცოცხლე მოწინააღმდეგეს","val":99}
    ]
  }
]
class Warior(ABC):

    def __init__(self,name,health):
        self._name = name
        self._health = health
        self._skills = []  

    @property
    @abstractmethod   
    def get_name(self):      
        pass 

    @property
    @abstractmethod   
    def get_health(self):      
        pass    

    @property
    @abstractmethod   
    def get_skills(self):      
        pass    

    @get_health.setter
    @abstractmethod   
    def get_health(self,change):      
        pass    

    @get_skills.setter
    @abstractmethod
    def get_skills(self,skills):      
        pass   

class Hero(Warior):
      
      def __init__(self,name,health):
          super().__init__(name,health) 

      @property
      def get_name(self):
          return self._name   
       
      @property
      def get_health(self):
          return self._health      

      @property
      def get_skills(self):
          return self._skills   
      
      @get_health.setter
      def get_health(self,change):           
           self._health += change
           
      @get_skills.setter
      def get_skills(self,skills): 
          self._skills = skills          
        #    for skill in skills:                         
        #        self._skills.append(skill) 


class Game:

    def __init__(self):
        self.__warriors = []
        self.__start_game = False
        self.__player1 = None
        self.__player2 = None

    # მებრძოლების შექმნა
    def generate_heroes(self,warriors):
        for warrior in warriors:
            h = Hero(warrior["name"],warrior["health"]) # სახელი, სიცოცხლე
            h.get_skills = warrior["skills"] # სქილების დამატება
            self.__warriors.append(h)
    # გმირების ჩვენება
    def _show_heroes(self):
     for idx,warrior in enumerate(self.__warriors):
                sk = [skill["name"] for skill in warrior.get_skills]
                print(f"{idx+1}. სახელი: {warrior.get_name}; სიცოცხლე:{warrior.get_health} სქილები: {sk}") 

    # თამაშის დასრულება
    def warrior_index(self,i_usr):
        if i_usr == "e":
            print(f"თამაში დასრულდა!")
            exit()
        return int(i_usr) -1    

    # თამაშის დაწყება
    def start(self,warriors):
        self.generate_heroes(warriors)
        self.__start_game = True        
        print(f"თამაშის დასაწყისი (e - დასრულება)")        
        while self.__start_game:
            print(f"გმირები: ")
            self._show_heroes()# გმირების ჩვენება
            i_player1 = input("აირჩიე გმირი (1,2,3,4,5):")
            idx1 = self.warrior_index(i_player1)
            self.__player1 = self.__warriors[idx1]           
            print(f"პირველმა მოთამაშემ აირჩია '{self.__player1.get_name}'")
            self._show_heroes()# გმირების ჩვენება
            i_player2 = input("აირჩიე გმირი (1,2,3,4,5):")
            idx2 = self.warrior_index(i_player2)
            self.__player2 = self.__warriors[idx2]
            print(f"მეორე მოთამაშემ აირჩია '{self.__player2.get_name}'")
            print(f"იწყება ბრძოლა {self.__player1.get_name} vs {self.__player2.get_name}\n -------")            
            break

        self.fight()
    # არჩევა
    def fight(self):  
          
          f_round = 1
          skill_names1 = [skill["name"] for skill in self.__player1.get_skills]
          skill_names2 = [skill["name"] for skill in self.__player2.get_skills]
          while self.__player1.get_health >= 0 or self.__player2.get_health >= 0:
              print(f"------------------\nრაუნდი {f_round}")
              i_skill1 = int(input(f"პირველი მოთამაშე\n აირჩიე სქილი (1,2 ან 3): {skill_names1} "))-1
              i_skill2 = int(input(f"მეორე მოთამაშე\n აირჩიე სქილი (1,2 ან 3): {skill_names2} "))-1
              if i_skill1 > 2 or i_skill1< 0 or i_skill2 > 2 or i_skill2< 0:
                   print(f" აირჩიე 1 დან 3 მდე")
                   continue
              self.battle(i_skill1,i_skill2)
             

              f_round += 1
    # შედეგები
    def show_result(self,at1,at2):
        print(f"შედეგები:")
        print(f"პირველი მოთამაშე {self.__player1.get_name}: ჯანმრთელობა: {self.__player1.get_health} ზიანი:-{at2}")
        print(f"მეორე მოთამაშე {self.__player2.get_name}: ჯანმრთელობა: {self.__player2.get_health} ზიანი:-{at1}")

    # ბრძოლა
    def battle(self,i_skill1,i_skill2):
        
        at1 = self.__player1.get_skills[i_skill1]["val"]
        at2 = self.__player2.get_skills[i_skill2]["val"]       
        if self.__player1.get_name != "პითონისტი" and self.__player2.get_name != "პითონისტი":         
            self.__player1.get_health =  -at2
            self.__player2.get_health =  -at1 
            self.show_result(at1,at2)   
            if self.__player2.get_health <= 0:
                print(f"გაიმარჯვა პირველმა მოთამაშემ '{ self.__player1.get_name}'")
                exit()
            elif self.__player1.get_health <= 0:   
              print(f"გაიმარჯვა მეორე მოთამაშემ '{ self.__player2.get_name}'") 
              exit()          
        elif self.__player1.get_name == "პითონისტი" and self.__player2.get_name != "პითონისტი":
               if at1 == 0:
                   print(f" თამაში დასრულდა. გაიმარჯვა პითონისტმა!")
                   exit()
               elif at1 == 1:
                   self.__player2.get_health =  -at2 
                   self.show_result(at1,at2)   
               else:
                    at1 = self.__player1.get_skills[i_skill1]["val"]
                    at2 = self.__player2.get_skills[i_skill2]["val"]  
                    self.__player1.get_health =  -at2
                    self.__player2.get_health =  -at1/100*self.__player2.get_health 
               self.show_result(at1,at2)        
               if self.__player1.get_health <= 0 or self.__player2.get_health <= 0:
                      print(f"გაიმარჯვა პირველმა მოთამაშემ '{ self.__player1.get_name}'") 
                      exit()   
        elif self.__player1.get_name != "პითონისტი" and self.__player2.get_name == "პითონისტი":
               if at2 == 0:
                   print(f" თამაში დასრულდა. გაიმარჯვა პითონისტმა!")
                   exit()
               elif at2 == 1:
                   self.__player1.get_health =  -at1 
                   self.show_result(at1,at2)   
               else:
                    at1 = self.__player1.get_skills[i_skill1]["val"]
                    at2 = self.__player2.get_skills[i_skill2]["val"] 
                    self.__player1.get_health =  -at2/100*self.__player1.get_health
                    self.__player2.get_health =  -at1 
                    self.show_result(at1,at2)    
                    if self.__player2.get_health <= 0 or self.__player1.get_health <= 0:
                      print(f"გაიმარჯვა მეორე მოთამაშემ '{ self.__player2.get_name}'") 
                      exit()  
        else:     
                print(f"at1 = {at1} and at2 = {at2}")      
                if at1 == 0 or at2 == 0:
                   print(f" თამაში დასრულდა. გაიმარჯვა პითონისტმა!")
                   exit()
                elif at1 == 1: 
                  self.__player2.get_health =  -at2 
                  self.show_result(at1,at2)   
                elif at2 == 1:
                   self.__player1.get_health =  -at1 
                   self.show_result(at1,at2)   
                else:
                    at1 = self.__player1.get_skills[i_skill1]["val"]
                    at2 = self.__player2.get_skills[i_skill2]["val"]
                    self.__player1.get_health =  -at2*self.__player1.get_health/100
                    self.__player2.get_health =  -at1*self.__player2.get_health/100 
                    self.show_result(at1,at2)  

gm = Game()
gm.start(warriors)
# #3
# შექმენით Earth კლასი, რომელიც იქნება მშობელი მინიმუმ 3 შვილის, თქვენი სურვილით უნდა
# დაწეროთ ისეთი ლოგიკა ამ კლასში რომ გამოყენებული გქონდეთ ობიექტზე ორიენტირებული
# პროგრამირების 4 პრინციპი, აბსტრაქცია, პოლიმორფიზმი, მრავალჯერადი მემკვიდრეობა &
# ენკაფსულაცია, შიდა ლოგიკა უნდა იყოს თანმიმდევრული, ანუ მაგალითად: class Animal-ში არ უნდა
# შეინახოთ შვილობილი class Engine. თავისუფალი ხართ შიგნით რას ჩაწერთ.
class  Planet(ABC):
    @abstractmethod
    def get_info(self):
        pass

class Life:
    def __init__(self):
        self.__inhabitants = ["ბაქტერიები", "სოკოები", "მცენარეები", "ცხოველები"] 

    @property
    def get_inhabitants(self):
        return self.__inhabitants

    @get_inhabitants.setter
    def get_inhabitants(self, new_organism):
        self.__inhabitants.append(new_organism)  
        
class Earth(Planet):
    def __init__(self):       
        self._name = "დედამიწა"        

    def get_info(self):
        return f"ეს არის პლანეტა: {self._name}"

class Air(Earth):
    def __init__(self, oxygen,percent):
        super().__init__() 
        self.__oxygen = oxygen
        self.__percent = percent

    def get_info(self):       
        print(f"{self._name}ზე: {self.__oxygen} დონე არის {self.__percent}")

    @classmethod
    def create_air(cls,oxygen,percent):
        per = str(percent)+"%"
        return cls(oxygen,per)   

class Water(Earth):
    def __init__(self, part, percent):
        super().__init__()
        self.__part = part
        self.__percent = percent

    def get_info(self):
        print(f"{self.__part} იკავებს {self._name[:-1]}ის {self.__percent}% ს.")

class Land(Earth,Life):
    def __init__(self, continent):
        super().__init__()
        self.__continent = continent

    def get_info(self):
        life = Life()
        life.get_inhabitants = "ადამიანები"
        print(f"{self._name}_ზე არის {self.__continent} კონტინენტი. აქ ცხოვრობენ: {life.get_inhabitants}")

earth = Earth().get_info()
oxygen = Air.create_air("ჟანგბადი",21)
nitrogen = Air.create_air("აზოტი",79)
print(earth)
oxygen.get_info()
nitrogen.get_info()
water = Water("წყალი",70)
water.get_info()
land = Land(7)
land.get_info()

print("--------------------------------------- 3 ------------------------------------------------\n")
# #4 ჯადოქარი
# მომხმარებელს აქვს 5 ინგრედიენტი: “ღამურა” , “ბუმბული”, “ვაშლი”, “ყვავილი”, “წყალი”. შეუძლია
# მხოლოდ 2-ის არჩევა და “მოხარშვა” ამ ორიდან უნდა გამოვიდეს რაღაც მაგალითად: “ვაშლი” +
# “წყალი” = “ვაშლის წვენი” და ასე შემდეგ.ყველა კომბინაცია უნდა იყოს განსხვავებული.
class Magician:
    def __init__(self):
        self.__ingredients = ["ღამურა", "ბუმბული", "ვაშლი", "ყვავილი", "წყალი"]
        self.__chosen_ings = []
        self.__products = [
            ["ბეტმენი","ბალიში","საწამლავი","ტეკილა","კოქტეილი"],
            ["ბალიში","ინდიელის ქუდი","სიდრი","ტატუ","კალამი"],
            ["საწამლავი","სიდრი","აიფონი","სუნამო","წვენი"],
            ["ტეკილა","ტატუ","სუნამო","თაფლი","გვირილის ჩაი"],
            ["კოქტეილი","კალამი","წვენი","გვირილის ჩაი","არაყი"]
        ]
        self.__game = True      

    def choose_ingredients(self):
        print(f"ინგრედიენტები(1,2,3,4,5, e - დასრულება)")
        while self.__game:
            i1 = input(f" აირჩიეთ:\n {self.__ingredients} (მაგალითად 1,3) : ")
            if i1.strip() == "e":
                print(f"თამაშის დასასრული")
                exit()
            chosen_ings = list(i1)
            del chosen_ings[1]
            self.__chosen_ings = chosen_ings
            print(self.__chosen_ings)
            reuslt = self.make() 
            print(f"გამოვიდა: {reuslt}\n --------------------- ")

    def make(self):
        key1 = int(self.__chosen_ings[0])-1
        key2 = int(self.__chosen_ings[1])-1
        print(f"არჩეული ინგრედიენტები: {self.__ingredients[key1]} და {self.__ingredients[key2]}")
        return self.__products[key1][key2]
    
mag = Magician().choose_ingredients()     
print("--------------------------------------- 4 ------------------------------------------------\n")
# #5 ტრანსპორტირების სისტემა
# უნდა ავაწყოთ სისტემა, სადაც სხვადასხვა ტრანსპორტი (Car, Bus, Bike) იმართება ერთიანი
# კლასით Transport
# - ყველა ტრანსპორტს აქვს fuel, speed, capacity.
# - არის აბსტრაქტული მეთოდი move().
# - ყოველი transport სხვადასხვა წესით ხარჯავს საწვავს (პოლიმორფიზმი).
# - fuel ინახება private (ენკაფსულაცია).
# - ყველა transport იღებს ძირითად ფუნქციონალს Transport-იდან.(მემკვიდრეობა)
print("--------------------------------------- 5 ------------------------------------------------\n")
class Transport:
    def __init__(self,fuel, speed, capacity):
        self.__fuel = fuel
        self.speed = speed
        self.capacity = capacity

    @property
    def get_fuel(self):
        return self.__fuel    

    @abstractmethod
    def move(self,distance):
        pass  

    def fuel_per_l100km(self,unit,distance):
        return f" {round(unit/distance*100,2)} {self.__fuel} per 100 km"
    
    def mpg(self,distance,quantity):
        return f" {round(distance/quantity,2)} mpg {self.__fuel}"
    
    def price_per_person(self,total):
        return round(total/self.capacity,2)
    
    def travel_time(self,distance):
        return f" {distance//self.speed} hour and {round((distance % self.speed/self.speed*60))} min"  

class Car(Transport):
    def __init__(self,fuel,speed,capacity,galon,total):
        super().__init__(fuel,speed,capacity)
        self.__galon = galon
        self.__total = total
       
    
    def move(self,distance):
        exp_fuel = self.mpg(distance,self.__galon)
        exp_per_person = str(self.price_per_person(self.__total))+" $ ხარჯი 1 ადამიანზე" 
        tr_time = self.travel_time(distance)        
        print(f" ავტომობილით:\n {self.capacity} ადამიანი\n{exp_fuel}\n {exp_per_person}\n{tr_time}\n--------------")
    
class Bus(Transport):
    def __init__(self,fuel,speed,capacity,unit,total):
        super().__init__(fuel,speed,capacity)
        self.__unit = unit
        self.__total = total
        
    
    def move(self,distance):
        exp_fuel = self.fuel_per_l100km(self.__unit,distance)
        exp_per_person = str(self.price_per_person(self.__total))+" $ ხარჯი 1 ადამიანზე" 
        tr_time = self.travel_time(distance)        
        print(f" ავტობუსით:\n {self.capacity} ადამიანი\n{exp_fuel}\n {exp_per_person}\n{tr_time}")
    
class Bike(Transport):
    def __init__(self,fuel,speed,capacity,unit,total):
        super().__init__(fuel,speed,capacity)
        self.__unit = unit
        self.__total = total
    
    def move(self,distance):
        exp_fuel = self.fuel_per_l100km(self.__unit,distance)
        exp_per_person = str(self.price_per_person(self.__total))+" $ ხარჯი 1 ადამიანზე" 
        tr_time = self.travel_time(distance)        
        print(f" მოტოციკლით:\n {self.capacity} ადამიანი\n{exp_fuel}\n {exp_per_person}\n{tr_time}")

distance = 400
data = [{"fuel":"Petrol","speed":105,"capacity":4,"fuel_unit":5,"cost":150},  # Car
        {"fuel":"diesel","speed":85,"capacity":40,"fuel_unit":65,"cost":350}, # Bus
        {"fuel":"Petrol","speed":130,"capacity":2,"fuel_unit":10,"cost":30}]  # Bike

car = Car(data[0]["fuel"],data[0]["speed"],data[0]["capacity"],data[0]["fuel_unit"],data[0]["cost"]) # Fuel, Speed, capacity, 
car.move(distance)
bus = Bus(data[1]["fuel"],data[1]["speed"],data[1]["capacity"],data[1]["fuel_unit"],data[1]["cost"])
bus.move(distance)
bike = Bike(data[2]["fuel"],data[2]["speed"],data[2]["capacity"],data[2]["fuel_unit"],data[2]["cost"])
bike.move(distance)
