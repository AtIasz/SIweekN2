months=["January","February","March","Aperil","May","June","July","September","October","November","December"]
cal=[[[""]*6]*3]*11
dais1=range(1,8)
dais2=range(8,15)
dais3=range(15,22)
dais4=range(22,29)
cal[6][1][0]+="Meeting with za Bossu" 
for i in range(len(months)):
    print(months[i])
    for j in range(4):
        
        for k in range(7):
            if j==0:
                print(dais1[k],end="")
            elif j==1:
                print(dais2[k],end="")
            elif j==2:
                print(dais3[k],end="")
            elif j==3:
                print(dais4[k],end="")
            print(" ",end="")
            if i==6 and j==1 and k==0:
                print(": "+cal[i][j][k],end=" ")
        print("")
    print("")