# მოამზადეთ ორი ფაილი - unittest.py & pytest.py შესაბამისად განათავსეთ დავალებები თითოეულში.

# #1 unittest1

# შექმენით Calculator კლასი add, subtract, multiply, divide მეთოდებით. დაწერეთ unittest რომელიც ამოწმებს ყველა მეთოდს.
# გაითვალისწინეთ 0-ზე გაყოფაც.
# გამოიყენეთ unittest მოდული
# გამოიყენეთ setup მეთოდი.
print(f"-----------------------------------------------------------1---------------------------------------------------------------")

import unittest


class Calculator:

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
             raise ValueError("0 ზე გაყოფა არ შეიძლება")
        return a / b

class TestCalculator(unittest.TestCase):

    def setUp(self):      
        print("ახალი კალკულატორი...\n")
        self.calc = Calculator()

    # Positive
    def test_add_positive(self):
        print("მიმატების ტესტი: დადებითი რიცხვები \N{check mark}")
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract_positive(self):
        print("გამოკლების ტესტი: დადებითი რიცხვები \N{check mark}")
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply_positive(self):
        print("გამრავლების ტესტი: დადებითი რიცხვები \N{check mark}")
        self.assertEqual(self.calc.multiply(5, 3), 15)

    def test_divide_positive(self):
        print("გაყოფის ტესტი: დადებითი რიცხვები \N{check mark}")
        self.assertEqual(self.calc.divide(15, 3), 5)

    # Negative
    def test_add_negative(self):
        print("მიმატების ტესტი: უარყოფითი რიცხვები \N{check mark}")
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract_negative(self):
        print("გამოკლების ტესტი: უარყოფითი რიცხვები \N{check mark}")
        self.assertEqual(self.calc.subtract(-5, -7), 2)

    def test_multiply_negative(self):
        print("გამრავლების ტესტი: უარყოფითი რიცხვები \N{check mark}")
        self.assertEqual(self.calc.multiply(-3, 7), -21)

    def test_divide_negative(self):
        print("გაყოფის ტესტი: დადებითი რიცხვები \N{check mark}")
        self.assertEqual(self.calc.divide(-27, 3), -9)

    # Divide by zero
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(-27, 0)

if __name__ == "__main__":
    unittest.main()    

# #2 unittest2

# შექმენით BankAccount კლასი deposit და withdraw მეთოდებით. დაწერეთ unittest რომელიც ამოწმებს:

# - სწორი ბალანსი

# - უარყოფითი თანხის შეტანისას შეცდომა

# - თანხის გამოტანა ბალანსზე მეტისას შეცდომა
print(f"-----------------------------------------------------------2---------------------------------------------------------------")

class BankAccount:
    def __init__(self):
        self.__balance = 0

    @property
    def get_balance(self):
        return self.__balance    
    
    @get_balance.setter
    def get_balance(self,amount):
        if amount <= 0:
            raise ValueError("თანხა უნდა იყოს დადებითი!")
        self.__balance += amount  

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("თანხა უნდა იყოს დადებითი!")
        self.__balance += amount

    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("თანხა უნდა იყოს დადებითი!")
        if amount > self.__balance:
            raise ValueError("ანგარიშზე არ არის საკმარისი თანხა")
        self.__balance -= amount

class TestBankAccount(unittest.TestCase):
     
     def setUp(self):      
        print("ახალი ბანკის ექაუნთი...\n")
        self.account = BankAccount()

    # Positive
     def test_balance_positive(self):
        print("ბალანსის ტესტი: დადებითი  \N{check mark}")
        self.account.get_balance = 100
        self.assertEqual(self.account.get_balance,100)

     def test_deposit_positive(self):
        print("დეპოზიტის ტესტი: დადებითი  \N{check mark}") 
        self.account.deposit(100)      
        self.assertEqual(self.account.get_balance, 100)

     def test_withdraw_positive(self):
        print("თანხის გატანის ტესტი: დადებითი  \N{check mark}") 
        self.account.deposit(100)  
        self.account.withdraw(50)        
        self.assertEqual(self.account.get_balance, 50)

     # Negative
     def test_balance_negative(self):
        print("ბალანსის ტესტი: უარყოფითი  \N{check mark}")        
        with self.assertRaises(ValueError):
            self.account.get_balance = -5

     def test_deposit_negative(self):
        print("დეპოზიტის ტესტი: უარყოფითი  \N{check mark}")
        with self.assertRaises(ValueError): 
            self.account.deposit(-100)    

     def test_withdraw_negative(self):
        print("თანხის გატანის ტესტი: უარყოფითი  \N{check mark}")
        with self.assertRaises(ValueError): 
            self.account.withdraw(-50) 
            

if __name__ == "__main__":
    unittest.main()    

# #3 unittest3

# შექმენით ფუნქცია რომელიც იღებს JSON (dict) response-ს და აბრუნებს "status"-ის მნიშვნელობას. თუ status არ არსებობს → შეცდომა. 
# დაწერეთ ტესტები
print(f"-----------------------------------------------------------3---------------------------------------------------------------")


def get_status(response): 
    if not isinstance(response, dict):
        raise TypeError("გადაცემული არგუმენტი უნდა იყოს (dict)!")
        
    if "status" not in response:
        raise ValueError("შეცდომა: 'status' გასაღები არ არსებობს response-ში!")
        
    return response["status"]
# response = requests.get("https://jsonplaceholder.typicode.com/users")
# data = response.json()
# dd = get_status(data)
class TestGetStatus(unittest.TestCase):
    # Positive
    def test_get_status_success(self):        
        mock_response = {"status": "success", "data": [1, 2, 3]}
        result = get_status(mock_response)
        self.assertEqual(result, "success")

    # Negative
    def test_get_status_missing_key_raises_error(self):      
        mock_response = {"code": 200, "message": "OK"}  # სტატუსი არ არის       
        with self.assertRaises(ValueError):
            get_status(mock_response)

    def test_get_status_invalid_input_type(self):       
        invalid_input = ''         
        with self.assertRaises(TypeError):
            get_status(invalid_input)

if __name__ == "__main__":
    unittest.main()