# bank_system_mysql.py

from db_config import get_connection

conn = get_connection()
cursor = conn.cursor()

# --------------s---- Helper Functions ------------------

def account_exists(acc_no):
    cursor.execute("SELECT * FROM accounts WHERE acc_no = %s", (acc_no,))
    return cursor.fetchone() is not None

def get_account(acc_no, pin):
    cursor.execute("SELECT * FROM accounts WHERE acc_no = %s AND pin = %s", (acc_no, pin))
    return cursor.fetchone()

# ------------------ Account Creation ------------------

def create_account():
    acc_no = input("Enter 4 digit account number: ")
    if not (acc_no.isdigit() and len(acc_no) == 4):
        print("Invalid account number.")
        return

    if account_exists(acc_no):
        print("Account already exists!")
        return

    pin = input("Enter 3 digit PIN: ")
    if not (pin.isdigit() and len(pin) == 3):
        print("Invalid PIN.")
        return

    try:
        amount = float(input("Enter initial amount (>0): "))
        if amount <= 0:
            print("Amount must be > 0.")
            return
    except ValueError:
        print("Invalid amount!")
        return

    cursor.execute("INSERT INTO accounts (acc_no, pin, balance) VALUES (%s, %s, %s)",
                   (acc_no, pin, amount))
    conn.commit()
    print("✅ Account created successfully!")

# ------------------ Login ------------------

def login():
    acc_no = input("Enter account number: ")
    pin = input("Enter PIN: ")

    account = get_account(acc_no, pin)
    if not account:
        print("Invalid credentials!")
        return

    print("✅ Login successful!")

    while True:
        print("\n1. Withdraw")
        print("2. Balance Enquiry")
        print("3. Deposit")
        print("4. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            try:
                amt = float(input("Enter amount to withdraw: "))
                if amt <= 0:
                    print("Amount must be > 0.")
                    continue

                cursor.execute("SELECT balance FROM accounts WHERE acc_no = %s", (acc_no,))
                balance = cursor.fetchone()[0]

                if amt > balance:
                    print("Insufficient balance!")
                    continue

                new_balance = balance - amt
                cursor.execute("UPDATE accounts SET balance = %s WHERE acc_no = %s",
                               (new_balance, acc_no))
                conn.commit()
                print("Withdrawal successful.")

            except ValueError:
                print("Invalid amount!")

        elif choice == "2":
            cursor.execute("SELECT balance FROM accounts WHERE acc_no = %s", (acc_no,))
            balance = cursor.fetchone()[0]
            print(f"Current Balance: {balance}")

        elif choice == "3":
            try:
                amt = float(input("Enter amount to deposit: "))
                if amt <= 0:
                    print("Amount must be > 0.")
                    continue

                cursor.execute("SELECT balance FROM accounts WHERE acc_no = %s", (acc_no,))
                balance = cursor.fetchone()[0]
                new_balance = balance + amt

                cursor.execute("UPDATE accounts SET balance = %s WHERE acc_no = %s",
                               (new_balance, acc_no))
                conn.commit()
                print("Deposit successful.")

            except ValueError:
                print("Invalid amount!")

        elif choice == "4":
            print("Logged out.")
            break

        else:
            print("Invalid option!")

# ------------------ Main Menu ------------------

def main():
    while True:
        print("\n===== WELCOME TO ABC BANK =====")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        option = input("Enter choice: ")

        if option == "1":
            create_account()
        elif option == "2":
            login()
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

main()