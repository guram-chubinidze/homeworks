# #1 დაწერეთ პაროლის გენერატორი.
# დავალების შესრულებაში დაგეხმარებათ: random მოდული, while ან for ციკლი, list,
# სტრიქონის ფორმატირება.
# input ის მეშვეობით უნდა შეგვეძლოს მითითება რა სიგრძის პაროლი გვინდა და რა
# სიმბოლეობიდან გენერირდება იგი: პაროლის სიგრძეს ირჩევს მომხმარებელი, უნდა თუ
# არა სიმბოლოები, რიცხვები, დიდი/პატარა ასოები (ლათინურად) თუ ქართულს შემოიტანს
# უნდა დაუწერო რომ “შეიყვანე მხოლოდ ლათინური ასოები”


import random
import string


print("პაროლის გენერატორი, exit - გამოსვლა ")
# პაროლის დაჭრა ნაჭრებად
def cur_pieces(pLen,piece):
   pLen = int(pLen)
   res = []
   for i in range(piece-1):
      fromLen = pLen-sum(res)-(piece-i-1) # პაროლის სიგრძეს- ნაჭრების ჯამი-დარჩენილი რაოდენობა
      apiece = random.randint(1,fromLen) # შემთხვევითი რიცხვი
      res.append(apiece)
   res.append(pLen - sum(res))  
   return res 



     
startTask = True
passParams = {"iPassLen":None,"iSymInPass":None,"iDigInPass":None,"iPassUp":None,"iPassLow":True}

while startTask:
    # check if question is answered & input password length
    if  passParams["iPassLen"] is None:
        iPassLen = input("შეიყვანეთ პაროლის სიგრძე: ")
    # Exit
    if(iPassLen == "exit"):
        break
    # validate digits
    if not iPassLen.isdigit():
        print("შეიყვანეთ მხოლოდ რიცხვები")
        continue
    # min password length 4
    if int(iPassLen) < 4:
        print("პაროლის სიგრძე უნდა იყოს 4 ან მეტი")
        continue
    else:    
    # set password length    
     passParams["iPassLen"] = iPassLen  
    # check if question is answered & input symbol   
    if passParams["iSymInPass"] is None:
       iSymInPass = input("გსურთ სიმბოლოების გამოყენება პაროლში? (Y/n) Y").lower().strip()    
    # Exit
    if(iSymInPass == "exit"):
        break
    # validate isalpha only y & n
    if passParams["iSymInPass"] is None and iSymInPass not in "yn ":
        print("შეიყვანე მხოლოდ ლათინური ასოები (y ან n)")
        continue
    else:  
     # set password symbols  dafault Yes
     if iSymInPass == "" or iSymInPass == "y":
        iSymInPass = True 
     else:
         iSymInPass = False   
     passParams["iSymInPass"] = iSymInPass 
      # check if question is answered & input digits   
    if passParams["iDigInPass"] is None:
       iDigInPass = input("გსურთ რიცხვების გამოყენება პაროლში? (Y/n) Y").lower().strip()    
    # Exit
    if(iDigInPass == "exit"):
        break
    # validate isdigits only y & n
    if passParams["iDigInPass"] is None and iDigInPass not in "yn ":
        print("შეიყვანე მხოლოდ ლათინური ასოები (y ან n)")
        continue
    else:  
     # set password digits  dafault Yes
     if iDigInPass == "" or iDigInPass == "y":
        iDigInPass = True 
     else:
         iDigInPass = False   
     passParams["iDigInPass"] = iDigInPass 
    # check if question is answered & input
    if passParams["iPassUp"] is None:       
       iPassUp = input("გსურთ დიდი/პატარა ასოების გამოყენება პაროლში? (Y/n) Y").lower().strip() 
    # Exit   
    if(iPassUp == "exit"):
        break
     # validate isalpha only y & n
    if passParams["iPassUp"] is None and iPassUp not in "yn":
        print("შეიყვანე მხოლოდ ლათინური ასოები (y ან n)")
        continue
    else:  
     # set Uppercase symbols default Yes
     if iPassUp == "" or iPassUp == "y":
          iPassUp = True
     else:
         iPassUp = False     
     passParams["iPassUp"] = iPassUp 
    if passParams["iPassLen"] is not None and passParams["iSymInPass"] is not None and  passParams["iPassUp"] is not None and  passParams["iDigInPass"] is not None:           
           startTask = False


