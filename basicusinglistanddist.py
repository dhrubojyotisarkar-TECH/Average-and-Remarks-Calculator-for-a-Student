name=input("Enter the student name :")
rollnumber=input("Enter the student roll number :")
n=int(input("Enter the number of subject:"))
est=[]
for i in range(0, n):
    ele = int(input("Enter the marks one by one:"))
  
    est.append(ele)

total=0
for j in range(0,n):
    total=total+est[j]

studentdetails = {
    "Name":name,
    "Roll number":rollnumber,
    "Marks":est,
    "Total marks":total
    }    
print(studentdetails)

print("Percentage :")
print(total/n)
if(total/n>=40):
    print("Remarks : Pass")
else:
    print("Remarks : Fail")

