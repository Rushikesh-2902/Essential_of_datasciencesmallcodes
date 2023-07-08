f1=open("emp.csv","r")
f2=open("emp_date.csv","r")
f3=open("emp_new.csv","w")
d1=f1.read()
d2=f2.read()
l1=d1.splitlines()
l2=d2.splitlines()
for line1 in l1:
    info1=line1.split(',')
    for line2 in l2:
        info2=line2.split(',')
        if (info1[0]==info2[0]):
            data=line1+','+info2[1]+'\n'
            f3.write(data)
f1.close()
f2.close()
f3.close()
            
