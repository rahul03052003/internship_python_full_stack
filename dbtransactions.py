from dbconnection import Database

class Dbtransaction:
    def insertEmployee(self, name, age, phone, salary, depid, joining_date):
        con = Database().dbconnection()
        db = con.cursor()
        
        # Use %s placeholders for mysql-connector
        query = "INSERT INTO emp (name, age, phone, salary, depid, joining_date) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, age, phone, salary, depid, joining_date)
        
        db.execute(query, values)
        
        con.commit()
        db.close() # Good practice to close the cursor too
        con.close()
    def viewAnEmp(self, emp_id):
        con = Database().dbconnection()
        db = con.cursor()
        
        # Use a tuple (emp_id,) even for a single parameter
        query = "SELECT * FROM emp WHERE id = %s"
        db.execute(query, (emp_id,))
        
        row = db.fetchone()
        if row:
            print("\n--- Employee Details ---")
            print(f"ID: {row[0]}\nName: {row[1]}\nAge: {row[2]}\nPhone: {row[3]}\nSalary: {row[4]}\nDept ID: {row[5]}\nJoining Date: {row[6]}")
        else:
            print(f"No employee found with ID: {emp_id}")
            
        db.close()
        con.close()
    def update_emp(self,emp_id,new_age):
        con=Database().dbconnection()
        db=con.cursor()
        
        query="update emp set age=%s where id=%s"
        values=(new_age,emp_id)
        db.execute(query,values)
        con.commit()
        if db.rowcount > 0:
            print(f"Successfully updated record for ID {emp_id}.")
        else:
            print("Update failed. ID not found.")
        db.close()
        con.close()
    def delete_emp(self,emp_id):
        con=Database().dbconnection()
        db=con.cursor()
        
        query="Delete from emp where id=%s"
        db.execute(query,(emp_id,))
        con.commit()
        if db.rowcount > 0:
            print(f"Successfully deleted employee with ID {emp_id}.")
        else:
            print(f"Delete failed. No employee found with ID {emp_id}.")
        db.close()
        con.close()    