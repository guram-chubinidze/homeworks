# ------------------------ ვებ-გვერდის ავტომატიზაცია ------------------------

# თქვენი მიზანია გააკეთოთ ვებ-გვერდის ავტომატიზაცია დრაივერის გამოყენებით:

# მისამართი: https://www.saucedemo.com/

# დავალება:

# 1. უნდა სცადოთ locked_out_user-ით ავტორიზაცია, ასევე უნდა დაიჭიროთ შეტყობინება რომელსაც დააბრუნებს გვერდი, ან გაივლის ავტორიზაციას.

# 2. უნდა სცადოთ performance_glitch_user-ით ავტორიზაცია, თუ გაივლით ავტორიზაციას უნდა გააკეთოთ logout, ან დაიჭიროთ error შეტყობინება

# 3. უნდა სცადოთ problem_user-ით ავტორიზაცია, თუ ვერ გაივლით ვიჭერთ error-ს, გავლის შემთხვევაში უნდა დაამატოთ 2 ნივთი კალათაში 
# და შემდეგ წაშალოთ ან დავიჭიროთ error (logout)

# 4. უნდა სცადოთ standard_user-ით ავტორიზაცია, თუ ვერ გაივლით ვიჭერთ error-ს, გავლის შემთხვევაში უნდა დაამატოთ 2 ნივთი კალათაში 
# და 5 წამის შემდეგ უნდა წაშალოთ ერთ-ერთი კალათიდან, ასევე უნდა შეხვიდეთ რომელიმე პროდუქტზე და 5 წამის შემდეგ დაბრუნდეთ მთავარ გვერდზე (back)-ით. 
# გამოიყენოთ სორტირება და ფასები დაალაგოთ High to Low, ბოლოს უნდა შეამოწმოთ footer-ის ნაწილი - გავაკეთოთ კლიკი ფეისბუქის icon-ზე 
# დავბრუნდეთ ისევ ვებ-გვერდზე და შემდეგ გავაკეთოთ კლიკი linkedin-ის icon-ზე და ისევ დავბრუნდეთ საიტზე, ამის შემდეგ გავაკეთოთ logout.

# აუცილებლად გამოიყენეთ unittest მოდული, ასევე გამოიყენეთ TestCase კლასი და ტესტები გაუშვით ფუნქციებად შინაარსობრივად უნდა გქონდეს მინიმუმ 4 ფუნქცია.

import logging
import random
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(
    filename='app.log',
    encoding='UTF-8',
    filemode='w', # 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level = logging.INFO
)

class User:
    
    def __init__(self,name):
        self.name = name
        self.password = "secret_sauce"
        self.status = "ავტორიზაცია ჯერ არ განხორციელებულა"
        logging.info(f"{self.name} - მომხმარებელის ინიციალიზაცია")
        
