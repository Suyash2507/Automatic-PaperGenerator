import mysql.connector
import sys
from colorama import Fore, Back, Style
from colorama import init 
from fpdf import FPDF
import pyfiglet 
import re
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2809",
  database="mydatabase"
)
def main():
    user=input('Please Enter username: ')
    passwd = input('Please Enter a password: ')
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
      
    # compiling regex 
    pat = re.compile(reg) 
      
    # searching regex                  
    mat = re.search(pat, passwd) 
      
    # validating conditions 
    if mat: 
        print("Congratulations! You can proceed. ")
        sql = "INSERT INTO pwd (pwwd,username) VALUES (%s,%s)"
        val = (passwd,user)
        mycursor.execute(sql, val)
        mydb.commit()
    else: 
        print("Program Terminated. Registration Failed. ")
def search(list, a):
    for i in range(len(list)):
        if list[i] == a:
            return True
    return False
init(convert=True)
print(pyfiglet.figlet_format("Question Paper Generator", font = "digital" ) )
rootp=int(input('Please Enter root password to access the application: '))
if rootp==2809:
    ia=input('Are you a new user? Type Yes or No')
    if ia=='yes' or ia=='Yes' or ia=='YES':
        print(Fore.RED+'Set a password follwing the guidelines mentioned:\n1. Should have at least one number.\n2. Should have at least one uppercase and one lowercase character.\n3. Should have at least one special symbol.\n4. Should be between 6 to 20 characters long')
        if __name__ == '__main__': 
            main()
        print("Enter your choice: ")
        print("1. Insert new qn\n2. Delete old question\n3. Modify old question")
        ch=int(input())
        if ch==1:
    
            a=int(input("Enter Question code: "))
            b=input("Enter your question: ")
            c=int(input("Enter weightage of the question(1/2/5 only): "))
            d=int(input("Enter level: "))
            e=input("Enter topic: ")
            mycursor = mydb.cursor()
            sql = "INSERT INTO yours (code,question,level,marks,topic) VALUES (%s,%s,%s,%s,%s)"
            val = (a,b,d,c,e)
            mycursor.execute(sql, val)
            mydb.commit()
            print("New question added.")
        if ch==2:
            a=int(input("Enter Question code "))
            mycursor = mydb.cursor()

            sql = "DELETE FROM yours WHERE code=%s"
            val=(a)

            mycursor.execute(sql,val)

            mydb.commit()

            print("Record deleted")
        if ch==3:
            a=int(input("enter Question code"))
            ph=ch=int(input("What you wanna change?\n1. question\n2. level\n3. marks\n4. topic"))
            if ph==1:
                b=input("enter new question")
                mycursor = mydb.cursor()
                sql = "UPDATE yours SET  question= %s WHERE code =%s"
                val=(b,a)
                mycursor.execute(sql,val)
                mydb.commit()
                print("record affected")
            if ph==2:
                b=int(input("enter new level for your question: "))
                mycursor = mydb.cursor()
                sql = "UPDATE yours SET  level= %s WHERE code =%s"
                val=(b,a)
                mycursor.execute(sql,val)
                mydb.commit()
                print("record affected")
            if ph==3:
                b=int(input("enter new marks for your question: "))
                mycursor = mydb.cursor()
                sql = "UPDATE yours SET  marks= %s WHERE code =%s"
                val=(b,a)
                mycursor.execute(sql,val)
                mydb.commit()
                print("record affected")
            if ph==4:
                b=input("enter new topic for your question: ")
                mycursor = mydb.cursor()
                sql = "UPDATE yours SET  topic= %s WHERE code =%s"
                val=(b,a)
                mycursor.execute(sql,val)
                mydb.commit()
                print("record affected")
    

    else:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT pwwd FROM pwd")
        myresult = mycursor.fetchall()
        newb=input('please enter your existing username')
        pc=input('please enter your existing password')
        if search(myresult,pc):
            print('Login Successful')
            print("Enter your choice: ")
            print("1. insert new qn\n2. delete old question\n3. modify old question")
            ch=int(input())
            if ch==1:
    
                a=int(input("enter Question code"))
                b=input("Enter your question")
                c=int(input("Enter weightage of the question(1/2/5 only)"))
                d=int(input("Enter level: "))
                e=input("Enter topic: ")
                mycursor = mydb.cursor()
                sql = "INSERT INTO yours (code,question,level,marks,topic) VALUES (%s,%s,%s,%s,%s)"
                val = (a,b,d,c,e)
                mycursor.execute(sql, val)
                mydb.commit()
            if ch==2:
                a=int(input("enter Question code"))
                mycursor = mydb.cursor()

                sql = "DELETE FROM yours WHERE code=%s"
                val=(a)

                mycursor.execute(sql,val)

                mydb.commit()

                print("record deleted")
            if ch==3:
                a=int(input("enter Question code"))
                ph=ch=int(input("What you wanna change?\n1. question\n2. level\n3. marks\n4. topic"))
                if ph==1:
                    b=input("enter new question")
                    mycursor = mydb.cursor()
                    sql = "UPDATE yours SET  question= %s WHERE code =%s"
                    val=(b,a)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    print("record affected")
                if ph==2:
                    b=int(input("enter new level for your question: "))
                    mycursor = mydb.cursor()
                    sql = "UPDATE yours SET  level= %s WHERE code =%s"
                    val=(b,a)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    print("record affected")
                if ph==3:
                    b=int(input("enter new marks for your question: "))
                    mycursor = mydb.cursor()
                    sql = "UPDATE yours SET  marks= %s WHERE code =%s"
                    val=(b,a)
                    mycursor.execute(sql,val)
                    mydb.commit()
                print("record affected")
                if ph==4:
                    b=input("enter new topic for your question: ")
                    mycursor = mydb.cursor()
                    sql = "UPDATE yours SET  topic= %s WHERE code =%s"
                    val=(b,a)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    print("record affected")
        
        else:
                print('login successful')
                print("Enter your choice: ")
                print("1. insert new qn\n2. delete old question\n3. modify old question")
                ch=int(input())
                if ch==1:
    
                    a=int(input("enter Question code"))
                    b=input("Enter your question")
                    c=int(input("Enter weightage of the question(1/2/5 only)"))
                    d=int(input("Enter level: "))
                    e=input("Enter topic: ")
                    mycursor = mydb.cursor()
                    sql = "INSERT INTO yours (code,question,level,marks,topic) VALUES (%s,%s,%s,%s,%s)"
                    val = (a,b,d,c,e)
                    mycursor.execute(sql, val)
                    mydb.commit()
                if ch==2:
                    a=int(input("enter Question code"))
                    mycursor = mydb.cursor()

                    sql = "DELETE FROM yours WHERE code=%s"
                    val=(a)

                    mycursor.execute(sql,val)

                    mydb.commit()
                    print("record deleted")
                if ch==3:
                    a=int(input("enter Question code"))
                    ph=ch=int(input("What you wanna change?\n1. question\n2. level\n3. marks\n4. topic"))
                    if ph==1:
                        b=input("enter new question")
                        mycursor = mydb.cursor()
                        sql = "UPDATE yours SET  question= %s WHERE code =%s"
                        val=(b,a)
                        mycursor.execute(sql,val)
                        mydb.commit()
                        print("record affected")
                    if ph==2:
                        b=int(input("enter new level for your question: "))
                        mycursor = mydb.cursor()
                        sql = "UPDATE yours SET  level= %s WHERE code =%s"
                        val=(b,a)
                        mycursor.execute(sql,val)
                        mydb.commit()
                        print("record affected")
                    if ph==3:
                        b=int(input("enter new marks for your question: "))
                        mycursor = mydb.cursor()
                        sql = "UPDATE yours SET  marks= %s WHERE code =%s"
                        val=(b,a)
                        mycursor.execute(sql,val)
                        mydb.commit()
                        print("record affected")
                    if ph==4:
                        b=input("enter new topic for your question: ")
                        mycursor = mydb.cursor()
                        sql = "UPDATE yours SET  topic= %s WHERE code =%s"
                        val=(b,a)
                        mycursor.execute(sql,val)
                        mydb.commit()
                        print("record affected")
else:
    print('Program is terminated!!!')