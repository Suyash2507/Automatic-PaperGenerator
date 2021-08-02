import random
import mysql.connector
import sys
import smtplib
from email.message import EmailMessage
from fpdf import FPDF
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2809",
    database="mydatabase"
)


def modify(big):

    new = []
    neww = []
    inp = int(input("enter the number of problemetic qns"))
    for i in range(inp):
        k = int(input("enter code"))
        new.append(k)
    for i in big:
        if i[0] not in new:
            neww.append(i)
    for i in range(inp):
        ar = []
        a = int(input("enter Question code"))
        b = input("Enter your question")
        c = int(input("Enter weightage of the question(1/2/5 only)"))
        d = int(input("Enter level: "))
        e = input("Enter topic: ")
        mycursor = mydb.cursor()
        sql = "INSERT INTO yours (code,question,level,marks,topic) VALUES (%s,%s,%s,%s,%s)"
        val = (a, b, d, c, e)
        mycursor.execute(sql, val)
        mydb.commit()
        ar.append(a)
        ar.append(b)
        ar.append(c)
        neww.append(ar)
    count = 0
    for i in neww:
        count += 1
        print("%d %s (%d)" % (count, i[1], i[2]))
    a1 = input("Enter college name: ")
    a2 = input("Enter subject/topic name ")
    f = input("Enter Faculty name: ")
    a3 = int(input("Enter total marks: "))

    sys.stdout = open("sample.txt", "w")
    print(a1)
    print(a2)
    print(f)
    print("Maximum marks: %d" % (a3))
    count = 0
    for i in neww:
        count += 1
        print("%d %s (%d)" % (count, i[1], i[2]))
    sys.stdout.close()


def satisfied(big):
    sa = input("Are you satisfies with the questions? Yes/No")
    if sa == "Yes" or sa == "yes" or sa == "YES":
        count = 0
        for i in big:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
    else:
        print("Invalid Input")


def pdfconvert():
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=13)

    # open the text file in read mode
    f = open("sample.txt", "r")

    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1)

    # save the pdf with name .pdf
    pdf.output("sample.pdf")


print("enter your choice")
print("\n1.Randomized weightage paper with long question priority \n2.Randomized weightage paper with very short question priority \n3.manual setting of weightages \n")
print("Choose from the following topics:")
print("1. Introduction to Software Enginnering\n2. Requirement Engineering and metrics\n3. Design and architecture\n4. Testing Techniques\n5. Validation and Verification")


ch = int(input())
ph = int(input())
if ch == 1 and ph == 1:

    jlist = []

    def countqn(total):
        weightage = [5, 2, 1]
        count = [0, 0, 0]

        for i, j in zip(weightage, count):
            if total >= i:
                j = total // i
                total = total - j * i
                for l in range(0, 2):
                    jlist.append(j)
    print("please input marks")
    marks = int(input())
    countqn(marks)
    if(len(jlist) == 2):
       f = jlist[1]
       o = 0
       t = 0
    if(len(jlist) == 4):
       f = jlist[1]
       t = jlist[3]
       o = 0
    if(len(jlist) == 6):
       f = jlist[1]
       t = jlist[3]
       o = jlist[5]
    c = d = e = []

    mycursor1 = mydb.cursor()
    mycursor1.execute(
        "SELECT code,question,marks FROM se WHERE marks=1 and topic='introduction'")
    myresult1 = mycursor1.fetchall()
    alist = list(myresult1)
    if(o != 0):
        c = random.choices(alist, k=o)
        for x in range(len(c)):
            print(c[x])

    mycursor2 = mydb.cursor()
    mycursor2.execute(
        "SELECT code,question,marks FROM se WHERE marks=2 and topic='introduction'")
    myresult2 = mycursor2.fetchall()
    blist = list(myresult2)
    if(t != 0):
        d = random.choices(blist, k=t)
        for x in range(len(d)):
            print(d[x])
    mycursor3 = mydb.cursor()
    mycursor3.execute(
        "SELECT code,question,marks FROM se WHERE marks=5 and topic='introduction'")
    myresult3 = mycursor3.fetchall()
    clist = list(myresult3)
    if(f != 0):
        e = random.choices(clist, k=f)
        for x in range(len(e)):
            print(e[x])
    big = c+d+e
    print("Do you want to modify?")
    mod = input()
    if mod == "yes" or "Yes":
        modify(big)
    elif mod == "No" or "no":
        count = 0
        for i in big:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        a1 = input("Enter college name: ")
        a2 = input("Enter subject/topic name ")
        f = input("Enter Faculty name: ")
        a3 = int(input("Enter total marks: "))

        sys.stdout = open("sample.txt", "w")
        print(a1)
        print(a2)
        print(f)
        print("Maximum marks: %d" % (a3))
        count = 0
        for i in neww:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        sys.stdout.close()

    pdfconvert()


