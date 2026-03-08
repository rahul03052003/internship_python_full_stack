from dbconfig_student import get_connection

conn=get_connection()
cursor=conn.cursor()

#add student

def add_students():
    name=input("Enter the name: ")
    cls=input("Enter the class: ")
    
    cursor.execute(
        "insert into students(name,class)values(%s,%s)",(name,cls)
    )
    conn.commit()
    print("Student added successfully!")
    

#add subject

def add_subjects():
    subject=input("Enter subject name: ")
    cursor.execute(
        "insert into subjects(subject_name)values(%s)",(subject,)
    )
    conn.commit()
    print("Subject added successfully!")


#add marks

def add_marks():
    student_id=input("Enter student ID: ")
    subject_id=input("Enter subject ID: ")
    marks=input("Enter marks: ")
    cursor.execute(
        "insert into marks(student_id,subject_id,marks)values(%s,%s,%s)",(student_id,subject_id,marks)
    )
    conn.commit()
    print("Marks added successfully!")
    
#show results

def show_results():
    query="""
    select s.name,sum(m.marks) as total,
    avg(m.marks) as average
    from students s
    join marks m on s.id=m.student_id
    group by s.id
    order by total desc
    """
    cursor.execute(query)
    result=cursor.fetchall()
    
    print("\n--- Student Results ---")
    rank=1
    for row in result:
        print("Results:",rank)
        print("Name:",row[0])
        print("Total:",row[1])
        print("Average:",round(row[2],2))
        print("------------------------")
        rank+=1

# Pass / Fail
def pass_fail():

    query = """
    SELECT s.name,
           AVG(m.marks)
    FROM students s
    JOIN marks m ON s.id = m.student_id
    GROUP BY s.id
    """

    cursor.execute(query)
    result = cursor.fetchall()

    print("\n--- Pass / Fail List ---")

    for row in result:

        if row[1] >= 40:
            status = "PASS"
        else:
            status = "FAIL"

        print(row[0], ":", status)


# ---------------- Menu ----------------
def main():

    while True:

        print("\n===== STUDENT RESULT SYSTEM =====")
        print("1. Add Student")
        print("2. Add Subject")
        print("3. Add Marks")
        print("4. Show Results (Rank & Average)")
        print("5. Pass / Fail List")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_students()

        elif choice == "2":
            add_subjects()

        elif choice == "3":
            add_marks()

        elif choice == "4":
            show_results()

        elif choice == "5":
            pass_fail()

        elif choice == "6":
            print("Program closed")
            cursor.close()
            conn.close()
            break

        else:
            print("Invalid option")


main()