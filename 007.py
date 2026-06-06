# #1 შექმენი გენერატორი, რომელიც ტექსტის თითოეულ სიმბოლოს აბრუნებს.
# Word = “CODE”
word = "CODE"
## function print_code @word
def print_code(word):
    for i in range(len(word)):    
     yield word[i]
     
pr_code = print_code(word)

for i in pr_code:
   print(i)


# #2 დაწერე პროგრამა რომელშიც მომხმარებელი შემოიყვანს მხოლოდ ციფრებს, ლოგიკა
# უნდა იყოს შემდეგი: გვაქვს კონკრეტული ლისტი და მომხმარებელი უნდა მიწვდეს
# შემოყვანილი ციფრით რომელიმე ელემენტს, თუ ვერ მიწვდება პროგრამა შეცდომაზე არ
# უნდა გავიდეს.
# arr = [1, 2, 3,4,5,6,7,8,9]
arr = [1,2,3,4,5,6,7,8,9]
i_number = input("შეიყვანეთ ინდექსი(მხოლოდ ციფრი): ")

try:
   i_number = int(i_number)
   print(arr[i_number])
except Exception as e:
   print(f"მოხდე შეცდომა: {e}")


# #3 შექმენი დეკორატორი, რომელიც ითვლის რამდენჯერ გამოიძახეს ფუნქცია.
# მაგალითი:
# @counter
# def say():
# print("Hi")
# say()
# say()
# გამოძახება: 1
# Hi
# გამოძახება: 2
# Hi

## Decorator
def counter(func):
   i = 0
   def wrapper(): 
       nonlocal i 
       i += 1           
       print(f"გამოძახება: {i}")
       func()    
   return wrapper   
   
## say Function
@counter
def say():
 print("Hi")

say()
say()
# გამოძახება: 1
# Hi
# გამოძახება: 2
# Hi

# #4 მომხმარებელს უნდა დავუსვათ 5 მათემატიკური შეკითხვა, თითოეულზე სწორი
# პასუხი არის 10 ქულა ხოლო არასწორი 0 ქულა, მიღებული პასუხებიდან უნდა
# განვსაზღვროთ რამდენი ქულა აიღო მომხმარებელმა, შევქმნათ ლოფ ფაილი
# game.log და შევინახოთ ყველა ქულა. ბოლოს გამოვუტანოთ მიღებული შედეგი

import logging
import random

## config logger
logging.basicConfig(
    filename='game.log',
    filemode='a',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    #force=True
)

count_questions = 5 
points_per_que = 10
total_points = 0 
operators = ['+', '-', '*', "//"]