class SauceDemoPage:
    
    def __init__(self,driver,user):
        self.driver = driver  
        self.url = {"login": "https://www.saucedemo.com/",
                    "cart": "https://www.saucedemo.com/cart.html",
                    "product": "https://www.saucedemo.com/inventory-item.html?id="}       
        self.user = user 
        self.random_products_ids = [] 
        self.cart = []
            
    # ვებ-გვერდის შესაბამის გვერდზე გადასვლა (page უნდა იყოს string ტიპის)    
    def loadPage(self,page="login"):        
        self.driver.get(self.url[page]) 
        
    # პროდუქტის გვერდზე გადასვლა (product_id უნდა იყოს string ტიპის)  
    def open_product(self, product_id):
        # f-string-ით id-ის მიბმა
        target_url = f"{self.url['product']}{product_id}"
        self.driver.get(target_url)
        
    # ავტორიზაცია (login) ფუნქცია, რომელიც შეამოწმებს ავტორიზაციის შედეგს და შეინახავს სტატუსს    
    def login(self):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")
        
        username_field.send_keys(self.user.name)       
        password_field.send_keys(self.user.password)
        
        login_button.click()
        
        # ავტორიზაციის შედეგის შემოწმება და შენახვა
        error_msg = self.get_login_error_message()
        
        if error_msg:
            self.status = f" ვერ გაიარა ავტორიზაცია!\n შეცდომა: {error_msg}"
            logging.warning(f"{self.user.name} - მომხმარებელმა {self.status}")
        else:
            self.status = " წარმატებული ავტორიზაცია"
            logging.info(f"{self.user.name} - მომხმარებელმა გაიარა {self.status}")
        
    # ავტორიზაციის შეცდომის შეტყობინების მიღება (error message)    
    def get_login_error_message(self):
        try:
            error_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
            )
            return error_element.text
        except:
            return None
        
    # ლოგაუტის შეცდომის შეტყობინების მიღება (error message)
    def get_logout_error_message(self):
        
        try:    
            logout_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "logout_sidebar_link"))
            )
            self.driver.execute_script("arguments[0].click();", logout_element)
            return None
        except Exception as e:
                    error = f"Logout failed: {e}"
                    logging.error(error)
                    return error
                
    # პროდუქტის კალათაში დამატება (2 შემთხვევითი პროდუქტი)
    def add_to_cart(self):
        try:
            items = WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
                        )  
          
            logging.info(f"წარმატებით მოიძებნა {len(items)} პროდუქტი:") 
            print(f"წარმატებით მოიძებნა {len(items)} პროდუქტი:")
            
            random_idx = random.sample(range(len(items)), 2)  # Randomly select 2 unique indices
            # შემთხვევითი ინდექსების(2 ინდექსი) მიხედვით ვამატებთ პროდუქტებს კალათაში
            for i,item in enumerate(items):  
                product_label = item.find_element(By.CLASS_NAME,"inventory_item_label")  
                a_attribute = product_label.find_element(By.TAG_NAME, "a").get_attribute("id") 
                item_id = int(a_attribute.split("_")[1])  # 0          
                
                product_name = item.find_element(By.CLASS_NAME,"inventory_item_name").text
                product_price = item.find_element(By.CLASS_NAME,"inventory_item_price").text                
                btn = item.find_element(By.TAG_NAME,'button')
                text = btn.text                
                
                if i in random_idx:
                    btn.click()
                    time.sleep(5)  # Pauses execution for exactly 5 seconds
                    btn_text = item.find_element(By.TAG_NAME,'button')
                    self.random_products_ids.append(item_id)
                    if text != btn_text.text:
                        self.cart.append({'user':self.user, "id": item_id, 'name':product_name,'price':product_price})
                        print(f"პროდუქტი იდენტიფიკატორით {item_id}, სახელი =  '{product_name}', ფასი =  {product_price} კალათაში წარმატებით დაემატა კალათაში.")
                        logging.info(f"პროდუქტი '{product_name}' {product_price} კალათაში წარმატებით დაემატა კალათაში.")    
                    else:
                         print(f"პროდუქტის იდენტიფიკატორით {item_id}, სახელი =  '{product_name}', ფასი =  {product_price} კალათაში დაემატება ვერ მოხერხდა!")
                         logging.warning(f"პროდუქტის იდენტიფიკატორით {item_id}, სახელი =  '{product_name}', ფასი =  {product_price} კალათაში დაემატება ვერ მოხერხდა!") 
                
          
                    
        except Exception as e:
            logging.warning(f"პროდუქტების ჩატვირთვა ვერ მოესწრო ან ვერ მოიძებნა:{e}") 
            print(f"პროდუქტების ჩატვირთვა ვერ მოესწრო ან ვერ მოიძებნა:{e}")
            
        # პროდუქტის კალათიდან წაშლა
    def remove_from_cart(self, product_id):
        try:
            remove_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, f"remove-{product_id}"))
            )         
            remove_button.click()
            
            
            logging.info(f"პროდუქტი იდენტიფიკატორით {product_id} კალათიდან წარმატებით წაიშალა.")
            print(f"პროდუქტი იდენტიფიკატორით {product_id} კალათიდან წარმატებით წაიშალა.")
        except Exception as e:
            logging.warning(f"პროდუქტის იდენტიფიკატორით {product_id} კალათიდან წაშლა ვერ მოხერხდა: {e}")
            print(f"პროდუქტის იდენტიფიკატორით {product_id} კალათიდან წაშლა ვერ მოხერხდა: {e}")  
    # პროდუქტების სორტირება (sort products) ფუნქცია, რომელიც იღებს პარამეტრს sort_order, რომელიც განსაზღვრავს სორტირების წესს ("hilo" ან "lohi")
    def sort_products(self, sort_order="hilo"):
        try:
            sort_dropdown = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container"))
            )
            sort_dropdown.click()
            
            if sort_order == "hilo":
                option = self.driver.find_element(By.XPATH, "//option[@value='hilo']")
            elif sort_order == "lohi":
                option = self.driver.find_element(By.XPATH, "//option[@value='lohi']")
            else:
                logging.warning(f"მიუთითეთ სწორი სორტირების პარამეტრი: 'hilo' ან 'lohi'.")
                return
            
            option.click()
            logging.info(f"პროდუქტები წარმატებით დალაგდა {sort_order} მიხედვით.")
            print(f"პროდუქტები წარმატებით დალაგდა {sort_order} მიხედვით.")
        except Exception as e:
            logging.warning(f"პროდუქტების დალაგება ვერ მოხერხდა: {e}")
            print(f"პროდუქტების დალაგება ვერ მოხერხდა: {e}")     
           
    # სოციალური ქსელის icon-ზე კლიკი (click footer icon) ფუნქცია, რომელიც იღებს პარამეტრს icon_name,
    # რომელიც განსაზღვრავს რომელ icon-ზე უნდა მოხდეს კლიკი ("facebook" ან "linkedin")
    def click_footer_icon(self, icon_name):
     try:
        wait = WebDriverWait(self.driver, 10)
        main_window = self.driver.current_window_handle

        # 1. ელემენტის მოძებნა
        if icon_name.lower() == "facebook":
            css_selector = ".social_facebook a"
        elif icon_name.lower() == "linkedin":
            css_selector = ".social_linkedin a"
        elif icon_name.lower() == "twitter":
            css_selector = ".social_twitter a"
        else:
            logging.warning(
                "მიუთითეთ სწორი footer icon: 'facebook', 'linkedin' ან 'twitter'."
            )
            return

        social_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )

        # 2. კრიტიკული ნაბიჯი: ინახება sessionStorage-ის შიგთავსი (username) კლიკამდე
        user_session = self.driver.execute_script(
            "return sessionStorage.getItem('session-username');"
        )

        # 3. კლიკი
        social_btn.click()
        time.sleep(2)  # ველოდებით 2 წამს კლიკის შემდეგ
        # 4. ველოდებით ახალ ტაბს
        wait.until(EC.number_of_windows_to_be(2))

        # 5. გადავდივართ ახალ ტაბზე და ვხურავთ მას
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                self.driver.close()
                break

        # 6. ვბრუნდებით მთავარ ფანჯარაზე
        self.driver.switch_to.window(main_window)

        # 7. კრიტიკული ნაბიჯი: აღვადგენთ სესიას, თუ წაიშალა
        if user_session:
            self.driver.execute_script(
                f"sessionStorage.setItem('session-username', '{user_session}');"
            )

        # 8. თუ ბრაუზერმა მაინც გადაისროლა Login გვერდზე, ვაბრუნებთ ინვენტარზე
        if "inventory.html" not in self.driver.current_url:
            self.driver.get("https://www.saucedemo.com/inventory.html")

        logging.info(f"{icon_name} icon-ზე კლიკი წარმატებით შესრულდა.")
        print(f"{icon_name} icon-ზე კლიკი წარმატებით შესრულდა.")

     except Exception as e:
        logging.warning(f"{icon_name} icon-ზე კლიკი ვერ მოხერხდა: {e}")
        print(f"{icon_name} icon-ზე კლიკი ვერ მოხერხდა: {e}")          
            
    # ლოგაუტი (logout) ფუნქცია, რომელიც შეამოწმებს ლოგაუტის შედეგს და შეინახავს სტატუსს    
    def logout(self):               
        
            # Logout შედეგის შემოწმება
            logout_msg = self.get_logout_error_message()
            if logout_msg:
                        self.status = f"მომხმარებელი '{self.user.name}' - Logout ვერ  შესრულდა!\n შეცდომა: {logout_msg}"
                        logging.warning(self.status)
            else:
                        self.status = f"მომხმარებელი '{self.user.name}' -  წარმატებული Logout"
                        logging.info(self.status)                    
         
            
    # __STR__ 
    def __str__(self):
        return self.status    
        
    # Delete Object       
    def __del__(self):
        try:
            self.driver.quit()
        except:
            None       

