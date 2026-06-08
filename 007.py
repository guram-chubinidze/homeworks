# #1 SQL დავალება
# გამოიტანე ProductName, CategoryID, Unit, Price ცხრილი- “პროდუქტები”
# სადაც ფასი მოთავსებული 18-სა და 25-ს შორის
# დაალაგე კლებადობით ფასის მიხედვით
import requests
print(f"-------------------------------------------------------------------1--------------------------------------------------------\n")
print(f"#1 SQL დავალება\nგამოიტანე ProductName, CategoryID, Unit, Price ცხრილი- “პროდუქტები”\nსადაც ფასი მოთავსებული 18-სა და 25-ს შორის\nდაალაგე კლებადობით ფასის მიხედვით")
query1 = """
SELECT ProductName, CategoryID, Unit, Price FROM Products
Where price > 18 and price < 25
ORDER BY PRICE DESC;
"""
print(query1)
# #2 SQL დავალება2
# გამოიტანე ყველა ველი, სადაც რაოდენობა ტოლია 15-ის ან 12-ის
# დაალაგე ზრდადობით
# ცხრილი - “OrderDetails”
print(f"-------------------------------------------------------------------2--------------------------------------------------------\n")
print(f"#2 SQL დავალება2\nგამოიტანე ყველა ველი, სადაც რაოდენობა ტოლია 15-ის ან 12-ის\n დაალაგე ზრდადობით\nცხრილი - “OrderDetails”")
query2 = """
SELECT * FROM OrderDetails
WHERE Quantity = 15 or Quantity = 12
ORDER BY Quantity ASC;
"""
print(query2)
# #3 მოცემულია JSON მასივი:
# [
# {"id": 1, "price": 50},
# {"id": 2, "price": 200},
# {"id": 3, "price": 150}
# ]
# ამოიღე მხოლოდ ის პროდუქტები, რომელთა ფასი 100-ზე მეტია.
print(f"-------------------------------------------------------------------3--------------------------------------------------------\n")
print(f"#3 მოცემულია JSON მასივი:\n ამოიღე მხოლოდ ის პროდუქტები, რომელთა ფასი 100-ზე მეტია.")
data = [
{"id": 1, "price": 50},
{"id": 2, "price": 200},
{"id": 3, "price": 150}
]
newList = [x for x in data if x["price"]>100]
print(newList)
# #4 მოცემულია რთული JSON:
# {
# "company": {
# "departments": [
# {"name": "IT", "employees": [{"name": "Ana"}, {"name": "Beka"}]},
# {"name": "HR", "employees": [{"name": "Nino"}]}
# ]
# }
# }
# ამოიღე ყველა თანამშრომლის სახელი
print(f"-------------------------------------------------------------------4--------------------------------------------------------\n")
print(f"#4 მოცემულია რთული JSON:\nამოიღე ყველა თანამშრომლის სახელი")
data = {
"company": {
"departments": [
{"name": "IT", "employees": [{"name": "Ana"}, {"name": "Beka"}]},
{"name": "HR", "employees": [{"name": "Nino"}]}
]
}
}
employee_names = [emp["name"] for dep in data["company"]['departments'] for emp in dep["employees"]] 
print(employee_names)
# #5 მოცემულია სტუდენტების სია:
# [
# {"name": "Ana", "grades": [90, 80, 95]},
# {"name": "Beka", "grades": [70, 85, 88]},
# {"name": "Nino", "grades": [100, 95, 99]}
# ]

# იპოვე სტუდენტი, რომელსაც აქვს საშუალო ქულის მიხედვით საუკეთესო
# შედეგი.
print(f"-------------------------------------------------------------------5--------------------------------------------------------\n")
print(f"#5 მოცემულია სტუდენტების სია:\nიპოვე სტუდენტი, რომელსაც აქვს საშუალო ქულის მიხედვით საუკეთესო\nშედეგი.")
data = [
{"name": "Ana", "grades": [90, 80, 95]},
{"name": "Beka", "grades": [70, 85, 88]},
{"name": "Nino", "grades": [100, 95, 99]}
]

my_lst = [{**st,"avg":round(sum(st["grades"])/len(st["grades"]),2)} for st in data]
max_vals = []
last_avg = [0]
for st in my_lst:  
    if st["avg"] > max(last_avg):
        max_vals = []
        max_vals.append(st)
    elif st["avg"] == max(last_avg):
        max_vals.append(st)
    last_avg.append(st["avg"])