if ch == 1 and ph == 2:

    jlist = []

    def countqn(total):
        weightage = [5, 2, 1]
        count = [0, 0, 0]

        for i, j in zip(weightage, count):
            if total >= i:
                j = total // i
                total = total - j * i
                for l in range(0, 2):
                    jlist.append(j)
    print("please input marks")
    marks = int(input())
    countqn(marks)
    c = d = e = []
    if(len(jlist) == 2):
       f = jlist[1]
       o = 0
       t = 0
    if(len(jlist) == 4):
       f = jlist[1]
       t = jlist[3]
       o = 0
    if(len(jlist) == 6):
       f = jlist[1]
       t = jlist[3]
       o = jlist[5]

    mycursor1 = mydb.cursor()
    mycursor1.execute(
        "SELECT code,question,marks FROM se WHERE marks=1 and topic='reqt'")
    myresult1 = mycursor1.fetchall()
    alist = list(myresult1)
    if(o != 0):
        c = random.choices(alist, k=o)
        for x in range(len(c)):
            print(c[x])

    mycursor2 = mydb.cursor()
    mycursor2.execute(
        "SELECT code,question,marks FROM se WHERE marks=2 and topic='reqt'")
    myresult2 = mycursor2.fetchall()
    blist = list(myresult2)
    if(t != 0):
        d = random.choices(blist, k=t)
        for x in range(len(d)):
            print(d[x])
    mycursor3 = mydb.cursor()
    mycursor3.execute(
        "SELECT code,question,marks FROM se WHERE marks=5 and topic='reqt'")
    myresult3 = mycursor3.fetchall()
    clist = list(myresult3)
    if(f != 0):
        e = random.choices(clist, k=f)
        for x in range(len(e)):
            print(e[x])
    big = c+d+e
    print("Do you want to modify?")
    mod = input()
    if mod == "yes" or "Yes":
        modify(big)
    elif mod == "No" or "no":
        count = 0
        for i in big:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        a1 = input("Enter college name: ")
        a2 = input("Enter subject/topic name ")
        f = input("Enter Faculty name: ")
        a3 = int(input("Enter total marks: "))

        sys.stdout = open("sample.txt", "w")
        print(a1)
        print(a2)
        print(f)
        print("Maximum marks: %d" % (a3))
        count = 0
        for i in neww:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        sys.stdout.close()

    pdfconvert()
if ch == 1 and ph == 4:

    jlist = []
    c = d = e = []

    def countqn(total):
        weightage = [5, 2, 1]
        count = [0, 0, 0]

        for i, j in zip(weightage, count):
            if total >= i:
                j = total // i
                total = total - j * i
                for l in range(0, 2):
                    jlist.append(j)
    print("please input marks")
    marks = int(input())
    countqn(marks)
    if(len(jlist) == 2):
       f = jlist[1]
       o = 0
       t = 0
    if(len(jlist) == 4):
       f = jlist[1]
       t = jlist[3]
       o = 0
    if(len(jlist) == 6):
       f = jlist[1]
       t = jlist[3]
       o = jlist[5]

    mycursor1 = mydb.cursor()
    mycursor1.execute(
        "SELECT code,question,marks FROM se WHERE marks=1 and topic='test'")
    myresult1 = mycursor1.fetchall()
    alist = list(myresult1)
    if(o != 0):
        c = random.choices(alist, k=o)
        for x in range(len(c)):
            print(c[x])

    mycursor2 = mydb.cursor()
    mycursor2.execute(
        "SELECT code,question,marks FROM se WHERE marks=2 and topic='test'")
    myresult2 = mycursor2.fetchall()
    blist = list(myresult2)
    if(t != 0):
        d = random.choices(blist, k=t)
        for x in range(len(d)):
            print(d[x])
    mycursor3 = mydb.cursor()
    mycursor3.execute(
        "SELECT code,question,marks FROM se WHERE marks=5 and topic='test'")
    myresult3 = mycursor3.fetchall()
    clist = list(myresult3)
    if(f != 0):
        e = random.choices(clist, k=f)
        for x in range(len(e)):
            print(e[x])
    big = c+d+e
    print("Do you want to modify?")
    mod = input()
    if mod == "yes" or "Yes":
        modify(big)
    elif mod == "No" or "no":
        count = 0
        for i in big:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        a1 = input("Enter college name: ")
        a2 = input("Enter subject/topic name ")
        f = input("Enter Faculty name: ")
        a3 = int(input("Enter total marks: "))

        sys.stdout = open("sample.txt", "w")
        print(a1)
        print(a2)
        print(f)
        print("Maximum marks: %d" % (a3))
        count = 0
        for i in neww:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        sys.stdout.close()

    pdfconvert()