print(f"-------------------------------------------------------------- 1 ------------------------------------------------------------------------")

# driver = webdriver.Firefox()
# user = User("locked_out_user")

# task1 = SauceDemoPage(driver,user)

# task1.loadPage()
# task1.login()
# print(task1)
# del task1


print(f"-------------------------------------------------------------- 2 ------------------------------------------------------------------------")

# driver = webdriver.Chrome()
# user = User("performance_glitch_user")

# task2 = SauceDemoPage(driver,user)

# task2.loadPage()
# task2.login()
# task2.logout()
# print(task2)
# del task2

print(f"-------------------------------------------------------------- 3 ------------------------------------------------------------------------")
# driver = webdriver.Edge()
# user = User("problem_user")

# task3 = SauceDemoPage(driver,user)

# task3.loadPage()
# task3.login()
# task3.add_to_cart()
# task3.loadPage('cart')
# # წაშალეთ კალათიდან პროდუქტები, რომლებიც დაემატა კალათაში (მხოლოდ 2 შემთხვევითი პროდუქტი)
# for product in task3.cart:
#     if product['id'] in task3.random_products_ids:
#        product_id =  product['name'].lower().replace(" ", "-")
#        task3.remove_from_cart(product_id)
# task3.logout()
# print(task3)
# del task3

