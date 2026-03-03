import mysql.connector as mq
class Database:
    def dbconnection(self):
        con=mq.connect(host="localhost",database="company",user="root",password="root")
        return con
