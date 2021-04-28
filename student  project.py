#Project on  Binary file
import pickle
import os
import sys

      
def create_rec():
    f=open("Student.dat","wb")
    while True:
        L=[]
        Roll_no=int(input("Enter the Roll no"))
        L.append(Roll_no)
        Stud_name=input("Enter the student name")
        L.append(Stud_name)
        Percentage=float(input("Enter the percentage"))
        L.append(Percentage)
        pickle.dump(L,f)
        ch=input("Do u want to enter more record(Y/N")
        if ch=='n' or ch=='N':
            break
    f.close()
   #========================================================================
def display_all():
    f=open("Student.dat","rb")
    try:
        while True:
            a=pickle.load(f)
            print(a)
    except EOFError:
        f.close()
  #========================================================================
def append_rec():
    f=open("Student.dat","ab")
    while True:
        L=[]
        Roll_no=int(input("Enter the Roll no"))
        L.append(Roll_no)
        Stud_name=input("Enter the student name")
        L.append(Stud_name)
        Percentage=float(input("Enter the percentage"))
        L.append(Percentage)
        pickle.dump(L,f)
        ch=input("Do u want to enter more record(Y/N")
        if ch=='n' or ch=='N':
            break
    f.close()
#========================================================================
def search_rec():
    f=open("Student.dat","rb+")
    a=int(input(" Enter the Roll no to be searched"))
    found=0
    try:
         while True and found==0:
             R=pickle.load(f)
             if R[0]==a:
                 print("found")
                 print(R)
                 found+=1
    except EOFError:
       print("record not found:")
       f.close()
#========================================================================
def update_rec():
    f=open("Student.dat","rb+")
    a=int(input(" Enter the Roll no to be updateded"))
    found=0
    pos=0
    try:
         while True and found==0:
             R=pickle.load(f)
             if R[0]==a:
                 f.seek(pos)
                 Salary=float(input("Enter the Modified Percentaage u want"))
                 R[2]=Salary
                 pickle.dump(R,f)
                 found+=1
             else:
                pos=f.tell()
    except EOFError:
       print("Record not found:")
       f.close()
#========================================================================
def delete_rec():
    f=open("Student.dat","rb")
    f1=open("Temp.dat","wb")
    a=int(input(" Enter the Roll no to be deleted"))
    found=0
    try:
        while True:
            R=pickle.load(f)
            if R[0]==a:
                found+=1
            else:
                pickle.dump(R,f1)
    except EOFError:
        f.close()
        f1.close()
    if found==0:
        print("Record not found")
    os.remove("Student.dat")
    os.rename("Temp.dat","Student.dat")
    
def exit_r():
    sys.exit("Exit from the program")
    
while True: 
    print("\t\t\t  MAIN MENU \n") 
    print("==============================================================") 
    print("1. Create Record              ") 
    print("2. Display Record          ")
    print("3. Append Record         ")
    print("4. Search Record           ") 
    print("5. Update  Record           ") 
    print("6. Delete  Record           ") 
    print("7. Return to Main Menu          ") 
    print("===============================================================") 
    choice=int(input("Enter Choice between 1 to 7-------> :  "))
        
    if choice==1:
        create_rec()
    elif choice==2:
        display_all()
    elif choice==3:
        append_rec()
    elif choice==4:
        search_rec()
    elif choice==5:
        update_rec()
    elif choice==6:
        delete_rec()
    elif choice==7:
        exit_r()
    else:
        print("You entered wrong option")
        


 






    