print(f"-------------------------------------------------------------- 4 ------------------------------------------------------------------------")
# driver = webdriver.Chrome()
# user = User("standard_user")

# task4 = SauceDemoPage(driver,user)

# task4.loadPage()
# task4.login()
# task4.add_to_cart()
# task4.loadPage('cart')

# time.sleep(5)  # ველოდებით 5 წამს წაშლის წინ
# if task4.cart:
#        # წაშალეთ კალათიდან პროდუქტები, რომლებიც დაემატა კალათაში (მხოლოდ პირცელი პროდუქტი)
#        first_product = task4.cart[0] # პირველი პროდუქტი წავშალოთ 
#        if first_product['id'] in task4.random_products_ids:
#          product_id =  first_product['name'].lower().replace(" ", "-")
#          task4.remove_from_cart(product_id)
# else:
#     logging.warning("კალათაში არ არის დამატებული პროდუქტები, რომლებიც უნდა წაიშალოს!")
#     print("კალათაში არ არის დამატებული პროდუქტები, რომლებიც უნდა წაიშალოს.")      
# time.sleep(3)  # ველოდებით 3 წამს პროდუქტის წაშლის შემდეგ
# # გადავიდეთ რომელიმე პროდუქტზე (მეორეზე), ვნახოთ პროდუქტის დეტალები და დავბრუნდეთ უკან 
# product_id = task4.random_products_ids[1] # მეორე პროდუქტი   

# task4.open_product(str(product_id))
# logging.info(f"პროდეუქტის {product_id} დეტალების ნახვა წარმატებით შესრულდა.")
# print(f"პროდეუქტის {product_id} დეტალების ნახვა წარმატებით შესრულდა.")
# time.sleep(5)  # ველოდებით 5 წამს პროდუქტის დეტალებზე

# task4.driver.back()  # უკან დაბრუნება დეტალების გვერდზე

# logging.info(f"პროდეუქტის {product_id} დეტალების გვერდზე დაბრუნება წარმატებით შესრულდა.")
# print(f"პროდეუქტის {product_id} დეტალების გვერდზე დაბრუნება წარმატებით შესრულდა.")
# time.sleep(3)  # ველოდებით 3 წამს დეტალების გვერდზე დაბრუნების შემდეგ
# task4.driver.back()  # უკან დაბრუნება მთავარ გვერდზე

