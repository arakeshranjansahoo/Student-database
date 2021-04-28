#Create  and display in a Binary file
import pickle
import os
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
delete_rec()
display_all()


    
