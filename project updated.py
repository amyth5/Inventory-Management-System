#INVENTORY MANAGEMENT
import os
import pymysql
import datetime
now=datetime.datetime.now()



def PRODUCT_MANAGEMENT():
    while True:
        u='''        .......................
        .1.Add New Product    .
        .2.List Product       .
        .3.Update Product     .
        .4.Delete Product     .
        .5.Back to Menu       .
        .......................'''
        print(u)
        print("----------------------------------------------------------------")
        p=int(input("\t\t\t Enter your choice:"))
        if p==1:
            add_product()
        elif p==2:
            list_product()
        elif p==3:
            update_product()
        elif p==4:
            delete_product()
        elif p==5:
            break



def PURCHASE_MANAGEMENT():
    while True:
        print("\t\t\t 1.Add Order")
        print("\t\t\t 2.List Order")
        print("\t\t\t 3.Back To Menu")
        print("----------------------------------------------------------------")
        x=int(input("\t\t\t Enter your choice:"))
        if x==1:
            add_order()
        elif x==2:
            list_order()
        elif x==3:
            break
    
def SALES_MANAGEMENT():
    while True:
        print("\t\t\t 1.Sale Items")
        print("\t\t\t 2.List Sales")
        print("\t\t\t 3.Back To Menu")
        print("----------------------------------------------------------------")
        w=int(input("\t\t\t Enter your choice:"))
        if w==1:
            sale_product()
        elif w==2:
            list_sale()
        elif w==3:
            break
    
        
def USER_MANAGEMENT():
    while True:
        print("\t\t\t 1.Add User")
        print("\t\t\t 2.List User")
        print("\t\t\t 3.Back To Menu")
        print("----------------------------------------------------------------")
        u=int(input("\t\t\t Enter your choice:"))
        if u==1:
            add_user()
        if u==2:
            list_user()
        if u==3:
            break

def create_database():
    mydb=pymysql.connect(host="localhost",user="root",password="tiger")
    mycursor=mydb.cursor()
    mycursor.execute(" use ok")
    print("\t\tCREATING PRODUCT TABLE")
    sql="CREATE TABLE if not exists product(PCODE int(4) primary key, PNAME char(30),PPRICE float(8,2),PQTY int(4),PCAT char(30));"
    mycursor.execute(sql)
    print("\t---------------------------------------------------------")
    print("\t\t PRODUCT TABLE CREATED")
    print("\t---------------------------------------------------------")
    print("CREATING ORDER TABLE")
    sql="CREATE TABLE if not exists orders(ORDERID int(10) primary key,OrderDate DATE not null,PCODE char(30),PPRICE float(8,2),PQTY int(4),SUPPLIER char(50),PCAT char(30));"
    mycursor.execute(sql)
    print("\t---------------------------------------------------------")
    print("ORDER TABLE CREATED")
    print("\t---------------------------------------------------------")
    print("CREATING SALES TABLE")
    sql="CREATE TABLE if not exists sales(SALESID int(9) primary key, SalesDate DATE,PCODE char(30) references product(PCODE),PPRICE float(8,2),PQTY int(4),TOTAL DOUBLE(15,2));"
    mycursor.execute(sql)
    print("\t---------------------------------------------------------")
    print("SALES TABLE CREATED")
    print("\t---------------------------------------------------------")
    print("CREATING USER TABLE")
    sql="CREATE TABLE if not exists user(UID char(30) primary key,UNAME char(30),UPASSWORD char(30));"
    mycursor.execute(sql)
    print("\t---------------------------------------------------------")
    print("USER TABLE CREATED")

def list_database():
    mydb=pymysql.connect(host="localhost",user="root",password="tiger",database="ok")
    mycursor=mydb.cursor()
    sql="show tables;"
    mycursor.execute(sql)
    for i in mycursor:
        print(i)
        
def add_order():
    try:
        mydb=pymysql.connect(host="localhost",user="root",password="tiger",database="ok")
        mycursor=mydb.cursor()
        now=datetime.datetime.now()
        sql="INSERT INTO orders(ORDERID,OrderDate,PCODE,PPRICE,PQTY,SUPPLIER,PCAT)values(%s,%s,%s,%s,%s,%s,%s);"
        code=int(input("\t Enter Product Code:"))
        oid=now.year+now.month+now.day+now.hour+now.minute+now.second
        qty=int(input("\t Enter Product Quantity:"))
        price=float(input("\t Enter Product Unit Price:"))
        cat=input("\t Enter Product Category:")
        supplier=input("\t Enter Supplier Details:")
        val=(oid,now,code,price,qty,supplier,cat)
        mycursor.execute(sql,val)
        mydb.commit()
    except:
        pass


