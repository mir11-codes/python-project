f=open("libmanage.dat","ab")
l=[]
f.close()

import pickle as pic
import os

def viewrecord(n):
    f=open("libmanage.dat","rb")
    found=-1
    while True:
        try:
            r=pic.load(f)
            if r[0]==n:
                found=1
                print("%15s"%'ISBN No.','%12s'%'Book Name','%8s'%'Price','%10s'%'Author','%12s'%'Publisher','%13s'%'Status')
                print("================================================================================")
                print('%10s'%r[0],'%15s'%r[1],'%10s'%r[2],'%11s'%r[3],'%12s'%r[4],'%16s'%r[5])
                

                #print("%15s"%'ISBN No.','%12s'%'Book Name','%8s'%'Price','%13s'%'Status')
                #print("===================================================================")
                #print('%10s'%r[0],'%15s'%r[1],'%10s'%r[2],'%18s'%r[3])
                
                '''print("isbn no: ",r[0])
                print("book: ",r[1])
                print("price: ",r[2])
                print("status: ",r[3])'''
        except(EOFError):
            if found==-1:
                print("record not found")
            break
    
    f.close()


def viewrecords():
    f=open('libmanage.dat','rb')
    
    print('%10s'%'ISBN','%11s'%'Book','%13s'%'Price','%11s'%'Author','%12s'%'Publisher','%9s'%'Status')
    print('================================================================================')
    while True:
        try:
            l=pic.load(f)
        except EOFError:
            break
        
        for i in range(len(l)):
            print('%11s'%l[i],end=' ')
        print()
    
    f.close()

def addrecord():
    f=open("libmanage.dat","rb+")
    isbn=input("enter isbn no.: ")
    found=-1
    while True:
        try:
            r=pic.load(f)
            if r[0]==isbn:
                found=1
        except(EOFError):
            break
    if found==1:
        print("record already exists")
        f.close()
        return
    book=input("enter book name: ")
    price=int(input("enter price: "))
    author=input("enter author's name: ")
    publisher=input("enter publisher: ")
    stat="available"
    r=[isbn,book,price,author,publisher,stat]
    pic.dump(r,f)
    l.append(r)
    f.close()
    print("record added")

def modifyrecord(n):
    f1=open("libmanage.dat","rb")
    f2=open("temporary.dat","ab")
    found=0
    
    while True:
        try:
            r=pic.load(f1)
            #pic.dump(r,f2)           
            isbn=r[0]
            book=r[1]
            price=r[2]
            author=r[3]
            publisher=r[4]
            stat=r[5]
    
            if isbn==n:
                found=1
                print("book: ",book)
                b=input("modify book name?(y/n): ")
                if b.lower()=="y":
                    new=input("enter new book name: ")
                    book=new

                    print("author :",author)
                    newa=input("enter new author's name: ")
                    author=newa
                    newu=input("enter new publisher: ")
                    publisher=newu
                    
                elif b.lower()=="n":
                    pass
                print("price: ",price)
                p=input("modify price?(y/n): ")
                if p.lower()=="y":
                    newp=int(input("enter new price: "))
                    price=newp
                elif p.lower()=="n":
                    pass
                
                
                m=[isbn,book,price,author,publisher,stat]
                pic.dump(m,f2)
                #print(m)
                l.append(m)
                print("record modified")
        except:
            break
    pic.dump(r,f2)
    
    f1.close()
    f2.close()
    if found==0:
        print("record not found")
        os.remove("temporary.dat")
    if found==1:
        os.remove("libmanage.dat")
        os.rename("temporary.dat","libmanage.dat")

def deleterecord(n):
    f1=open("libmanage.dat","rb")
    f2=open("temporary.dat","ab")
    found=0
    deleted=0
    while True:
        try:
            d=0
            r=pic.load(f1)
            isbn=r[0]
            book=r[1]
            price=r[2]
            author=r[3]
            publisher=r[4]
            stat=r[5]
            if isbn==n:
                found=1
                verify=input("do you want to delete?(y/n): ")
                if verify.lower()=="y":
                    print("record deleted")
                    d=1
                    deleted=1
                else:
                    print('record not deleted')
            elif d==0:
                r=[isbn,book,price,author,publisher,stat]
                pic.dump(r,f2)
                
                l.append(r)
        except:
            break
    f1.close()
    f2.close()
    if found==0:
        print('record not found')
        os.remove("temporary.dat")
    elif deleted==1:
        os.remove("libmanage.dat")
        os.rename("temporary.dat","libmanage.dat")
    else:
        os.remove("temporary.dat")

