import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Task 1
df=pd.read_excel('data_tasks.xlsx', sheet_name='task1')
print(df)
print(df.values[:,1])
time = df.values[:,0]
temp=df.values[:,1]
stdev=df.values[:,2]
#error=(1.96*stdev)/ # I would use the 95% CI but I don't know n, so I'll jsut assume the standard deviation is my error
line,caps,bars=plt.errorbar(
        time,
        temp,
        stdev,
        fmt="gs--",
        linewidth=2,
        elinewidth=.5,
        ecolor="k",
        capsize=5,
        capthick=1
        )
plt.xticks(time)
plt.yticks([0,5,10,15,20,25])
plt.legend(["Standard Deviation"], numpoints=1, loc=('upper left'))
plt.title("Moss Temperature in Spring", fontsize=24)
plt.xlabel("Time in minutes", fontsize=14)
plt.ylabel("Temperture in degrees C", fontsize=14)
plt.savefig('mossTempLine.png', dpi=600)
plt.show()


barWidth=.5
r1=[r+barWidth for r in range(len(temp))]
plt.bar(r1,
        temp,
        color="#7f6d5f",
        width=barWidth,
        edgecolor='white',
        label='Temperature',
        yerr=stdev,
        capsize=5)
plt.title("Moss Temperture in Spring", fontsize=24)
plt.legend(loc="upper right")
plt.xlabel('Minute', fontsize=12, fontweight="bold")
plt.ylabel("Temperture in degrees C",fontsize=12, fontweight ="bold")
plt.xticks([r+barWidth for r in range(len(temp))], ['1','2','3','4','5','6','7','8','9'])
plt.savefig('mossTempBar.png', dpi=600)
plt.show()
# Task 2
t2=pd.read_excel('data_tasks.xlsx', sheet_name='task2')
print(t2)
time=t2.values[1:,0]
vegasC=t2.values[1:,1]
vegasS=t2.values[1:,2]
durangoC=t2.values[1:,3]
durangoS=t2.values[1:,4]
denverC=t2.values[1:,5]
denverS=t2.values[1:,6]
barWidth=.2

r1=np.arange(len(vegasC))
r2=[i+barWidth for i in r1]
r3=[l+(2*barWidth) for l in r1]
line,caps,bars=plt.errorbar(
        time,
        vegasC,
        vegasS,
        color="#7f6d5f",
        fmt="s--",
        linewidth=2,
        elinewidth=.5,
        ecolor='k',
        capsize=5,
        capthick=1)
       

line2,caps2,bars2=plt.errorbar(
        time,
        durangoC,
        durangoS,
        fmt="bs--",
        linewidth=2,
        elinewidth=.5,
        ecolor='b',
        capsize=5,
        capthick=1)
line3,caps3,bars3=plt.errorbar(
        time,
        denverC,
        denverS,
        fmt="rs--",
        linewidth=2,
        elinewidth=.5,
        ecolor='r',
        capsize=5,
        capthick=1)
plt.title("City Tempertures", fontsize=24)
plt.legend(["Las Vegas", "Durango", "Denver"], loc= "upper left")
plt.xlabel('Hour', fontsize=12, fontweight="bold")
plt.ylabel('Temperature in degrees C', fontsize=12, fontweight="bold")
plt.savefig("cityTempLine.png", dpi=600)
plt.show()






plt.bar(r1, vegasC, color="#7f6d5f", width=barWidth, edgecolor='white', label='Las Vegas', yerr = vegasS, capsize=5)
plt.bar(r2, durangoC, color="blue", width=barWidth, edgecolor='white', label='Durango', yerr=durangoS, capsize=5)
plt.bar(r3, denverC, color="red", width=barWidth, edgecolor='white', label='Denver', yerr=denverS, capsize=5)
plt.title("City Tempertures", fontsize=24)
plt.legend(loc= "upper left")
plt.xlabel('Hour', fontsize=12, fontweight="bold")
plt.ylabel('Temperature in degrees C', fontsize=12, fontweight="bold")
plt.xticks([r+barWidth for r in range(len(vegasC))], ['1','2','3','4','5','6'])
plt.savefig('cityTempBar.png', dpi=600)
plt.show()


