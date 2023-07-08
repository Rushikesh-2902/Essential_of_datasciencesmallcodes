fo=open('empsal.csv',"r")
r=fo.read()
lines=r.splitlines()
fo.close()
s=str()
for line in lines:
    data=line.split(',')
    ns=str(int(data[4])/81.64)
    #print('salary in ind rupee: ' ,int(data[4]),',sal in us doller : ',ns,'$')
    #sid.append(ns)
    s=s+line+","+ns+"\n"
    
fw=open("emp_new.csv","w")
fw.write(s)
fw.close()