def issue(n):
    f1=open("libmanage.dat","rb")
    f2=open("temporary.dat","ab")
    found=0
    while True:
        try:
            r=pic.load(f1)
            isbn=r[0]
            book=r[1]
            price=r[2]
            author=r[3]
            publisher=r[4]
            stat=r[5]
            if isbn==n:
                found=1
                if stat=="out of stock" or stat=="issued":
                    print("sorry book not available!(ISSUED/OUT OF STOCK)")
                else:
                    print("book name: ",book)
                    print("price: ",price)
                    print("author name: ",author)
                    print("publisher: ",publisher)
                    print("availability: ",stat)
                    v=input("do you want to proceed?(y/n): ")
                    if v.lower()=="y":
                        stat="issued"
                        print("availability: ",stat)
                        print("book issued")
            r=[isbn,book,price,author,publisher,stat]
            pic.dump(r,f2)
            l.append(r)
        except:
            break
    f1.close()
    f2.close()
    if found==0:
        print("Record not found")
        os.remove("temporary.dat")
    elif found==1:
        os.remove("libmanage.dat")
        os.rename("temporary.dat","libmanage.dat")

def returnb(n):
    f1=open("libmanage.dat","rb")
    f2=open("temporary.dat","ab")
    found=0
    while True:
        try:
            r=pic.load(f1)
            isbn=r[0]
            book=r[1]
            price=r[2]
            author=r[3]
            publisher=r[4]
            stat=r[5]
            if isbn==n:
                found=1
                if stat=="issued":
                    print("book name: ",book)
                    print("price: ",price)
                    print("author name: ",author)
                    print("publisher: ",publisher)
                    print("availability: ",stat)
                    v=input("do you want to proceed?(y/n): ")
                    expire=input("is the book date expired?(y/n):")
                    total=price
                    if expire.upper()=="Y":
                        day=int(input("by how many days is the book returned late? "))
                        fine=2*day
                        total+=fine
                   # print("final total: ",total)
                    if v.lower()=="y":
                        stat="available"
                        #print("availability: ",stat)
                        #print("book returned")
                        print("           RECEIPT           ")
                        print("Final Total:",         total)
                        print("Availability:",       stat)
                        print("*******************************")
                        print("book returned")
                elif stat=="available":
                    print("book already available")
                else:
                    print('book is out of stock')
            r=[isbn,book,price,author,publisher,stat]
            pic.dump(r,f2)
            l.append(r)
        except:
            break
    f1.close()
    f2.close()
    if found==0:
        print("record not found")
        os.remove("temporary.dat")
    elif found==1:
        os.remove("libmanage.dat")
        os.rename("temporary.dat","libmanage.dat")

ch=0
while ch!=9:
    print("                                                                      ")
    print("                         LIBRARY MANAGEMENT                           ")
    print("                          ARCHIE'S LIBRARY                          ")
    print("                                                                    ")
    print("                            MAINTENANCE                             ")
    print("1. view book details by ISBN")
    print("2. view all books")
    print("3. add book details ")
    print("4. edit book details")
    print("5. remove book")
    print("                             LIBRARY                                  ")
    print("6. Issue book")
    print("7. return book")
    print("**********************************************************************")
    print("8. Exit")
 
    ch=int(input("Enter  choice (1/2/3/4/5/6/7/8): "))
    
    if ch==1:
        n=input("enter isbn value: ")
        viewrecord(n)
    elif ch==2:
        viewrecords()
    elif ch==3:
        addrecord()
    elif ch==4:
        n=input("enter isbn value: ")
        modifyrecord(n)
    elif ch==5:
        n=input("enter isbn value: ")
        deleterecord(n)
    elif ch==6:
        n=input("enter isbn value: ")
        issue(n)
    elif ch==7:
        n=input("enter isbn value: ")
        returnb(n)
    elif ch==8:
        print("thanks for using library management system")
        break
    else:
        print("please input valid choice from 1-8")
        
                    
