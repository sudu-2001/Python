import csv

with open("emp.csv","r",newline='') as file:

	reader=csv.reader(file)

	data=list(reader)

for i in range(1,len(data)):

	data[i][1]=str(float(data[i][1])*1.1)

with open("empc.csv","w",newline='') as file:

	writer=csv.writer(file)

	write=writer.writerows(data)