# time.sleep(3)  # ველოდებით 3 წამს მთავარ გვერდზე დაბრუნების შემდეგ
# logging.info(f"მთავარ გვერდზე დაბრუნება წარმატებით შესრულდა.")
# print(f"მთავარ გვერდზე დაბრუნება წარმატებით შესრულდა.")

# # სორტირება High to Low
# task4.sort_products("hilo")
# logging.info(f"პროდეუქტების სორტირება წარმატებით შესრულდა.")
# print(f"პროდეუქტების სორტირება წარმატებით შესრულდა.")
# time.sleep(3)  # ველოდებით 3 წამს სორტირების შემდეგ

# #სოციალური ქსელის icon-ზე კლიკი (facebook)
# task4.click_footer_icon("facebook")
# time.sleep(3)  # ველოდებით 3 წამს facebook icon-ზე კლიკის შემდეგ


# #სოციალური ქსელის icon-ზე კლიკი (linkedin)
# task4.click_footer_icon("linkedin") 
# time.sleep(3)  # ველოდებით 3 წამს linkedin icon-ზე კლიკის შემდეგ


# time.sleep(3)  # ველოდებით 3 წამს ლოგაუტის წინ
   
# task4.logout()
# print(task4)

# del task4


# ------------------------ UNITTEST TEST CASE ------------------------


class TestSauceDemoAutomation(unittest.TestCase):

    def setUp(self):
        # თითოეული ტესტის წინ იხსნება Chrome ბრაუზერი
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # თითოეული ტესტის დასრულებისას ბრაუზერი იხურება
        if self.driver:
            self.driver.quit()
# მუშაობა: locked_out_user-ის ტესტი უნდა შეამოწმოს ავტორიზაცია და დაიჭიროს error შეტყობინება.
    def test_01_locked_out_user(self):
        print(
            "\n--- ტესტი 1: locked_out_user ავტორიზაცია და Error შეტყობინება ---"
        )
        user = User("locked_out_user")
        page = SauceDemoPage(self.driver, user)

        page.loadPage()
        page.login()

        error_message = page.get_login_error_message()
        self.assertIsNotNone(
            error_message,
            "locked_out_user-ზე Error შეტყობინება უნდა დაბრუნებულიყო!",
        )
        print(f"შედეგი: {page}")
# მუშაობა: performance_glitch_user-ის ტესტი უნდა შეამოწმოს ავტორიზაცია და Logout, თუ ვერ გაივლის ვაჭერთ error შეტყობინებას, თუ გაივლის ვაჭერთ Logout-ს.
    def test_02_performance_glitch_user(self):
        print(
            "\n--- ტესტი 2: performance_glitch_user ავტორიზაცია და Logout ---"
        )
        user = User("performance_glitch_user")
        page = SauceDemoPage(self.driver, user)

        page.loadPage()
        page.login()
        page.logout()

        self.assertIn("წარმატებული Logout", page.status)
        print(f"შედეგი: {page}")
        
