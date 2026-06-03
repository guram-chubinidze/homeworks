
# \#1 მოცემულია სიტყვა "ABCD". დაბეჭდე ყველა შესაძლო ვარიანტი და **დაითვალე** რამდენია სულ რაოდენობრივად (უნდა დააბრუნო რიცხვი)

print('"ABCD". დაბეჭდე ყველა შესაძლო ვარიანტი და **დაითვალე**\n')

from itertools import combinations, permutations

my_word = "ABCD"

#result1 = ["".join(a) for a in combinations(my_word, 4)] # 4 სიმბოლოდ
result2 = ["".join(v2) for v2 in permutations(my_word, 4)] # 4 იმბოლოდ
#cresult1 = len(result1)
cresult2 = len(result2)

#print(f"ვარიანტი 1 : რაოდენობა = {cresult1}  {result1}")
print(f"ვარიანტი 2 : რაოდენობა = {cresult2}  {result2}")




# \#2 იპოვე მომდევნო კვირის პირველი სამშაბათი, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)
print("იპოვე მომდევნო კვირის პირველი სამშაბათი, საწყისი თარიღი არის დღევანდელი დღე\n")
from datetime import datetime, timedelta

def next_thue(target_idx):
 today = datetime.now()
 today_idx = today.weekday()  # ორშაბათი=0, სამშაბათი=1... კვირა=6
 # ვითვლით სხვაობას სამშაბათამდე
 days_do = target_idx - today_idx # 7  #1-1=0->7,
 if days_do <= 0:
    days_do += 7
        
 return today + timedelta(days=days_do)
next_tuesday = next_thue(1)    # მომავალი სამშაბათი 

print("შემდეგი სამშაბათი იქნება:", next_tuesday.strftime('%Y-%m-%d'))



# \#3 დაადგინე, არის თუ არა შეყვანილი წელი ნაკიანი, მომხმარებელს შემოჰყავს მხოლოდ წელი და ვეუბნებით არის თუ არა ნაკიანი
print("დაადგინე, არის თუ არა შეყვანილი წელი ნაკიანი, მომხმარებელს შემოჰყავს მხოლოდ წელი\n")
# import calendar



# myinput = ...

from datetime import date

checkYear = int(input("შეიყვანეთ წელი: "))
def isset_february_29(year):
    try:    
        date(year, 2, 29)
        return True  
    except ValueError:
        return False 

# შემოწმება:
if isset_february_29(checkYear):
    print(f"{checkYear} წელი ნაკიანია!")
else:
   print(f"{checkYear} წელი არ არის ნაკიანი!") 




# \#4 დაითვალე რამდენი კვირაა დარჩენილი ახალ წლამდე, საწყისი თარიღი არის დღევანდელი დღე (ხელით არ გაწეროთ თარიღი)
print("დაითვალე რამდენი კვირაა დარჩენილი ახალ წლამდე, საწყისი თარიღი არის დღევანდელი დღე\n")
from datetime import datetime

today = datetime.now()
target_date = datetime(2026, 12, 31)
days_left = (target_date - today).days
weeks_left = days_left // 7
print(f"დარჩენილია დაახლოებით: {weeks_left} კვირა")




# \#5 შექმენი ყველა 3-ელემენტიანი კომბინაცია სიიდან \[1,2,3,4,5] (itertools-ის გამოყენებით)
print(f"შექმენი ყველა 3-ელემენტიანი კომბინაცია სიიდან [1,2,3,4,5]\n")
from itertools import combinations, permutations

my_list = [1,2,3,4,5]

result1 = [c for c in combinations(my_list, 3)]
result2 = [c for c in permutations(my_list, 3)]

print(f"ვარიანტი 1 = ყველა შესაძლო 3-ელემენტიანი კომბინაცია {result1} \n")

print(f"ვარიანტი 2 = ყველა შესაძლო 3-ელემენტიანი კომბინაცია {result2}")



# \#6 მიიღე ყველა კომბინაცია "XYZ"-ის სიმბოლოებით სიგრძე 1-დან 3-მდე

# მაგალითი: X, Y, Z, XY, XZ, YZ, XYZ უნდა მივიღოთ მსგავსი შედეგი.
print('მიიღე ყველა კომბინაცია "XYZ"-ის სიმბოლოებით სიგრძე 1-დან 3-მდე\n')
from itertools import product

my_text = "XYZ"
all_variants = []

for r in range(1, 4):
    all_variants.extend(["".join(p) for p in product(my_text, repeat=r)])

print(all_variants)





# \#7 თამაში უკუსვლაზე

