#  Student Information System
#  1. Create a class Student.
class student:
#  2. Add a class variable university = "DUET".
    university ="DUET"
#  3. Initialize name, roll_no, and marks as instance variables.
    def __init__(self,name,roll_no,marks):
        self.name= name
        self.roll_no = roll_no
        self.marks = marks
        pass
    def display(self):
        print("\nuni :",self.university)
        print("name :",self.name)
        print("roll-no :",self.roll_no)
        print("marks :",self.marks)
#  4. Create three student objects.
s1 = student("usman",122,11)
s2 = student("aziz",124,11)
s3 = student("asim",143,12)
#  5. Display each student's information and university.
s1.display()
s2.display()
s3.display()
#  Concepts: Class variables, instance variables, constructor.


# Student Counter
# 1. Create a Student class.
class student:
# 2. Add a class variable total_students = 0.
    total_students = 0
# 3. Increment total_students whenever a new object is created.
    def __init__(self):
        student.total_students+=1
        
# 4. Create a class method show_total_students().
    @classmethod
    def show_total_students(cls):
        print("total_students :",cls.total_students)
# 5. Create five student objects and display the total count.
student()
student()
student.show_total_students()


# Bank Account Management System

# Create a BankAccount class with:
class BankAccount:
# - Class variable bank_name = "Python Bank".
    bank_name = "Python Bank"
# - Instance variables owner, account_number, and balance.
    def __init__(self,owner,account_no,balance):
        self.owner=owner
        self.account_no = account_no
        self.balance = balance  
# - Instance method deposit(amount).
    def deposit(self,amount):
        print(f"\nThe current balance for {self.owner} at {self.bank_name} (Account No: {self.account_no}) is {self.balance}.")
        self.balance+=amount
        print(f"the amount of {amount} has been deposit, the new balance is {self.balance}")
# - Instance method withdraw(amount) that prevents invalid withdrawals.
    def withdraw(self,amount):
        print(f"\nThe current balance for {self.owner} at {self.bank_name} (Account No: {self.account_no}) is {self.balance}.")
        if amount< self.balance:
            self.balance-=amount
            print(f"the amount of {amount} has been withdraw from account of {self.owner}")
        else:
            print("not enough balance")    
# - Class method change_bank_name(new_name).
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name = new_name
        print("\nnew bank name is",cls.bank_name)

        
# - Static method is_valid_amount(amount) that returns True for positive amounts.
    def is_valid_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0
# Create two accounts and test deposits, withdrawals, and bank-name changes.
ac1= BankAccount("usman",1234,1000)
ac2 = BankAccount("ali",4567,2000)
ac1.deposit(2000)
ac2.deposit(3000)
ac1.withdraw(4000)
ac2.withdraw(2000)
ac2.change_bank_name("dubai")
ac2.deposit(100)