countPassPiece =  list(passParams.values()).count(True)  # პაროლის ნაჭრების რაოდენობა 

passParamsOnlyTrue = [key for key, value in passParams.items() if value is True]    # მხოლოდ True მონაცემები 

lenPassPiece = cur_pieces(passParams["iPassLen"],countPassPiece)  # პაროლის ნაჭრების სიგრძე

# combine lists
combineData = list(zip(passParamsOnlyTrue,lenPassPiece))

def pass_str(combineData):
    
    gPassword = ""
    for name,value in combineData:   
     if name == "iSymInPass":
        if value > 1:
         syms =  ''.join(random.choices(string.punctuation,k=value))
        else:
         syms =  random.choice(string.punctuation)
        gPassword += syms
     elif name ==  "iDigInPass":
        strt = 10**(value-1)
        end  = (10**value)-1
        dgts = random.randint(strt,end)
        gPassword += str(dgts)
     elif name == "iPassUp":
        if value > 1:
         upStr =  ''.join(random.choices(string.ascii_uppercase,k=value))
        else:
         upStr =  random.choice(string.ascii_uppercase)   
        gPassword += upStr
     elif name == "iPassLow":
       if value > 1:
        lowStr =  ''.join(random.choices(string.ascii_lowercase,k=value)) 
       else:
         lowStr =  random.choice(string.ascii_lowercase)   
       gPassword += lowStr

    return gPassword  

passResult = pass_str(combineData)         
print(f" დაგენერირდა პაროლი   {passResult}")  

      



# #2 პაროლის შეფასება
# ამოცანა: მომხმარებლის შეყვანილი პაროლი შეაფასე 0–10 შკალით: სიგრძე, ციფრები, სიმბოლოები,
# დიდი/პატარა ასოები, განმეორებადი სიმბოლოების არსებობა.
# მოთხოვნები: გამოიტანე “weak/medium/strong”.
# დუპლიკატების დათვლა
def count_chars(iText):
  rChars = []
  for char in iText:
   count = iText.count(char) 
   iText = iText.replace(char,"")
   if count > 2:   
    rChars.append({char:count})
  return rChars

# სტრინგის ტიპების შემოწმება
def has_punctuation_set(text,textType):
    if textType == "punctuation":
     return not set(text).isdisjoint(string.punctuation)
    elif textType == "digits":
     return not set(text).isdisjoint(string.digits)
    elif textType == "uppercase":
     return not set(text).isdisjoint(string.ascii_uppercase)
    elif textType == "lowercase":
     return not set(text).isdisjoint(string.ascii_lowercase)
    return False 


# ინპუტი
iPass = input("შეიყვანეთ პაროლი: ")

def check_password_quality():
    ## დუპლიკატების შემოწმება
    checkDuplicates = count_chars(iPass)

    points = 0
    liPass  = len(iPass)
    # პაროლის სიგრძე
    if liPass < 6:
       points -= 2
    elif 6 <= liPass < 8:
     points -= 1   
    elif 8 <= liPass < 10: 
     points += 1
    elif liPass >= 10:
     points += 2
    points += int(has_punctuation_set(iPass,'punctuation'))*2
    # print(f"punctuation {points}")
    points += int(has_punctuation_set(iPass,'digits'))*2
    # print(f"digits {points}")
    points += int(has_punctuation_set(iPass,'uppercase'))*2
    # print(f"uppercase {points}")
    points += int(has_punctuation_set(iPass,'lowercase'))*2
    # print(f"lowercase {points}")

    # გამეორებებზე ქულების დაკლება
    if len(checkDuplicates) > 2:
     points -= 2
    elif 0 > len(checkDuplicates) < 2:
     points -= 1  

    # 0 ზე ნაკლები რომ არ გამოჩნდეს  
    if points < 0 :
     points = 0

    passCheck = ""

    if points < 7:
     passCheck = "Weak"
    elif 7 < points < 10:
     passCheck = "Medium"
    elif points > 9:
     passCheck = "Strong"  
    return {"points":points,"quality":passCheck} 

