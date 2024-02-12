# ATM Machine implementation using OOP 

class Atm:

    def __init__(self):

        self.pin = ""
        self.balnce = 0

        self.menu()

    def menu(self):
        while True:
            user_input = int(input("Choose your service\n 1 Create pin \n 2 deposit \n 3 Withdraw \n 4 Check Balance \n 5 Exit \n"))

            if user_input == 1:
                self.create_pin()
            elif user_input == 2:
                self.deposit()
            elif user_input == 3:
                self.withdraw()
            elif user_input == 4:
                self.check_balance()
            elif user_input == 5:
                print("Bye")
                break
            else:
                print("Invalid choice")

    
    def create_pin(self):
        self.pin = int(input("Enter pin"))
        print('Set successfully')
         
    def deposit(self):
        temp = int(input("Enter pin"))
        if temp == self.pin:
            amount = int(input("Enter amount"))
            self.balnce += amount
            print("Deposit successful")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = int(input("Enter pin"))
        if temp == self.pin:
            amount = int(input("Enter amount"))
            if amount < self.balnce:
                self.balnce -= amount
                print("Withdraw successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = int(input("Enter pin"))
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid")
sbi = Atm()



        
