#Create  and display in a Binary file
import pickle
import os
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
    
def display_all():
    f=open("Student.dat","rb")
    try:
        while True:
            a=pickle.load(f)
            print(a)
    except EOFError:
        f.close()
       
create_rec()
display_all()
search_rec()


    
