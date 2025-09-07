import pickle
import os

class Emp:
    def __init__(self,eid,ename,basics):
        self.eid=eid
        self.ename=ename
        self.basics=basics

    def display(self):
        print(f"ID:{self.eid},Name:{self.ename},Basic salary:{self.basics}")

FILENAME ="emp.dat"
# 1. Add record

def add_record():
    eid=int(input("enter employee ID :"))
    ename=input("enter employee name:")
    basics=float(input("enter basic salary:"))
    e= Emp(eid,ename,basics)

    with open(FILENAME ,"ab") as f:pickle.dump(e,f)
    print("record added successfully!")

# 2. Search record

def search_record():
    eid=int(input("enter employee ID to search:"))
    found=False

    try:
        with open(FILENAME,"rb") as f:
            while True:
                e=pickle.load(f)
                if e.eid==eid:
                    print("record found:")
                    e.display()
                    found=True
                    break
    except EOFError:
        pass
    if not found:
        print("record not found!")

# 3. Delete Record

def delete_record():
    eid=int(input("enter employee ID to delete:"))
    found=False
    temp_file="temp.dat"
    with open(FILENAME,"rb") as f,open(temp_file,"wb")as t:
        try:
            while True:
                e=pickle.load(f)
                if e.eid !=eid:
                    pickle.dump(e,t)
                else:
                    found=True
        except EOFError:
            pass
    os.remove(FILENAME)
    os.rename(temp_file,FILENAME)
    if found:
        print("record deleted successfully!")
    else:
        print("record not found!")

# 4. Edit Record

def edit_record():
    eid=int(input("enter employee ID to edit:"))
    found=False
    temp_file="temp.dat"
    with open(FILENAME,"rb")as f,open(temp_file,"wb")as t:
        try:
            while True:
                e=pickle.load(f)
                if e.eid==eid:
                    print("existing record:")
                    e.display()
                    e.ename=input("enter new name:")
                    e.basics=input("enter new basics salary:")
                    found=True
                pickle.dump(e,t)
        except EOFError:
            pass
    os.remove(FILENAME)
    os.rename(temp_file,FILENAME)
    if found:
        print("record updated successfully!")
    else:
        print("record not found!")

# 5. Display All Records

def display_all():
    try:
        with open(FILENAME,"rb") as f:
            print("\nAll Employee Records:")
            while True:
                e= pickle.load(f)
                e.display()
    except EOFError:
        pass
    except FileNotFoundError:
        print("no records found yet!")

while True:
    print("\n===== employee management system =====")
    print("1.add record")
    print("2.search record")
    print("3.delete record")
    print("4.edit record")
    print("5.display all records")
    print("6.exit")

    ch=input("enter your choice:")

    if ch == "1":
        add_record()
    elif ch == "2":
        search_record()
    elif ch == "3":
        delete_record()
    elif ch == "4":
        edit_record()
    elif ch == "5":
        display_all()
    elif ch == "6":
        print("exiting program... Goodbye!")
        break
    else:
        print("invalid choice! please try again.")