## calculate
def calculate(a,b,op):
    res = 0
    try:        
        if op == '+':
            res = a + b 
        elif op == '-':
            res = a - b
        elif op == '*':
            res = a * b
        elif op == '//':
            res = int(a // b)
    except Exception as e:
        logging.warning("დაფიქსირდა შეცდომა: {e}")
        print(f"მოხდა შეცდომა {e}")   
    finally:
        if isinstance(res, int): 
           res =  int(res) 
    return res

## check input value
def check_input_val(i_val):
    try:
      i_val = int(i_val)
    except Exception as e:
        print(f"შეიყვანეთ კორექტული მონაცემები! {e}")
        logging.warning(f"მომხმარებელმა შეიყვანა არასწორი მონაცემები!: {e}")
    return i_val  
    
i = 1
while i < count_questions+1:
    #logging.info()
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    if num2 == 0 or num2 < num1:
       chosen_operator = random.choice(operators[:-1])        
    else:
          chosen_operator = random.choice(operators)
    print(f"Question {i}) What is {num1} {chosen_operator} {num2}?")
    logging.info(f"Question {i}) What is {num1} {chosen_operator} {num2}?")
    i_answer = input("პასუხი: ")    
    i_answer = check_input_val(i_answer)
    if isinstance(i_answer,str):
        continue     
    else:
        true_answ = calculate(num1,num2,chosen_operator)
        if i_answer == true_answ:
            total_points += points_per_que
            logging.info(f"answer to question {i}): {i_answer} Correct")
        else:
            logging.info(f"answer to question {i}): {i_answer} Wrong")     
        
        logging.info(f"Total Points: {total_points}")
        i += 1
       
     
print(f"სულ ქულების რაოდენობა = {total_points}") 

# #5 შექმენით ფაილი quiz.log, შექმენით გენერატორი რომელშიც შენახული იქნება
# 5 შეკითხვა და სათითაოდ დააბრუნებს, მომხმარებელმა უნდა უპასუხოს ყველა
# შეკითხვას და პასუხები შეინახეთ ლოგ ფაილში.
import logging

logging.basicConfig(
    filename='quiz.log',
    filemode='a',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
## question generator
def q_generator():
    yield "1. რომელია logging მოდულში  ყველაზე მაღალი და ყველაზე დაბალი პრიორიტეტის დონე(Log Levels)?"
    yield "2. რა არის logging მოდულის დეფოლტ (Default) დონე?"
    yield "3. რას აკეთებს `yield` ოპერატორი ფუნქციაში?"
    yield "4. რა არის დეკორატორი (Decorator) Python-ში?"
    yield "5. რა მოხდება, თუ კოდში დავწერთ logging.error()-ს?"

# show questions
for question in q_generator():    
    i_answ = input(f"{question}: ")
    logging.info(i_answ)

# #6 შექმენი პროგრამა სადაც მომხმარებელი ეჯიბრება კომპიუტერს: ქვა/ბადე/
# მაკრატელის თამაშში, თამაში არის სამამდე, კომპიუტერი შემთხვევითობის

# პრინციპით ირჩევს ამ სამიდან 1-ს , ასევე ტერმინალში მომხმარებელი წერს ერთ-
# ერთს, ერთნაირის შემთხვევაში ფრეა და გრძელდება თამაში 3-მდე, ვინც პირველი

# მიაღწევს 3-ს გამოიტანე შეტყობინება .....-მ გაიმარჯვა, ყველა ნათამაშები ხელი
# უნდა შეინახოო ლოგირების ფაილში.

import logging
import random

game_opts = {1:"ქვა",2:"ბადე",3:"მაკრატელი"}

def cal_points(a,b):
    if   a == 1 and b == 2:
        return b
    elif a == 1 and b == 3:
        return a
    elif a == 2 and b == 3:
        return b
    elif a == 2 and b == 1:
        return b
    elif a == 3 and b == 1:
        return b
    elif a == 3 and b == 2:
        return b
    elif a == b:
        return 0
    

logging.basicConfig(
    filename='game1.log',
    filemode='a',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding='utf-8' 
)

game_level = 3
com_points = 0
usr_points = 0
strGame = True
while com_points < 3 or usr_points < 3:
    if com_points == 3:
        print(f"თამაშის გამარჯვებულია კომპიუტერი. ანგარიში:\n კომპიუტერი {com_points} vs მომხმარებელი {usr_points}")
        logging.info(f"თამაშის გამარჯვებულია კომპიუტერი. ანგარიში:\n კომპიუტერი {com_points} vs მომხმარებელი {usr_points}")
        break
    elif usr_points == 3:
        print(f"თამაშის გამარჯვებულია მომხმარებელი. ანგარიში:\n მომხმარებელი {usr_points} vs კომპიუტერი {com_points}")
        logging.info(f"თამაშის გამარჯვებულია მომხმარებელი. ანგარიში:\n მომხმარებელი {usr_points} vs კომპიუტერი {com_points}")
        break

    com_choice = random.choice(list(game_opts.keys()))
    usr_choice = input("აირჩიეთ:\n 1) ქვა\n 2) ბადე\n 3) მაკრატელი\n")
    try:
        usr_choice = int(usr_choice)
        res = cal_points(com_choice,usr_choice)
        logging.info(f"კომპიუტერის არჩევანია {game_opts[com_choice]} მომხმარებელმა აირჩია {game_opts[usr_choice]}")        
        if res == com_choice:
            com_points += 1
            print(f"რაუნდის გამარჯვებულია კომპიუტერი. დაემატა 1 ქულა. სულ ქულა {com_points}")
            logging.info(f"რაუნდის გამარჯვებულია კომპიუტერი. დაემატა 1 ქულა. სულ ქულა {com_points}")
        elif res == usr_choice:
            usr_points += 1
            print(f"რაუნდის გამარჯვებულია მომხმარებელი. დაემატა 1 ქულა. სულ ქულა {usr_points}")
            logging.info(f"რაუნდის გამარჯვებულია მომხმარებელი. დაემატა 1 ქულა. სულ ქულა {usr_points}")
        else:
            print(f"რაუნდი დასრულდა ფრედ.")
            logging.info(f"რაუნდი დასრულდა ფრედ. ანგარიშია -\n კომპიუტერი: {com_points} vs მომხმარებელი {usr_points}")
            
        print(f" კომპიუტერი: '{game_opts[com_choice]}' vs მომხმარებელი '{game_opts[usr_choice]}'.\n ანგარიშია \n კომპიუტერი: {com_points} vs მომხმარებელი {usr_points}")        
    except Exception as e:
           print(f" შეიყვანეთ მხოლოდ ციფრები: 1,2 ან 3")   

# #7 პროგრამა კამათელზე - გვყავს ორი მომხმარებელი Gamer 1 & Gamer 2,
# თითოეულს უნდა გავაგორებინოთ კამათელი თითო თითოჯერ, თუ ფრეა ვიმეორებთ,
# სხვა შემთხვევაში მოგებულ მოთამაშეს უნდა ვკითხოთ კიდევ 1 შანსს მისცემს თუ
# არა წაგებულს და კიდევ გააგორებს თუ არა, თუ უარია ვამთავრებთ, თუ თანახმაა
# იგივე ლოგიკა უნდა გაგრძელდეს სანამ უარს არ იტყვის ერთ-ერთი.
import random

dc = [1,2,3,4,5,6]
str_dc_game = True
while str_dc_game:
    
        g1 = input("Roll Gamer 1(enter): ")
        g1_choice = random.choice(dc)
        print(f"Gamer 1 rolled a {g1_choice}")
        g2 = input("Roll Gamer 2(enter): ")
        g2_choice = random.randint(1,6)
        print(f"Gamer 2 rolled a {g2_choice}")  
        if g1_choice == g2_choice:
            print(f"შედეგი: ფრე Gamer 1 = {g1_choice} Gamer 2 = {g2_choice}")
            continue 
        elif g1_choice > g2_choice:
         print(f"შედეგი: Gamer 1 გაიმარჯვა. Gamer 1 = {g1_choice} Gamer 2 = {g2_choice}")
         g1_cont = input(f"მისცემთ კიდევ 1 შანსს Gamer 2 ს? (Y/n) ") 
         if g1_cont == 'n':
            break 
         else:
            g2_ask = input("Gamer 2 კიდევ გააგორებ?")
            if g2_ask == 'n':
               break       
        elif g2_choice > g1_choice:
         print(f"შედეგი: Gamer 2 გაიმარჯვა. Gamer 2 = {g2_choice} Gamer 1 = {g1_choice}")
         g2_cont = input(f"მისცემთ კიდევ 1 შანსს Gamer 1 ს? (Y/n) ") 
         if g2_cont == 'n':
            break 
         else:
            g1_ask = input("Gamer 1 კიდევ გააგორებ?")
            if g1_ask == 'n':
               break  

# #8 შექმენი პროგრამა სადაც გექნება გადაცემული 10 სიტყვა ლისტში და ლოგიკა
# არის შემდეგი, ამ სიტყვებიდან 2 ცალს ირჩევ შემთხვევითობის პრინციპით და
# თითოეული სიტყვიდან უნდა ამოაკლო 2 ასო და მომხმარებელს აჩვენო მსგავსი
# ფორმით და უთხრა რომ გამოიცნოს სიტყვა და ჩაწეროს სრულად, თუ გამოიცნო
# “გამარჯვება” თუ ვერ გამოიცნო ვერცერთი სიტყვა “დამარცხდი”, ერთის
# გამოცნობის შემთხვევაში “50%”
import random


fruits = ["apple","banana", "orange", "mango", "watermelon","grape", "peach", "cherry", "fig", "kiwi"]

random_fruits = random.choices(fruits, k=2)

w1 = random_fruits[0]
w2 = random_fruits[1]
w1_l = list(w1)
w2_l = list(w2)

random_indexes_w1 = random.sample(range(len(w1)), 2)
random_indexes_w2 = random.sample(range(len(w2)), 2)

## change letters w1
for index in random_indexes_w1:
    w1_l[index] = "*"
## change letters w2 
for idx in random_indexes_w2:
    w2_l[idx] = "*"

masked_word1 = "".join(w1_l)    
masked_word2 = "".join(w2_l)    
strgm = True

while strgm:
    try:
      print(f"პირველი სიტყვა: {masked_word1}, მეორე სიტყვა: {masked_word2}")
      i_ans1 = input("გამოიცანი პირველი სიტყვა: ")
      i_ans2 = input("გამოიცანი მეორე სიტყვა: ")
      if i_ans1.strip() == w1 and i_ans2.strip() == w2:
          print(f"თქვენ გაიმარჯვეთ!")
          break
      elif i_ans1.sprip() == w1 and i_ans2.strip() != w2:
          print(f"თქვენ გამოიცანით 1 სიტყვა. 50% {w1} სწორია, {i_ans2} არასწორია") 
      elif i_ans1.strip() != w1 and i_ans2.strip() == w2:
          print(f"თქვენ გამოიცანით 2 სიტყვა. 50% {w2} სწორია, {i_ans1} არასწორია") 
      else: 
          print(f"თქვენ დამარცხდით! პირველი სიტყვა {w1}, მეორე სიტყვა {w2}")        
    except Exception as e:
        print(f"მოხდა რაღაც შეცდომა! {e}")   
   



# დავალება მოამზადეთ მხოლოდ 1 ფაილში და ისე ატვირთეთ, გამოიყენეთ PEP8
# სტანდარტი და მიჰყევით მხოლოდ ამოცანის პირობას.