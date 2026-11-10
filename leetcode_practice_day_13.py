# Car Information System

# Create a Python program that:
# 1. Defines a class named Car.
# class car:

# # 2. Uses __init__() to receive brand, model, and year.
#     def __init__(self,brand,model,year):
# # 3. Stores these values using self.
#         self.model = model
#         self.year = year
#         self.brand = brand
# # 4. Creates a method named display_info() to print the car's details.
#     def display_info(self):
#         print("\nmodel: ",self.model)
#         print("year :",self.year)
#         print("brand :",self.brand)
# # 5. Creates two different car objects.

# car1= car("toyota","corolla",2010)
# car2= car("kia","sportage",2019)
# # 6. Calls display_info() for both objects.
# car1.display_info()
# car2.display_info()


# Bank Account
# 1. Create a BankAccount class.

class bankaccount:
# 2. Initialize owner and balance.
    def __init__(self,onwer,balance):
        self.owner = onwer
        self.balance = balance
        
# 3. Create deposit(amount) and withdraw(amount) methods.
    def deposit(self,amount):
        self.balance+= amount
        print(f"the amount of {amount} has been deposit in your account balance")

    def withdraw(self,amount):
        self.balance-= amount 
        self.amount = amount  
# 4. Prevent withdrawing more than the available balance.
        if self.amount >= self.balance and self.balance > 0:
            print(f"the amount of {amount} has been withdraw from your account balance")
        else:     
            print("not enough balance")
# 5. Display the final balance.
    def display_balance(self):
        print(f"the curreant balance of {self.owner} is :",self.balance)

a1=bankaccount("usman",0)
a1.deposit(2000)
a1.withdraw(2000)
a1.withdraw(3000)
a1.display_balance()