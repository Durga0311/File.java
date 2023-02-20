burst=[]
arrive=[]
top=0
ct=[]
var=0
tat=[]
ch=0
wt=[]
n=int(input("enter the no.of process:"))
for i in range(n):
    i=int(input("enter the burst time:"))
    burst.append(i)
for i in range(n):
    i=int(input("enter the arrival time:"))
    arrive.append(i)
for i in range(n):
    if i==0:
        top=top+burst[i]
        ct.append(top)
    elif i>0:
         if top<arrive[i]:
                top=arrive[i]+burst[i]
                ct.append(top)
                
         else:
             top=top+burst[i]
             ct.append(top)
for i in range(n):
    var=ct[i]-arrive[i]
    tat.append(var)
for i in range(n):
     ch=tat[i]-burst[i]
     wt.append(ch)
print("| Process | Arrive |  Burst  |   ct  |  wt   |  tat  |")
for i in range(n):
     print("|",str(i+1),"|",str(arrive[i]),"|",str(burst[i]),"|",str(ct[i])," ","|",str(tat[i]),"|",str(wt[i]),"|")
avg_tat=0
for i in tat:
       avg_tat+=i
avg_tat=(avg_tat)/n
avg_wt=0
for i in wt:
       avg_wt+=i
avg_wt=(avg_wt)/n
avg_tat=0
for i in tat:
       avg_tat+=i
avg_tat=(avg_tat)/n
print("avg_wt:",avg_wt)
print("avg_tat:",avg_tat)



    

        


    
