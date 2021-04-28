#Create  and display and update in a Binary file
import pickle
import os
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
update_rec()
display_all()



    