# კომპიუტერი ირჩევს შემთხვევითობის პრინციპით რიცხვს 1-20 მდე, მოთამაშეს აქვს მხოლოდ 5 წამი რიცხვის გამოსაცნობად,
#  თუ 5 წამში სწორ რიცხვს ვერ შეიყვანს, თამაში სრულდება და გამოდის ტექსტი "დრო ამოიწურა, თქვენ დამარცხდით".

# from datetime import datetime, timedelta

# import time, random


from datetime import datetime
import random
import time

# 1. მიმდინარე დრო წამებში (Timestamp)
now_in_seconds = time.time()
# 2. 5 წამის შემდეგ
after_5_seconds = now_in_seconds + 5
randNumFrom = random.randint(1,20)
parsed_date_start = datetime.fromtimestamp(now_in_seconds).strftime('%Y-%m-%d %H:%M:%S')
parsed_date_end = datetime.fromtimestamp(after_5_seconds).strftime('%Y-%m-%d %H:%M:%S')

print(f"თამაში დაიწყო: {parsed_date_start}")
print(f"თამაში დასრულდება: {parsed_date_end}")
startGame = True

while startGame:
      inputNum = int(input("შეიყვანეთ რიცხვი: "))  
      secs = int(after_5_seconds-time.time())
      if int(time.time()) > int(after_5_seconds):
            print(f"თქვენ დამარცხდით! დრო ამოიწურა. სწორი პასუხი იყო: {randNumFrom}. თამაში დასრულდა {parsed_date_end}")  
            bstartGame = False
      elif inputNum == randNumFrom:
            print(f"გილოცავთ თქვენ გაიმარჯვეთ! სწორი პასუხია: {randNumFrom}")
            startGame = False 
      else:
            print(f"პასუხი არასწორია! კიდევ სცადეთ: თამაშის დასრულებამდე დარჩენილია {secs} წამი")
            continue

# \#7 თამაში უკუსვლაზე

# კომპიუტერი ირჩევს შემთხვევითობის პრინციპით რიცხვს 1-20 მდე, მოთამაშეს აქვს მხოლოდ 5 წამი რიცხვის გამოსაცნობად, თუ 5 წამში სწორ რიცხვს ვერ შეიყვანს, თამაში სრულდება და გამოდის ტექსტი "დრო ამოიწურა, თქვენ დამარცხდით".



# from datetime import datetime, timedelta

# import time, random





# \#8 ორი მოთამაშე იწყებს "გარბენს". უნდა შეამოწმო რომელი დაასრულებს ნაკლებ დროში

# player1 = start + timedelta(seconds=random.randint(5,20))

# player2 = start + timedelta(seconds=random.randint(5,20))





# \#9 იღბლიანი დაბადების დღე

# მოთამაშემ უნდა შეიყვანოს დაბადების თარიღი და თამაში დაითვლის რამდენი დღეა დარჩენილი შემდეგ დაბადების დღემდე

# birthday = date(2000, 12, 10)





# \#10 საცავი - ჯუნიორ ჰაკერი :)

# თამაში არის შემდეგი - გვაქვს სეიფი რომელსაც აქვს ციფრები 1-6 მდე პაროლი არ ვიცით, ყოველ დღე კომპიუტერი აგენერირებს ახალ პაროლს (შემთხვევითობის პრინციპით) პაროლი არის 4 ციფრიანი. ჩვენი მიზანია დავწეროთ ისეთი კოდი რომელიც შეამოწმებს ვარიანტებს და როცა მოხდება კომპიუტერის მიერ დაგენერირებული პაროლის დამთხვევა უნდა გამოვიტანოთ შეტყობინება "პაროლი სწორია, საცავი გახსნილია", აუცილებელი პირობაა გამოვიტანოთ ყველა ჩვენს მიერ ნაცადი პაროლი სანამ მივალთ სწორ ვარიანტამდე.















# სავარჯიშოები გავყოთ ორ ნაწილად: 1-6 მდე სავარჯიშოებისთვის გავაკეთოთ ახალი ბრანჩი რომელსაც დავარქმევთ სახელს და ვიმუშავებთ, როდესაც დავასრულებთ ყველას უნდა მოხდეს GITHUB-ზე ატანა გიტ ბრძანებებით. 7-10-მდე სავარჯიშოებისთვის უნდა გავაკეთოთ კიდევ ერთი ბრენჩი და იქ ვიმუშაოთ, დასრულების შემდეგ ავიტანოთ GITHUB-ზე, გავაკეთოთ ყველას MERGE და ამის შემდეგ განვაახლოთ ჩვენი main ბრენჩი EDITOR-ში.



# ყველა ბრძანება ამოიწერეთ და დავალებას დაურთეთ თან, ასევე მიუთითეთ თქვენი გითჰაბის შესაბამისი რეპოზიტორია.



































# ნაჩვენებია დავალება #5.md