if ch == 2 and ph == 1:
    jlist = []
    c = d = e = []

    def countqn(total):
        weightage = [1, 2, 5]
        count = [0, 0, 0]

        for i, j in zip(weightage, count):
            if total >= i:
                j = total // i
                total = total - j * i
                for l in range(0, 2):
                    jlist.append(j)
    print("please input marks")
    marks = int(input())
    countqn(marks)
    if(len(jlist) == 2):
       o = jlist[1]
       t = 0
       f = 0
    if(len(jlist) == 4):
       o = jlist[1]
       t = jlist[3]
       f = 0
    if(len(jlist) == 6):
       o = jlist[1]
       t = jlist[3]
       f = jlist[5]

    mycursor1 = mydb.cursor()
    mycursor1.execute(
        "SELECT code,question,marks FROM se WHERE marks=1 and topic='introduction'")
    myresult1 = mycursor1.fetchall()
    alist = list(myresult1)
    if(o != 0):
        c = random.choices(alist, k=o)
        for x in range(len(c)):
            print(c[x])

    mycursor2 = mydb.cursor()
    mycursor2.execute(
        "SELECT code,question,marks FROM se WHERE marks=2 and topic='introduction'")
    myresult2 = mycursor2.fetchall()
    blist = list(myresult2)
    if(t != 0):
        d = random.choices(blist, k=t)
        for x in range(len(d)):
            print(d[x])
    mycursor3 = mydb.cursor()
    mycursor3.execute(
        "SELECT code,question,marks FROM se WHERE marks=5 and topic='introduction'")
    myresult3 = mycursor3.fetchall()
    clist = list(myresult3)
    if(f != 0):
        e = random.choices(clist, k=f)
        for x in range(len(e)):
            print(e[x])
    big = c+d+e
    print("Do you want to modify?")
    mod = input()
    if mod == "yes" or "Yes":
        modify(big)
    elif mod == "No" or "no":
        count = 0
        for i in big:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        a1 = input("Enter college name: ")
        a2 = input("Enter subject/topic name ")
        f = input("Enter Faculty name: ")
        a3 = int(input("Enter total marks: "))

        sys.stdout = open("sample.txt", "w")
        print(a1)
        print(a2)
        print(f)
        print("Maximum marks: %d" % (a3))
        count = 0
        for i in neww:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        sys.stdout.close()

    pdfconvert()

