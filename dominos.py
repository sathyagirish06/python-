import random
class dominos:
    menu={
        "veg":{"margerita":129,"cheese_n_corn":169,"peppi_paneer":260,"veg_lodead":210,"tomato_tangi":170},
        "non-veg":{"pepper_bbq":199,"non_veg_loaded":160,"chicken_sausage":200},
        "snack":{"garlic_bread":120,"zingy":59,"chicken_cheese_balls":170},
        "dessert":{"choco_lava":100,"mousse cake":169},
        "drinks":{"coke":90,"pepsi":70,"sprite":50}
    }
    def __init__(self,name,email,phno): 
        self.name=name
        self.email=email
        self.phno=phno
        self.login_status=False #to validate login status 
        self.cart={}#to store order
        #main program
        while True:
            if not self.login_status:
                print("-----------------------------------------------Welcome to dominos🍕 app------------------------------------------------ ")
                print("Login")
                ch=input("Do you u want to login(y/n):").lower()
                if ch=="y":
                    self.login()
            if self.login_status:
                print("-----------------------------------------------------------------------------------------------")
                print("user",self.name)
                print("Enter 1:order")
                print("Enter 2:show cart")
                print("Enter 3:logout")
                ch=int(input("Enter choice:"))
                if ch==1:
                    self.order()
                elif ch==2:
                    self.show_cart()
                elif ch==3:
                    self.logout()
                else:print("Ivalid choice")
    @staticmethod
    def validate_otp(value):
        while True:
            print("---------------------------------------------------------------------------------------------")
            og_otp=random.randint(1000,9999)
            print(f'An otp is sent{value}:')
            print(f'your dominos otp is {og_otp}')
            otp=int(input("Enter the OTP:"))
            if otp==og_otp:
                print("Login successful ✅")
                return True
            else:print("incorrect otp entered")
    
    def login(self):
        print("Enter1:login with phone no.")
        print("Enter2:login with email")
        ch=int(input("Enter choice:"))
        if ch==1:
            phno=int(input("Enter your phone no.:"))
            if phno==self.phno:
                state=self.validate_otp(phno)
                self.login_status=state
            else:
                print("In valid phone no.")
            print("phone no. validation")
        elif ch==2:
            email=input("Enter your email:")

            if email==self.email:
                state=self.validate_otp(email)
                self.login_status=state
            else:print("Invalid email")

           
            print("Email validation")
        else:
            print("Invalid choice")          
    def order(self):
        print('---------------------------------------------Menu---------------------------------------')
        for category in dominos.menu:
             print(category)   
        cat=input("Enter category:")
        if cat in dominos.menu:
            d=dominos.menu[cat]
            for item in d :            
              print(item,'',d[item])
            item=input("Enter item:")
            if item in d: 
                q=int(input("Enter the quantity:"))       
                if item in self.cart:    
                    self.cart[item]+=d[item]*q
                else:
                    self.cart[item]=d[item]
                print(f'{item} added to the cart')
                print(self.cart)
            else:
                print("item not available")
        else:
            print(f'{cat} not aviable sorry ❌')

    def show_cart(self):
        print('------------------------cart----------------------------')
        if self.cart!={}:
            Total_bill=0
            for item in self.cart:
                Total_bill+=self.cart[item]
                print(item,':',self.cart[item])
            print("Total bill:",Total_bill)
        else:print("Cart is empty please order 🛒")
        if self.cart!={}:
            ch=input("Do you want order(y/n):").lower()
            if ch=='y':
                print("Thank you for placing the order:")
                print("You order is no the way ")
                self.cart={}

    def logout(self):
        ch=input("Do you want logout (y/n):").lower()
        if ch=="y":
            self.login_status=False
            print("Logout successful")
        
ob=dominos("sathya","sathya@gmail.com",7338910014)
       