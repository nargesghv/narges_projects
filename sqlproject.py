
import mysql
import mysql.connector

class person:
    def __init__(self,Name, Family, age, NationalCode, Education_Id) :
        self.Name=Name
        self.Family=Family
        self.age=age
        self.NationalCode=NationalCode
        self.Education_Id=Education_Id
    def getInfo(self):
        return (self.Name, self.Family, self.age,self.NationalCode,self.Education_Id)  

def tablelist(Cursor, tablename):
    Cursor.execute("select* from {}".format(tablename))
    return Cursor.fetchall()

def saveperson(person,Numbers):
    try:
        sqlcommand = "INSERT INTO person (Name,Family,age, NationalCode,Education_Id) VALUES (%s,%s,%s,%s,%s)"
        value=person.getInfo()
        Cursor.execute(sqlcommand,value)
        id=Cursor.lastrowid
        print("done")
        for number in Numbers:
            sqlcommand="INSERT INTO phone(Number, person_Id) VALUES (%s,%s)"
            value=(number,id)
            Cursor.execute(sqlcommand,value)
        connection.commit()
    
    except mysql.connector.Error as e:
        print (e)
        connection.rollback()


connection=mysql.connector.connect(host="localhost",user="root",password="new22852433",database="firstdatabase")
Cursor=connection.cursor()

#Cursor.execute("CREATE DATABASE firstdatabase")
Name=input("please enter your Name: ")
Family=input("please enter your family: ")
age=input("please enter your age: ")

NationalCode=input("please enter your National Code: ")

result=tablelist(Cursor,"education")


try:
    for item in result:
        print(item)

except TypeError as te:
    print(te)


Education_Id=input("Enter your Education Id: ")
p1=person(Name, Family, age, NationalCode,Education_Id)

Numbers=[]
hasNum=input("Do you have phone number:y/n ")
if hasNum=="y":
    end="y"
    while end=="y":
        numbe=input("please enter your number: ")
        Numbers.append(numbe)
        end=input("if is there any more phone: y/n")
    else:
        print("thanks for taking time!")
       



saveperson(p1,Numbers)




