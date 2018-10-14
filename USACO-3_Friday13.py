'''
ID:yourname here
LANG:PYTHON3
PROG:friday
'''
fin = open("friday.in",'r')
fout = open("friday.out",'w')
# The value of N
N = int(fin.readline())
Weekday = 0
WeekdayList = [0]

for i in range(1900,1900+N):
	monthList = [31,31,28,31,30,31,30,31,31,30,31,30]	
	if i % 4 == 0 and i != 1900 and i != 2100 and i != 2200 and i != 2300:
		monthList.remove(28)
		monthList.insert(2,29)
	if i == 1900:
		for j in monthList[1:]:
			remain = j % 7 
			Weekday += remain
			Weekday = Weekday % 7
			WeekdayList.append(Weekday)
			Weekday = Weekday % 7
	else:
		for j in monthList:
			remain = j % 7 
			Weekday += remain
			Weekday = Weekday % 7
			WeekdayList.append(Weekday)
			Weekday = Weekday % 7

Output = []

for x in range(0,7):
	Output.append(WeekdayList.count(x))
for i in Output[:6]:
	fout.write(str(i)+' ')
fout.write(str(Output[6])+'\n')