res = check_password_quality()
print(f"Points: {res['points']}, Quality: {res["quality"]} ")

# #3 დაწერე ფუნქცია (ფიბონაჩის რიგი) - *რა არის ფიბონაჩი - ბოლო ორი ელემენტის ჯამით ვამატებთ
# ახალ რიცხვს*, სანამ სიგრძე არ გახდება მომხმარებლის მიერ შემოყვანილი რიცხვი, აუცილებლად
# უნდა შემოიტანოს რიცხვი, სხვა რამის შემოტანის დროს უნდა შემოწმდეს რა შემოიტანა
# მომხმარებელმა და უნდა დაუსახელო აღნიშნული და უთხრა რომ მხოლოდ რიცხვი შემოიტანოს. მაგ:
# შემოიტანა სიმბოლო, უნდა უთხრა შენ შემოიტანე სიმბოლო არასწორია, მხოლოდ რიცხვი!
import string


print("# 3 - ფიბონაჩის მიმდევრობის კალკულატორი, exit - გამოსვლა ")
## Check input type
def checkInputType(iNumber):
    msg = ""
    if all(char in string.punctuation for char in iNumber):
         msg = "თქვენ შემოიყვანეთ სიმბოლო, არასწორია!"
    elif iNumber.isalpha():
         msg = "თქვენ შემოიყვანეთ ასოები, არასწორია!"
    elif iNumber.isspace():
         msg = "თქვენ შემოიყვანეთ ცარიელი ადგილი, არასწორია!"     
    elif iNumber.startswith("-"):
         msg = "თქვენ შემოიყვანეთ უარყოფითი მნიშვნელობა!" 
    else:
         msg = "თქვენ შემოიყვანეთ უცნობი ტიპის მონაცემი, შეიყვანეთ მხოლოდ რიცხვი!"                       
        
    return msg

## მიმდევრობა
def my_fibonacci(n):    
    members = [0, 1]
    # 0 და 1 უკვე გვაქვს, თუ მომხმარებელმა 1 ან 2 შეიყვანა, მაშინ პირდაპირ ვაბრუნებთ შესაბამის ლისტს
    if int(n) == 2:        
        return members
    if int(n) == 1:        
        return [0]    
    wTrue = True
    nLen = int(n)    
    while wTrue:
     members.append(members[-1]+members[-2])
     if len(members) == nLen:
        wTrue = False
    return members

startTask = True
while startTask:
    iNumber = input("შეიყვანეთ რიცხვი (დადებითი): ")
    # Exit
    if(iNumber == "exit"):
        break
    # validate digits
    if not iNumber.isdigit():
        checkType = checkInputType(iNumber)        
        print(f"{checkType}. შეიყვანეთ მხოლოდ რიცხვები(დადებითი) ")                
        continue 

    else:  
       if int(iNumber) < 10:
        print("თქვენ შემოიყვანეთ ციფრი.შეიყვანეთ მხოლოდ რიცხვები(დადებითი)")
        continue
       else:
        res = my_fibonacci(iNumber)
        print(f"ფიბონაჩის ლისტი {iNumber} წევრით: {res}") 
        startTask = False
# #4 პალინდრომი
# ამოცანა: შეამოწმე, არის თუ არა შეყვანილი ტექსტი პალინდრომი (მხოლოდ ასოები/ციფრები). თუ
# არაა, შესთავაზე ყველაზე ახლო პალინდრომი ერთი სიმბოლოს ჩასმით/წაშლით.
print(" #4 პალინდრომი") 
import string

mkhedruli = [chr(code) for code in range(0x10D0, 0x10F1)]
allowSymbols = mkhedruli + [char for char in string.digits] + [" "]+[char for char in string.ascii_letters]

startTask = True
while startTask:
    iText = input("შეიყვანეთ ტექსტი: ")

    if not all(char in allowSymbols for char in iText): 
        print("შეყვანილი ტექსტი უნდა შედგებოდეს მხოლოდ ასოებისა და ციფრებისგან")
        continue
    else:
        startTask = False

