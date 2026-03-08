import mysql.connector as my

conn=my.connect(
    host="localhost",
    user="root",
    password="root",
    database="payroll_db"
)

cursor=conn.cursor()

def add_emp():
    name=input("Employee name: ")
    dept=input("Department: ")
    salary=int(input("Basic salary: "))
    
    cursor.execute(
        "insert into emp(name,department,basic_salary)values(%s,%s,%s)",(name,dept,salary)
    )
    
    conn.commit()
    print("Employee added")


def add_attendance():
    emp=input("Employee ID: ")
    days=int(input("Present days:"))
    
    cursor.execute(
        "insert into attendance(emp_id,presents_days)values(%s,%s)",(emp,days)
    )
    
    conn.commit()
    
    
def calculate_salary():
    emp=input("Employee ID:")
    cursor.execute("select basic_salary from emp where id=%s",(emp,))
    basic=cursor.fetchone()[0]
        
    cursor.execute("select presents_days from attendance where emp_id=%s",(emp,))
    days=cursor.fetchone()[0]
        
    gross=(basic/30)*days
    deduction=basic*0.1
    net=gross-deduction
        
    cursor.execute(
            "insert into salary(emp_id,gross,deductions,net)values(%s,%s,%s,%s)",(emp,gross,deduction,net)
    )
    conn.commit()
    print("Net salary: ",net)
        
        
        
def main():
    while True:
        print("\nPAYROLL SYSTEM")
        print("1 Add Employee")
        print("2 Add Attendance")
        print("3 Calculate Salary")
        print("4 Exit")

        ch = input("Choice: ")
        if ch=="1":
            add_emp()
        elif ch=="2":
            add_attendance()
        elif ch=="3":
            calculate_salary()
        elif ch=="4":
            break
main()
                