if ch == 2 and ph == 4:
    jlist = []
    c = d = e = []

    def countqn(total):
        weightage = [1, 2, 5]
        count = [0, 0, 0]

        for i, j in zip(weightage, count):
            if total >= i:
                j = total // i
                total = total - j * i
                for l in range(0, 2):
                    jlist.append(j)
    print("please input marks")
    marks = int(input())
    countqn(marks)
    if(len(jlist) == 2):
       o = jlist[1]
       t = 0
       f = 0
    if(len(jlist) == 4):
       o = jlist[1]
       t = jlist[3]
       f = 0
    if(len(jlist) == 6):
       o = jlist[1]
       t = jlist[3]
       f = jlist[5]

    mycursor1 = mydb.cursor()
    mycursor1.execute(
        "SELECT code,question,marks FROM se WHERE marks=1 and topic='test'")
    myresult1 = mycursor1.fetchall()
    alist = list(myresult1)
    if(o != 0):
        c = random.choices(alist, k=o)
        for x in range(len(c)):
            print(c[x])

    mycursor2 = mydb.cursor()
    mycursor2.execute(
        "SELECT code,question,marks FROM se WHERE marks=2 and topic='test'")
    myresult2 = mycursor2.fetchall()
    blist = list(myresult2)
    if(t != 0):
        d = random.choices(blist, k=t)
        for x in range(len(d)):
            print(d[x])
    mycursor3 = mydb.cursor()
    mycursor3.execute(
        "SELECT code,question,marks FROM se WHERE marks=5 and topic='test'")
    myresult3 = mycursor3.fetchall()
    clist = list(myresult3)
    if(f != 0):
        e = random.choices(clist, k=f)
        for x in range(len(e)):
            print(e[x])
    big = c+d+e
    print("Do you want to modify?")
    mod = input()
    if mod == "yes" or "Yes":
        modify(big)
    elif mod == "No" or "no":
        count = 0
        for i in big:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        a1 = input("Enter college name: ")
        a2 = input("Enter subject/topic name ")
        f = input("Enter Faculty name: ")
        a3 = int(input("Enter total marks: "))

        sys.stdout = open("sample.txt", "w")
        print(a1)
        print(a2)
        print(f)
        print("Maximum marks: %d" % (a3))
        count = 0
        for i in neww:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        sys.stdout.close()

    pdfconvert()
if ch == 2 and ph == 2:
    jlist = []
    c = d = e = []

    def countqn(total):
        weightage = [1, 2, 5]
        count = [0, 0, 0]

        for i, j in zip(weightage, count):
            if total >= i:
                j = total // i
                total = total - j * i
                for l in range(0, 2):
                    jlist.append(j)
    print("please input marks")
    marks = int(input())
    countqn(marks)
    if(len(jlist) == 2):
       o = jlist[1]
       t = 0
       f = 0
    if(len(jlist) == 4):
       o = jlist[1]
       t = jlist[3]
       f = 0
    if(len(jlist) == 6):
       o = jlist[1]
       t = jlist[3]
       f = jlist[5]

    mycursor1 = mydb.cursor()
    mycursor1.execute(
        "SELECT code,question,marks FROM se WHERE marks=1 and topic='reqt'")
    myresult1 = mycursor1.fetchall()
    alist = list(myresult1)
    if(o != 0):
        c = random.choices(alist, k=o)
        for x in range(len(c)):
            print(c[x])

    mycursor2 = mydb.cursor()
    mycursor2.execute(
        "SELECT code,question,marks FROM se WHERE marks=2 and topic='reqt'")
    myresult2 = mycursor2.fetchall()
    blist = list(myresult2)
    if(t != 0):
        d = random.choices(blist, k=t)
        for x in range(len(d)):
            print(d[x])
    mycursor3 = mydb.cursor()
    mycursor3.execute(
        "SELECT code,question,marks FROM se WHERE marks=5 and topic='reqt'")
    myresult3 = mycursor3.fetchall()
    clist = list(myresult3)
    if(f != 0):
        e = random.choices(clist, k=f)
        for x in range(len(e)):
            print(e[x])
    big = c+d+e
    print("Do you want to modify?")
    mod = input()
    if mod == "yes" or "Yes":
        modify(big)
    elif mod == "No" or "no":
        count = 0
        for i in big:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        a1 = input("Enter college name: ")
        a2 = input("Enter subject/topic name ")
        f = input("Enter Faculty name: ")
        a3 = int(input("Enter total marks: "))

        sys.stdout = open("sample.txt", "w")
        print(a1)
        print(a2)
        print(f)
        print("Maximum marks: %d" % (a3))
        count = 0
        for i in neww:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        sys.stdout.close()

    pdfconvert()

if ch == 3 and ph == 1:
    marks = int(input("Enter total marks"))
    f = int(input("enter number of 5 markers"))
    t = int(input("enter number of 2 markers"))
    o = int(input("enter number of 1 markers"))
    c = d = e = []
    mycursor1 = mydb.cursor()
    mycursor1.execute(
        "SELECT code,question,marks FROM se WHERE marks=1 and topic='introduction'")
    myresult1 = mycursor1.fetchall()
    alist = list(myresult1)
    if(o != 0):
        c = random.choices(alist, k=o)
        for x in range(len(c)):
            print(c[x])

    mycursor2 = mydb.cursor()
    mycursor2.execute(
        "SELECT code,question,marks FROM se WHERE marks=2 and topic='introduction'")
    myresult2 = mycursor2.fetchall()
    blist = list(myresult2)
    if(t != 0):
        d = random.choices(blist, k=t)
        for x in range(len(d)):
            print(d[x])
    mycursor3 = mydb.cursor()
    mycursor3.execute(
        "SELECT code,question,marks FROM se WHERE marks=5 and topic='introduction'")
    myresult3 = mycursor3.fetchall()
    clist = list(myresult3)
    if(f != 0):
        e = random.choices(clist, k=f)
        for x in range(len(e)):
            print(e[x])
    big = c+d+e
    print("Do you want to modify?")
    mod = input()
    if mod == "yes" or "Yes":
        modify(big)
    elif mod == "No" or "no":
        count = 0
        for i in big:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))