# შეცდომა: problem_user-ის ტესტი უნდა შეამოწმოს კალათის badge-ის მნიშვნელობა, რომელიც უნდა იყოს 2, მაგრამ problem_user-ზე ეს assert დავარდება (FAIL) და დაგიწერს ბაგის შესახებ, მაგრამ კოდი უხეშად არ დასქრაშავს!
    def test_03_problem_user(self):
        print(
            "\n--- ტესტი 3: problem_user დამატება/წაშლის ბაგის შემოწმება ---"
        )
        user = User("problem_user")
        page = SauceDemoPage(self.driver, user)

        page.loadPage()
        page.login()

        # 1. ვამოწმებთ ავტორიზაციას
        self.assertIn(
            "inventory.html",
            self.driver.current_url,
            "problem_user-მა ავტორიზაცია ვერ გაიარა!",
        )

        # 2. ვცდილობთ 2 ნივთის დამატებას
        page.add_to_cart()

        # 3. ვამოწმებთ, გაჩნდა თუ არა კალათის badge
        try:
            cart_badge_element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "shopping_cart_badge")
                )
            )
            badge_value = cart_badge_element.text
        except:
            badge_value = "0"  # თუ ელემენტი საერთოდ არ გამოჩნდა DOM-ში

        # ASSERT: ვამოწმებთ, რომ 2 ნივთი უნდა დამატებულიყო.
        # problem_user-ზე ეს assert დავარდება (FAIL) და დაგიწერს ბაგის შესახებ,
        # მაგრამ კოდი უხეშად არ დასქრაშავს!
        self.assertEqual(
            badge_value,
            "2",
            f"problem_user-მა ვერ დაამატა ნივთები კალათაში! კალათის badge-ის მნიშვნელობა: {badge_value}",
        )

        # 4. თუ დამატებამ მაინც იმუშავა, ვამოწმებთ წაშლას
        page.loadPage("cart")
        if page.cart:
            first_product = page.cart[0]
            product_id = first_product["name"].lower().replace(" ", "-")
            page.remove_from_cart(product_id)

            updated_badge = self.driver.find_element(
                By.CLASS_NAME, "shopping_cart_badge"
            ).text
            self.assertEqual(
                updated_badge,
                "1",
                f"problem_user-მა ვერ წაშალა ნივთი კალათიდან! დარჩა: {updated_badge}",
            )

        page.logout()
# მუშაობა: standard_user-ის ტესტი უნდა შეამოწმოს კალათის badge-ის მნიშვნელობა, სორტირება, ფუტერის ლინკები და Logout.
    def test_04_standard_user(self):
        print("\n--- ტესტი 4: standard_user ნამდვილი შემოწმებები (Asserts) ---")
        user = User("standard_user")
        page = SauceDemoPage(self.driver, user)

        page.loadPage()
        page.login()

        # 1. ვამოწმებთ წარმატებულ ავტორიზაციას
        self.assertIn(
            "inventory.html",
            self.driver.current_url,
            "ავტორიზაცია ვერ გაიარა!",
        )

        # 2. ვამატებთ 2 პროდუქტს და ვამოწმებთ კალათის count-ს (უნდა იყოს 2)
        page.add_to_cart()
        cart_badge = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge"
        ).text
        self.assertEqual(
            cart_badge,
            "2",
            "კალათაში 2 პროდუქტი არ დაემატა!",
        )

        # 3. ვშლით 1 პროდუქტს და ვამოწმებთ, რომ კალათაში დარჩა 1
        page.loadPage("cart")
        if page.cart:
            first_product = page.cart[0]
            product_id = first_product["name"].lower().replace(" ", "-")
            page.remove_from_cart(product_id)

            updated_badge = self.driver.find_element(
                By.CLASS_NAME, "shopping_cart_badge"
            ).text
            self.assertEqual(
                updated_badge,
                "1",
                "წაშლის შემდეგ კალათაში 1 პროდუქტი არ დარჩა!",
            )

        # 4. ვამოწმებთ სორტირებას (High to Low)
        page.driver.get("https://www.saucedemo.com/inventory.html")
        page.sort_products("hilo")

        # ვიღებთ ფასებს და ვამოწმებთ, რომ პირველი ფასი მეტია ან ტოლი მეორეზე
        prices_elements = self.driver.find_elements(
            By.CLASS_NAME, "inventory_item_price"
        )
        prices = [float(p.text.replace("$", "")) for p in prices_elements]

        self.assertGreaterEqual(
            prices[0],
            prices[1],
            "სორტირება High to Low არ იმუშავა!",
        )

        # 5. ვამოწმებთ ფუტერის ლინკების სისწორეს
        fb_link = self.driver.find_element(
            By.CSS_SELECTOR, ".social_facebook a"
        ).get_attribute("href")
        self.assertIn(
            "facebook.com",
            fb_link,
            "Facebook-ის ლინკი არასწორია!",
        )

        page.logout()


if __name__ == "__main__":
    unittest.main()
