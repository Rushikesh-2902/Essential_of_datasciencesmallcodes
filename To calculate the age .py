from datetime import datetime
tdate=datetime.today()
def Age_cal(edate):
    for i in edate:
        x=datetime.strptime(i,'%m/%d/%Y').date()
        print('age of emp is: ',(tdate.year-x.year))
    

    
fo=open("emp_new.csv","r")
str1=fo.read()
lst=str1.splitlines()
bd=[]
for d in lst:
    rw=d.split(',')
    bd.append(rw[5])
Age_cal(bd)
    