iText = iText.strip().lower()
## შევამოწმოთ არის თუ არა პალინდრომი
def checkPalindrome(text):
    lText = len(text)
    divText = lText//2
    firstHalf = text[:divText]
    secondHalf = text[-divText:][::-1]
    return firstHalf == secondHalf

lText = len(iText)
divText = lText//2
firstHalf = list(iText[:divText])
secondHalf = list(iText[-divText:][::-1])

noequalSymbols = []

i = divText-1
while i >= 0:    
    if(firstHalf[i] != secondHalf[i]):
        noequalSymbols.append((i, firstHalf[i], secondHalf[i]))
    i-=1




if checkPalindrome(iText+iText[:1]):
    print(f"შეყვანილი ტექსტი პალინდრომი გახდება თუ ერთი სიმბოლოს {iText[:1]} დამატებით ბოლოში")
elif checkPalindrome(iText[-1]+iText):
    print(f"შეყვანილი ტექსტი პალინდრომი გახდება თუ ერთი სიმბოლოს {iText[-1:]} დამატებით დასაწყისში")
elif len(noequalSymbols) == 1:
    print(f"შეყვანილი ტექსტი პალინდრომი გახდება თუ ერთი სიმბოლოს {noequalSymbols[0][1]} წაშლით პოზიციიდან {noequalSymbols[0][0]}")
elif len(noequalSymbols) == 0:
    print("შეყვანილი ტექსტი უკვე პალინდრომია")
else:
    print("შეყვანილი ტექსტი პალინდრომი ვერ გახდება ერთი სიმბოლოს დამატებით ან წაშლით")            

# #5 ზედმეტსახელების გენერატორი
# მომხმარებელს შემოაქვს მხოლოდ ერთი სიტყვა(სხვა შემთხვევები დაბლოკე) და შენ სთავაზობ 5
# ზედმეტსახელს ამ სიტყვასთან კავშირში.
print("# 5 ზედმეტსახელების გენერატორი")

from datetime import date
inputWord = input("შეიყვანეთ სიტყვა: ")
if not inputWord.isalpha() or len(inputWord.split()) > 1:
    print("შეყვანილი ტექსტი უნდა შედგებოდეს მხოლოდ ასოებისა და ერთი სიტყვისგან")
else:   
    nameGen = [{"conn": ["-","_",".","",""], 
                "endings": [111,222,333,444,555,666,777,888,999,date.today().year,""],
                "replace": {"a": "@", "s": "$","1":"!","n":""}}]

    countNicknames = 5
    nicknameSym = ""
    for i in range(countNicknames):
     conn  = random.choice(nameGen[0]["conn"])
     ending = random.choice(nameGen[0]["endings"])
     replace = random.choice(list(nameGen[0]["replace"].keys()))
     nicknameSym = inputWord.replace(replace, nameGen[0]["replace"][replace])
     nickname = nicknameSym + conn + str(ending)
     print(f"შენთვის გენერირებული ზედმეტსახელი: {nickname}")
     i += 1

# #6 სორტირება
# მომხმარებელს შემოჰყავს რიცხვები თითო გამოტოვებით, (ულიმიტოდ რამდენიც უნდა) პროგრამა
# სთავაზობს როგორ უნდა რომ დაუსორტირდეს აღნიშნული: კლებადობით, ზრდადობით, random-ად,
# მხოლოდ უნიკალური მონაცემები დატოვოს. რომელსაც აირჩევს უნდა გამოვიდეს ზუსტად ისე
# დალაგებული სია.
print("# 6 სორტირება")
startTask = True
data = {"inputNumbers":None}

