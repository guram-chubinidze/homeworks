import pytest
print(f"-----------------------------------------------------------4---------------------------------------------------------------")
from pcode import celsius_to_fahrenheit

def test_celsius_to_fahrenheit_positive():   
    assert celsius_to_fahrenheit(0) == pytest.approx(32.0)  # 0°C და 32°F

def test_celsius_to_fahrenheit_negative():   
    assert celsius_to_fahrenheit(-40) == pytest.approx(-40.0)  # -40°C და -40°F 

def test_celsius_to_fahrenheit_float():   
    assert celsius_to_fahrenheit(36.6) == pytest.approx(97.88) # 36.6°C არის 97.88°F

def test_celsius_to_fahrenheit_boiling():    
    assert celsius_to_fahrenheit(100) == pytest.approx(212.0) # 100°C უნდა იყოს 212°F

print(f"-----------------------------------------------------------5---------------------------------------------------------------")
from pcode import login_user

def test_login_success():   
    result = login_user("giorgi", "p@ssword")
    assert result == "წარმატებული ავტორიზაცია!"

def test_login_wrong_username():   
    with pytest.raises(ValueError) as exc_info:
        login_user("unknown_user", "any_password")

    assert str(exc_info.value) == "მომხმარებელი ვერ მოიძებნა!"
def test_login_wrong_password():

    with pytest.raises(PermissionError) as exc_info:
        login_user("admin", "არასწორი_პაროლი_123")
        
    assert str(exc_info.value) == "არასწორი პაროლი!"

def test_password_len():
       
    with pytest.raises(ValueError) as info:
        login_user("admin", "secr")
        
    assert str(info.value) == "მინიმუმ 6 სიმბოლო"  

print(f"-----------------------------------------------------------6---------------------------------------------------------------")

from pcode import is_valid_email

# ტესტების პარამეტრიზაცია
@pytest.mark.parametrize(
    "email_input, expected_result",
    [
        # პოზიტიური ქეისები (სწორი მეილები)
        ("giorgi@gmail.com", True),
        ("nino_beridninoshvilize@work.ge", True),
        ("ia.iashvili@ia.ge", True),
        ("test_123@subdomain.example.com", True),
        
        # ნეგატიური ქეისები (არასწორი მეილები)
        ("giorgigmail.com", False),       # აკლია @
        ("giorgi@gmailcom", False),        # აკლია წერტილი
        ("@gmail.com", False),             # აკლია იუზერნეიმი @-ის წინ
        ("giorgi@.com", False),            # აკლია დომენი @-სა და წერტილს შორის
        ("giorgi.com@gmail", False),       # წერტილი @-ის წინ არის და არა მერე
        (12345, False),                    # საერთოდ არ არის სტრიქონი
        ("", False),                        # ცარიელი სტრიქონი
        ("a@gmail.com", False),             # 1 სიმბოლო @ მდე
        ("giorgi@g.com", False),            # 1 სიმბოლო დომეინში 
    ]
)
def test_is_valid_email(email_input, expected_result):

    assert is_valid_email(email_input) == expected_result