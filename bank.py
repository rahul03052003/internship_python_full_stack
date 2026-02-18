acc=[]
pins=[]
balances=[]


#help function

def find_acc(acc_no):
    try:
        return acc.index(acc_no)
    except ValueError:
        return -1

#Account create 
def create_acc():
    try:
        acc_no=input("Enter 4 digits account number:")
        if not(acc_no.isdigit() and len(acc_no)==4):
            print("Invalid account number")
            return
        if acc_no in acc:
            print("Account already exist")
            return
        pin=input("Enter 3 digit pin")
        if not(pin.isdigit() and len(pin)==3):
            print("Invalid PIN!")
            return
        amount=float(input("Enter the inital amount"))
        if(amount<=0):
            print("Amount must be greater than zero")
            return
        acc.append(acc_no)
        pins.append(pin)
        balances.append(amount)
        print("Account created successfully!")
    except ValueError:
        print("Invalid")


#login
def login():
    try:
        acc_no=input("Enter account number")
        pin=input("Enter PIN:")

        index=find_acc(acc_no)

        if index==-1 or pins[index]!=pin:
            print("Invalid account number or PIN!")
            return
        print("Login successfully")
        
        while True:
            print("\n1.Withdraw")
            print("2.Balance Enquiry")
            print("3.Deposit")
            print("4.Logout")

            choice=input("Choose Option:")
            if choice=="1":
                amt=float(input("Enter the withdraw amount:"))
                if amt<=0:
                    print("Amount much greater than 0")
                elif amt>balances[index]:
                    print("Insufficient Funds!")
                else:
                    balances[index]-=amt
                    print("Withdrawal successfully!")

            elif choice=="2":
                print("Current Balance: ",balances[index])
                
            elif choice=="3":
                amt=float(input("Enter deposit amount:"))
                if amt<=0:
                    print("Amount must be greater than 0")
                else:
                    balances[index]+=amt
                    print("Deposit successfully")
                    
            elif choice=="4":
                print("Logged out successfully")
                break
            else:
                print("Invalid choice!")
                
    except ValueError:
        print("Invalid input!")

#main
def main():
    while True:
        print("\n==== Welcome To ABC Bank ====")
        print("1.Create Account")
        print("2.Login")
        print("3.Exit")

        option=input("Enter choose:")

        if option=="1":
            create_acc()
        elif option=="2":
            login()
        elif option=="3":
            print("Thank You")
            break
        else:
            print("Invalid option!")
main()
        
        
           