while startTask:    
        if data["inputNumbers"] is None:   
           inputNumbers = input("შეიყვანეთ რიცხვები, თითო გამოტოვებით: exit -გამოსვლა  ")
           data["inputNumbers"] = inputNumbers
       
           numbersList = inputNumbers.split() # აქ ვიღებთ სტრინგს და ვყოფთ მას ლისტად, სადაც თითო ელემენტი არის რიცხვი სტრინგის სახით  
        # აქ ვქმნით ახალ ლისტს, სადაც თითო ელემენტი არის რიცხვი ინტის სახით,
        #  ამისთვის ვიყენებთ list comprehension-ს და ვცვლით სტრინგებს ინტებზე        
           numbersListInt = [int(x) for x in numbersList] 

        if inputNumbers.lower() == "exit":
            print("პროგრამიდან გამოსვლა...")
            startTask = False
        else:
            chooceSort = input("აირჩიეთ სორტირების ტიპი: 1-კლებადობით, 2-ზრდადობით, 3-random-ად, 4-მხოლოდ უნიკალური მონაცემები დატოვოს: ")  
            if chooceSort.lower() == "exit":
                print("პროგრამიდან გამოსვლა...")
                startTask = False
            else:    
                if chooceSort == "1":
                    sortedList = sorted(numbersListInt, reverse=True)
                    print(f"რიცხვები კლებადობით: {sortedList}")
                    continue
                elif chooceSort == "2":
                    sortedList = sorted(numbersListInt)
                    print(f"რიცხვები ზრდადობით: {sortedList}")
                    continue
                elif chooceSort == "3":
                    import random
                    sortedList = numbersListInt[:]
                    random.shuffle(sortedList)
                    print(f"რიცხვები random-ად: {sortedList}")
                    continue
                elif chooceSort == "4":
                    sortedList = list(set(numbersListInt))
                    print(f"რიცხვები მხოლოდ უნიკალური მონაცემები დატოვოს: {sortedList}")
                    continue
                else:
                    print("არასწორი არჩევანი, გთხოვთ აირჩიოთ 1, 2, 3 ან 4") 
                    continue               

# #7 ტექსტის ფილტრი
# მომხმარებელი შეჰყავს ტექსტი.
# ამოცანა: პროგრამამ უნდა წაშალოს ყველა ციფრი და სიმბოლო, დატოვოს მხოლოდ ასოები და
# სივრცეები.

# #8 პირამიდა
# მომხმარებელი შეჰყავს რიცხვების სია (მაგ. 3,5,7,2).
# ამოცანა: შექმენი “პირამიდა”, სადაც ყოველი ახალი რიგი ზემოთაა წინა ორი რიცხვის ჯამი.
# 3 5 7 2

# 8 12 9
# 20 21
# 41

# #9 მომხმარებელი შეჰყავს ნებისმიერი ტექსტი, მოძებნე, რომელი სიტყვა მეორდება ტექსტში ყველაზე
# მეტჯერ. მაგ: "Python is great and python is easy" → ყველაზე ხშირია
# "python". თუ ორი ან მეტი სიტყვაა ტოლი, დააბრუნე ყველა.

# #10 მომხმარებელს შეჰყავს წინადადება, ამოცანა: გამოიანგარიშე თითოეული სიტყვის სიგრძე და
# დააბრუნე dictionary
# მაგალითად: "Python is fun" → {"Python": 6, "is": 2, "fun": 3}

# # შექმენით გითჰაბზე რეპოზიტორია, დაკლონეთ ედიტორში, 1,2,3 ამოცანის ამოხსნის შემდეგ მთავარ
# ბრენჩზე გააკეთე დამატება , კომიტი და აიტანე გითჰაბზე ეს სამი ამოცანა, შემდეგ გააგრძელე
# მუშაობა, გააკეთე ახალი ბრენჩი სახელად “secondbranch” 4,5,6 ამოცანა ამოხსენი ამ ბრენჩზე და
# აიტანე გითჰაბზე, გააკეთე ფულ რექუესთი და დამერჯე მთავარ ბრენჩზე (main)-ზე. შემდეგ გააკეთე
# მესამე ბრენჩი “thirdbranch” გააკეთე დარჩენილი ამოცანები და აიტანე გითჰაბზე ანალოგიურად და
# ფულ რექუესთი და დამერჯე მეინზე.
# აუცილებლად გადაიღეთ სქრინები რასაც დაწერთ ტერმინალში თანმიმდევრობით და მიაბით
# დავალებასთან ერთად, ასევე გამიზიარეთ რეპოზიტორიის მისამართი. (უნდა იყოს public)