if ch == 3 and ph == 2:
    marks = int(input("Enter total marks"))
    f = int(input("enter number of 5 markers"))
    t = int(input("enter number of 2 markers"))
    o = int(input("enter number of 1 markers"))
    c = d = e = []
    mycursor1 = mydb.cursor()
    mycursor1.execute(
        "SELECT code,question,marks FROM se WHERE marks=1 and topic='reqt'")
    myresult1 = mycursor1.fetchall()
    alist = list(myresult1)
    if(o != 0):
        c = random.choices(alist, k=o)
        for x in range(len(c)):
            print(c[x])

    mycursor2 = mydb.cursor()
    mycursor2.execute(
        "SELECT code,question,marks FROM se WHERE marks=2 and topic='reqt'")
    myresult2 = mycursor2.fetchall()
    blist = list(myresult2)
    if(t != 0):
        d = random.choices(blist, k=t)
        for x in range(len(d)):
            print(d[x])
    mycursor3 = mydb.cursor()
    mycursor3.execute(
        "SELECT code,question,marks FROM se WHERE marks=5 and topic='reqt'")
    myresult3 = mycursor3.fetchall()
    clist = list(myresult3)
    if(f != 0):
        e = random.choices(clist, k=f)
        for x in range(len(e)):
            print(e[x])
        a1 = input("Enter college name: ")
        a2 = input("Enter subject/topic name ")
        f = input("Enter Faculty name: ")
        a3 = int(input("Enter total marks: "))

        sys.stdout = open("sample.txt", "w")
        print(a1)
        print(a2)
        print(f)
        print("Maximum marks: %d" % (a3))
        count = 0
        for i in neww:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        sys.stdout.close()

    pdfconvert()

if ch == 3 and ph == 4:
    marks = int(input("Enter total marks"))
    f = int(input("enter number of 5 markers"))
    t = int(input("enter number of 2 markers"))
    o = int(input("enter number of 1 markers"))
    c = d = e = []
    mycursor1 = mydb.cursor()
    mycursor1.execute(
        "SELECT code,question,marks FROM se WHERE marks=1 and topic='test'")
    myresult1 = mycursor1.fetchall()
    alist = list(myresult1)
    if(o != 0):
        c = random.choices(alist, k=o)
        for x in range(len(c)):
            print(c[x])

    mycursor2 = mydb.cursor()
    mycursor2.execute(
        "SELECT code,question,marks FROM se WHERE marks=2 and topic='test'")
    myresult2 = mycursor2.fetchall()
    blist = list(myresult2)
    if(t != 0):
        d = random.choices(blist, k=t)
        for x in range(len(d)):
            print(d[x])
    mycursor3 = mydb.cursor()
    mycursor3.execute(
        "SELECT code,question,marks FROM se WHERE marks=5 and topic='test'")
    myresult3 = mycursor3.fetchall()
    clist = list(myresult3)
    if(f != 0):
        e = random.choices(clist, k=f)
        for x in range(len(e)):
            print(e[x])
    big = c+d+e
    print("Do you want to modify?")
    mod = input()
    if mod == "yes" or "Yes":
        modify(big)
    elif mod == "No" or "no":
        count = 0
        for i in big:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        a1 = input("Enter college name: ")
        a2 = input("Enter subject/topic name ")
        f = input("Enter Faculty name: ")
        a3 = int(input("Enter total marks: "))

        sys.stdout = open("sample.txt", "w")
        print(a1)
        print(a2)
        print(f)
        print("Maximum marks: %d" % (a3))
        count = 0
        for i in neww:
            count += 1
            print("%d %s (%d)" % (count, i[1], i[2]))
        sys.stdout.close()

    pdfconvert()