def list_order():
    mydb=pymysql.connect(host="localhost",user="root",password="tiger",database="ok")
    mycursor=mydb.cursor()
    sql="SELECT * from orders;"
    mycursor.execute(sql)
    print("\t\t\t\t\t\t\t ORDER DETAILS")
    print("\t\t","-"*92)
    print("\t\t ORDERID      DATE                PCODE      PRICE       QTY.       SUPPLIER   CATEGORY")
    print("\t\t","-"*92)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t\t",i[4],"\t\t",i[5],"\t\t",i[6])
    print("\t\t","-"*92)



def DATABASE_MANAGEMENT():
    while True:
        print("\t\t\t 1.Database Creation")
        print("\t\t\t 2.List Database")
        print("\t\t\t 3.Back To Menu")
        print("\t-------------------------------------------------------------------")
        y=int(input("\t\t Enter your Choice:"))
        if y==1:
            create_database()
        if y==2:
            list_database()
        if y==3:
            break

def add_product():
    mydb=pymysql.connect(host="localhost",user="root",password="tiger",database="ok")
    mycursor=mydb.cursor()
    sql="INSERT INTO product(PCODE,PNAME,PPRICE,PQTY,PCAT)values (%s,%s,%s,%s,%s);"
    code=int(input("\t Enter Product Code:"))
    search="SELECT count(*) FROM product WHERE PCODE=%s;"
    val=(code,)
    mycursor.execute(search,val)
    for x in mycursor:
        cnt=x[0]
    if cnt==0:
        name=input("\t Enter Product Name: ")
        qty=int(input("\t Enter Product Quantity:"))
        price=float(input("\t Enter Product Unit Price:"))
        cat=input("\t Enter Product Category:")
        val=(code,name,price,qty,cat)
        mycursor.execute(sql,val)
        mydb.commit()
    else:
        print("\t Product Already Exist")


def update_product():
    mydb=pymysql.connect(host="localhost",user="root",password="tiger",database="ok")
    mycursor=mydb.cursor()
    code=int(input("\t\t\t Enter Product Code:"))
    qty=int(input("\t\t\t Enter Quantity:"))
    sql="UPDATE product SET PQTY=PQTY+%s where PCODE=%s;"
    val=(qty,code)
    mycursor.execute(sql,val)
    mydb.commit()
    print("\t----------------------------------")
    print(" PRODUCT DETAILS UPDATED")
    

def delete_product():
    mydb=pymysql.connect(host="localhost",user="root",password="tiger",database="ok")
    mycursor=mydb.cursor()
    code=int(input("\t\t\t Enter Product Code:"))
    sql="DELETE FROM product WHERE PCODE=%s;"
    val=(code,)
    mycursor.execute(sql,val)
    mydb.commit()
    print("\t----------------------------------")
    print(mycursor.rowcount,"RECORD(s) DELETED")
    


def search_product():
    while True:
        print("\t\t\t 1.List All Product")
        print("\t\t\t 2.List Product Code Wise")
        print("\t\t\t 3.List Product Category Wise")
        print("\t\t\t 4.Back To Menu")
        print("\t-------------------------------------------------------------")
        s=int(input("\t\t\t Enter Your Choice:"))
        if s==1:
            list_product()
        if s==2:
            code=int(input("\t\t\t Enter Product Code:"))
            list_prcode(code)
        if s==3:
            cat=input("\t\t\t Enter Category:")
            list_prcat(cat)
        if s==4:
            break


