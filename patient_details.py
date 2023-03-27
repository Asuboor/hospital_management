import datetime
from datetime import date
import mysql.connector as c


con=c.connect(host="localhost",username="root",password="yourPassword",database="patient")
cursor=con.cursor()



#login security code id=admin , password=admin
def login():
    staffid =input('enter staff id : ')
    if staffid !="admin" and staffid !="suboor" and staffid !="ali"and staffid !="fatha"and staffid !="fasi":
        print("enter correct id !!")
        login()
    while staffid == "admin" or staffid =="suboor" or staffid =="ali" or staffid =="fatha" or staffid =="fasi" :
            password =input('enter password : ')
            if (staffid == "admin" and password == "admin") or (staffid == "suboor" and password == "suboor") or (staffid == "fatha" and password == "fatha") or (staffid == "ali" and password == "ali") or (staffid == "fasi" and password == "fasi") :
                print("login successful")
                print("logged in @ :" ,datetime.datetime.now())
                print("welcome to records, "+staffid)
                global recp_id
                recp_id =staffid
                staffid = 0
            else :
                print("enter correct password!!")
    
login()

#insert function
def insert():
    cursor.execute('select pat_id from pat where pat_id=(select max(pat_id) from pat)')
    id=(cursor.fetchone())
    pat_id=int(''.join(map(str,id)))
    
    if pat_id :
        pat_id=pat_id+1
    else:
        pat_id=1

    pat_name=input(("Enter patient name:"))
    pat_age=int(input("Enter patient age:"))
    pat_sex=input("Gender:")
    pat_dob=input("Enter Date of Birth (Y-M-D):")
    doa=date.today()
    pat_doa=datetime.datetime.strptime("{}".format(doa), "%Y-%m-%d").strftime("%d/%m/%Y")
    pat_bg=input("Enter Blood Group:")
    pat_weight=int(input("Enter Weight:"))
    pat_contactno=int(input("Enter Contact No.:"))
    pat_CDoc=input("Enter Consulting Doctor:")
    query1="Insert into pat values({},'{}',{},'{}','{}','{}','{}',{},{},'{}')".format(pat_id,pat_name,pat_age,pat_sex,pat_dob,pat_doa,pat_bg,pat_weight,pat_contactno,pat_CDoc)
    cursor.execute(query1)
    con.commit()

    print("Data inserted successfully ")



#delete function
def delete():
    cursor.execute('select pat_id,pat_name from pat')
    print(cursor.fetchall())
    print('Enter record to be deleted')

    pat_id=int(input("Enter id:"))

    query2="delete from pat where pat_id={}".format(pat_id)
    cursor.execute(query2)
    con.commit()

    print("Record deleted successfully")


#retrieve function
def retrieve():
    pat_id=int(input("Enter id:"))
    cursor.execute('select * from pat where pat_id={}'.format(pat_id))
    print(cursor.fetchone())

 #menufunc switch case

def updatefunc():
    #("Enter id to update:")
    cursor.execute('select pat_id,pat_name from pat')
    print(cursor.fetchall())
    pat_id=int(input('id:'))
    cursor.execute('select * from pat where pat_id={}'.format(pat_id))
    print(cursor.fetchone())

    def pat_newname(pat_id):
        newname=input('Enter new name:')
        query4="update pat set pat_name='{}' where pat_id={}".format(newname,pat_id)
        print('Name updated successfully !')
        cursor.execute(query4)
        con.commit()

    def pat_newage(pat_id):
        newage=input('Enter new age:')
        query5="update pat set pat_age='{}' where pat_id={}".format(newage,pat_id)
        print('Age updated successfully !')
        cursor.execute(query5)
        con.commit()    

    def pat_newsex(pat_id):
        newsex=input('Enter new gender:')
        query6="update pat set pat_sex='{}' where pat_id={}".format(newsex,pat_id)
        print('Gender updated successfully !')
        cursor.execute(query6)
        con.commit()

    def pat_newdob(pat_id):
        newdob=input('Enter new Dob:')
        query7="update pat set pat_dob='{}' where pat_id={}".format(newdob,pat_id)
        print('dob updated successfully !')
        cursor.execute(query7)
        con.commit()
    
    def pat_newbg(pat_id):
        newbg=input('Enter new bloodgroup:')
        query10="update pat set pat_bg='{}' where pat_id={}".format(newbg,pat_id)
        print('bg updated successfully !')
        cursor.execute(query10)
        con.commit()

    def pat_newweight(pat_id):
        newweight=input('Enter new weight:')
        query8="update pat set pat_weight='{}' where pat_id={}".format(newweight,pat_id)
        print('weight updated successfully !')
        cursor.execute(query8)
        con.commit()

    def pat_newcontactno(pat_id):
        newcontactno=input('Enter new contactno:')
        query9="update pat set pat_contactno='{}' where pat_id={}".format(newcontactno,pat_id)
        print('contactno updated successfully !')
        cursor.execute(query9)
        con.commit()


    def pat_newCDoc(pat_id):
        newCDoc=input('Enter new consulting doctor:')
        query10="update pat set pat_CDoc='{}' where pat_id={}".format(newCDoc,pat_id)
        print('consulting doctor updated successfully !')
        cursor.execute(query10)
        con.commit()

    def updatation_switch(arg):

                        match arg:
                            case 1:
                                pat_newname(pat_id)
                                menufunc()
                            case 2:
                                pat_newage(pat_id)
                                menufunc()
                            case 3: 
                                pat_newsex(pat_id)
                                menufunc()
                            case 4:
                                pat_newdob(pat_id)
                                menufunc()
                            case 5:
                                pat_newbg(pat_id)
                                menufunc()
                            case 6:
                                pat_newweight(pat_id)
                                menufunc()
                            case 7:
                                pat_newcontactno(pat_id)
                                menufunc()
                            case 8:
                                pat_newCDoc(pat_id)
                                menufunc()
                            case 9:
                                menufunc() 
                            case default:
                                print("Please select from above options") 
                                updatation_switch(arg)

    def update_menu():

        print('1.Name 2.Age 3.Gender 4.Date Of Birth 5.Blood Group 6.weight 7.Contact no. 8.Consulting Doctor 9.Exit')
        arg=int(input('Enter Your choice:'))
        updatation_switch(arg)
    update_menu()

#menufunc switch case
def Hospital(argument):
    match argument:
        case 1:
            insert()
            menufunc()
        case 2:
            delete()
            menufunc()
        case 3:
            retrieve()
            menufunc()
        case 4:
            updatefunc()
            menufunc()
        case 5:
            print('program exited')
            exit(0)
        case default:
            print("Please select from above options") 
            menufunc()

#menufunc function
def menufunc():
    print('1.Insert 2.Delete 3.Retrieve 4.Update 5.Exit')
    argument=int(input('Enter Your choice:'))
    Hospital(argument)

menufunc()