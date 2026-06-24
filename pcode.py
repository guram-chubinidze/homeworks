

# #4 pytest1

# შექმენით ფუნქცია Celsius → Fahrenheit. დაწერეთ pytest ტესტები approx-ის გამოყენებით.

# ნიმუში: assert pytest.approx
print(f"-----------------------------------------------------------4---------------------------------------------------------------")
def celsius_to_fahrenheit(celsius):    
    return (celsius * 1.8) + 32
# #5 pytest2

# შექმენით ფუნქცია რომელიც ამოწმებს მომხმარებლის ლოგინს და პაროლს dictionary-დან
# pytest-ში გამოიყენეთ raises შეცდომის დასატესტად

# ნიმუში: raise ValueError
print(f"-----------------------------------------------------------5---------------------------------------------------------------")
USERS = {
    "admin": "secret123",
    "giorgi": "p@ssword",
    "ani": "hello2026"
}

def login_user(username, password):    
  
    
    if  len(password) < 6:
        raise ValueError("მინიმუმ 6 სიმბოლო")
    
    if username not in USERS:
        raise ValueError("მომხმარებელი ვერ მოიძებნა!")    
    
    if USERS[username] != password:
        raise PermissionError("არასწორი პაროლი!")
        
    return "წარმატებული ავტორიზაცია!"

# #6 pytest3

# დაწერეთ ფუნქცია, რომელიც ამოწმებს არის თუ არა სტრიქონი სწორი email (ანუ შეიცავს @ და . სიმბოლოებს)
# pytest-ით გააკეთეთ ტესტები parametrization-ის გამოყენებით

# ნიმუში: @pytest.mark.parametrize
print(f"-----------------------------------------------------------6---------------------------------------------------------------")
def is_valid_email(email):   
    if not isinstance(email, str):
        return False
    email.lower()    
    # უნდა შეიცავდეს '@' და '.' სიმბოლოებს
    # ასევე '@' უნდა იყოს წერტილამდე და არცერთი არ უნდა იყოს სტრიქონის დასაწყისში(მინიმუმ 2 სიმბოლო)
    if "@" in email and "." in email and len(email) > 0:
        if email.find("@") > 1 and len(email) -1 - email[::-1].find(".") >  email.find("@")+2 :
            return True
            
    return False