def list_product():
    mydb=pymysql.connect(host="localhost",user="root",password="tiger",database="ok")
    mycursor=mydb.cursor()
    sql="select * from product;"
    mycursor.execute(sql)
    print("\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*60)
    print("\t\t CODE     NAME      PRICE(Rs)    QTY   CATEGORY")
    print("\t\t","-"*60)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
    print("\t\t","-"*60)    

    
def list_prcode(code):
    mydb=pymysql.connect(host="localhost",user="root",password="tiger",database="ok")
    mycursor=mydb.cursor()
    sql="SELECT * from product where PCODE=%s;"
    val=(code,)
    mycursor.execute(sql,val)
    print("\t\t\t\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*60)
    print("\t\t CODE     NAME      PRICE(Rs)    QTY   CATEGORY")
    print("\t\t","-"*60)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
    print("\t\t","-"*60)


def sale_product():
    try:
        mydb=pymysql.connect(host="localhost",user="root",password="tiger",database="ok")
        mycursor=mydb.cursor()
        pcode=input("Enter Product Code:")
        sql="SELECT count(*) from product where PCODE=%s;"
        val=(pcode,)
        mycursor.execute(sql,val)
        for x in mycursor:
            cnt=x[0]
        if cnt!=0:
            sql="select * from product where PCODE=%s;"
            val=(pcode,)
            mycursor.execute(sql,val)
            for x in mycursor:
                print(x)
                price=int(x[2])
                pqty=int(x[3])
            qty=int(input("Enter No. of Quantity:"))
            if qty<=pqty:
                total=qty*price
                print("Collect Rs",total)
                sql="INSERT into sales values(%s,%s,%s,%s,%s,%s);"
                val=(int(cnt)+1,datetime.datetime.now(),pcode,price,qty,total)
                mycursor.execute(sql,val)
                sql="update product set PQTY=PQTY-%s where PCODE=%s;"
                val=(qty,pcode)
                mycursor.execute(sql,val)
                mydb.commit()
            else:
                print("Quantity Not Available")
        else:
            print("Product Is Not Available")
    except:
        pass


def list_sale():
    mydb=pymysql.connect(host="localhost",user="root",password="tiger",database="ok")
    mycursor=mydb.cursor()
    sql="SELECT * from sales;"
    mycursor.execute(sql)
    print("\t\t\t SALES DETAILS")
    print("\t\t","-"*70)
    print("\t\t SALESID     DATE    PCODE     PRICE     QTY     TOTAL")
    print("\t\t","-"*70)
    for x in mycursor:
        print("\t\t",x[0],"\t",x[1],"\t",x[2],"\t",x[3],"\t",x[4],"\t",x[5])
    print("\t\t","-"*70)




def list_prcat(cat):
    mydb=pymysql.connect(host="localhost",user="root",password="tiger",database="ok")
    mycursor=mydb.cursor()
    print(cat)
    sql="select * from product where PCAT=%s;"
    val=(cat,)
    mycursor.execute(sql,val)
    clscr()
    print("\t\t\t\t PRODUCT DETAILS")
    print("\t\t","-"*47)
    print("\t\t CODE  NAME  PRICE QTY CATEGORY")
    print("\t\t","-"*47)
    for i in mycursor:
        print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
    print("\t\t","-"*47)


def add_user():
    mydb=pymysql.connect(host="localhost",user="root",password="tiger",database="ok")
    mycursor=mydb.cursor()
    uid=input("Enter Email ID:")
    uname=input("Enter Name:")
    upassword=input("Enter Password:")
    sql="insert into user values(%s,%s,%s);"
    val=(uid,uname,upassword)
    mycursor.execute(sql,val)
    mydb.commit()
    print("\t----------------------------------")
    print(mycursor.rowcount,"USER CREATED")


def list_user():
    mydb=pymysql.connect(host="localhost",user="root",password="tiger",database="ok")
    mycursor=mydb.cursor()
    sql="select UID,UNAME from user;"
    mycursor.execute(sql)
    print("\t\t\t USER DETAILS")
    print("\t\t","-"*27)
    print("\t\t\t UID          NAME")
    print("\t\t","-"*27)
    for i in mycursor:
        print("\t\t\t",i[0],"\t\t",i[1])
    print("\t\t","-"*27)

def clrscr():
    print("\n"*5)

while True:
    clrscr()

















    print("\t\t\t***********************************")
    print("\t\t\t***********INVENTORY\n                                       MANAGEMENT**********")
    print("\t\t\t***********************************\n")
    print("\t\t 1.PRODUCT MANAGEMENT")
    print("\t\t 2.PURCHASE MANAGEMENT")
    print("\t\t 3.SALES  MANAGEMENT")
    print("\t\t 4.USER MANAGEMENT")
    print("\t\t 5.DATABASE SETUP")
    print("\t\t 6.EXIT\n")
    n=int(input("enter your choice:"))
    
    if n==1:
        PRODUCT_MANAGEMENT()
    if n==2:
        
        PURCHASE_MANAGEMENT()
    if n==3:
        SALES_MANAGEMENT()
    if n==4:
        USER_MANAGEMENT()
    if n==5:
        DATABASE_MANAGEMENT()
    if n==6:
        break
    else:
        print('not correct')
    

