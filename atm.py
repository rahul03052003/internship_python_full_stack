import mysql.connector

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="atm_system"
)

cursor = conn.cursor()


# Create Account
def create_account():

    acc = int(input("Enter Account Number: "))
    name = input("Enter Name: ")
    pin = int(input("Set PIN: "))
    balance = int(input("Initial Deposit: "))

    cursor.execute(
        "INSERT INTO accounts VALUES(%s,%s,%s,%s)",
        (acc, name, pin, balance)
    )

    conn.commit()

    print("Account Created Successfully")


# Balance Check
def check_balance(acc):

    cursor.execute(
        "SELECT balance FROM accounts WHERE acc_no=%s",
        (acc,)
    )

    bal = cursor.fetchone()[0]

    print("Current Balance:", bal)


# Deposit Money
def deposit(acc):

    amount = int(input("Enter Deposit Amount: "))

    cursor.execute(
        "UPDATE accounts SET balance = balance + %s WHERE acc_no=%s",
        (amount, acc)
    )

    conn.commit()

    print("Deposit Successful")


# Withdraw Money
def withdraw(acc):

    amount = int(input("Enter Withdraw Amount: "))

    cursor.execute(
        "SELECT balance FROM accounts WHERE acc_no=%s",
        (acc,)
    )

    bal = cursor.fetchone()[0]

    if amount > bal:
        print("Insufficient Balance")
    else:

        cursor.execute(
            "UPDATE accounts SET balance = balance - %s WHERE acc_no=%s",
            (amount, acc)
        )

        conn.commit()

        print("Withdraw Successful")


# Login
def login():

    acc = int(input("Enter Account Number: "))
    pin = int(input("Enter PIN: "))

    cursor.execute(
        "SELECT * FROM accounts WHERE acc_no=%s AND pin=%s",
        (acc, pin)
    )

    user = cursor.fetchone()

    if user:

        print("Login Successful")

        while True:

            print("\nATM MENU")
            print("1. Balance Enquiry")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Logout")

            ch = int(input("Choose Option: "))

            if ch == 1:
                check_balance(acc)

            elif ch == 2:
                deposit(acc)

            elif ch == 3:
                withdraw(acc)

            elif ch == 4:
                print("Logged Out")
                break

            else:
                print("Invalid Option")

    else:
        print("Invalid Account Number or PIN")


# Main Menu
def main():

    while True:

        print("\nATM SIMULATION SYSTEM")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        ch = int(input("Enter Choice: "))

        if ch == 1:
            create_account()

        elif ch == 2:
            login()

        elif ch == 3:
            print("Thank You")
            break

        else:
            print("Invalid Choice")


main()