print(max_vals)     
# #6 მოცემულია კომპანიების სია:
# {
# "companies": [
# {
# "name": "TechCorp",
# "employees": [
# {"name": "Ana", "salary": 3000},
# {"name": "Beka", "salary": 4500}
# ]
# },
# {
# "name": "SoftPlus",
# "employees": [
# {"name": "Nino", "salary": 5000},
# {"name": "Giorgi", "salary": 2500}
# ]
# }
# ]
# }
# იპოვე ყველა თანამშრომელი, რომლის ხელფასი მეტია 4000-ზე და დაბეჭდე
# მათი სახელები + კომპანიის სახელი.
print(f"-------------------------------------------------------------------6--------------------------------------------------------\n")
print(f"#6 მოცემულია კომპანიების სია:\nიპოვე ყველა თანამშრომელი, რომლის ხელფასი მეტია 4000-ზე და დაბეჭდე\nმათი სახელები + კომპანიის სახელი.")
data = {
"companies": [
{
"name": "TechCorp",
"employees": [
{"name": "Ana", "salary": 3000},
{"name": "Beka", "salary": 4500}
]
},
{
"name": "SoftPlus",
"employees": [
{"name": "Nino", "salary": 5000},
{"name": "Giorgi", "salary": 2500}
]
}
]
}

employees = [{"comp":comp["name"],"emp_name":emp["name"],"salary":emp["salary"]} for comp in data["companies"] for emp in comp["employees"] if emp["salary"] > 4000]
print(employees)
# #7 გააგზავნე GET მოთხოვნა https://jsonplaceholder.typicode.com/users და
# დაბეჭდე პირველი მომხმარებლის სახელი.
print(f"-------------------------------------------------------------------7--------------------------------------------------------\n")
print(f"#7 გააგზავნე GET მოთხოვნა https://jsonplaceholder.typicode.com/users და დაბეჭდე პირველი მომხმარებლის სახელი.")
response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()
print(data[0]["name"])

# #8 გააგზავნე POST მოთხოვნა https://jsonplaceholder.typicode.com/posts და
# შექმენი ახალი პოსტი შემდეგი მონაცემებით:
# {"title": "Test", "body": "Hello World", "userId": 5}
print(f"-------------------------------------------------------------------8--------------------------------------------------------\n")
print(f"#8 გააგზავნე POST მოთხოვნა https://jsonplaceholder.typicode.com/posts და\nშექმენი ახალი პოსტი შემდეგი მონაცემებით:\n{{'title': 'Test', 'body': 'Hello World', 'userId': 5}}")
data = {"title": "Test", "body": "Hello World", "userId": 5}
response = requests.post("https://jsonplaceholder.typicode.com/posts",json=data)
answer = response.json()
print(answer)
# #9 წამოიღე ყველა TODO task და დაბეჭდე მხოლოდ ის, სადაც "completed": False -
# https://jsonplaceholder.typicode.com/todos
# ბოლოს დათვალე რამდენი შეუსრულებელი ტასკია (რაოდენობაში)
print(f"-------------------------------------------------------------------9--------------------------------------------------------\n")
print(f"#9 წამოიღე ყველა TODO task და დაბეჭდე მხოლოდ ის, სადაც 'completed': False -\nhttps://jsonplaceholder.typicode.com/todos\nბოლოს დათვალე რამდენი შეუსრულებელი ტასკია (რაოდენობაში)")
response1 = requests.get("https://jsonplaceholder.typicode.com/todos")
response2 = requests.get("https://jsonplaceholder.typicode.com/todos?completed=false")
data1 = response1.json()
data2 = response2.json()
#ვარიანტი 1 ს თვის
uncomp = [task for task in data1 if not task["completed"]]
print(f"ვარიანტი 1: {uncomp}\n")
print(f"ვარიანტი 2: {data2}\n")
print(f"ვარიანტი 1: რაოდენობა = {len(uncomp)}")
print(f"ვარიანტი 2: რაოდენობა = {len(data2)}")

# #10 ამოიღე ყველა პოსტი https://jsonplaceholder.typicode.com/posts, შემდეგ
# იპოვე ავტორის სახელი (users API-დან) და დაბეჭდე:
# "Post Title – Author Name"
# გამოიტანე მხოლოდ პირველი 5
print(f"-------------------------------------------------------------------10--------------------------------------------------------\n")
print(f"#10 ამოიღე ყველა პოსტი https://jsonplaceholder.typicode.com/posts, შემდეგ.\nიპოვე ავტორის სახელი (users API-დან) და დაბეჭდე:\n'Post Title – Author Name'\nგამოიტანე მხოლოდ პირველი 5")
responsePosts = requests.get("https://jsonplaceholder.typicode.com/posts?_limit=5")
postData = responsePosts.json()
user_ids = set([usr["userId"] for usr in postData])

user_names= {}
## users response
for i in user_ids:
    userResponse = requests.get(f"https://jsonplaceholder.typicode.com/users?id={i}")
    user_data = userResponse.json() 
    user_names[i] = user_data[0]["name"]
## print Data
for post in postData:    
    print(f"{post["title"]} - {user_names[post["userId"]]}")


# დავალება დაწერეთ 1 ფაილში და ისე ატვირთეთ Classroom-ში
# ბაზებისთვის გამოიყენეთ: https://www.w3schools.com/sql/trysql.asp?filename=trysql_editor