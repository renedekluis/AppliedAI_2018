import numpy as np
from KMeans import *
import matplotlib.pyplot as plt

datasetcsv 	= "../Datasets/dataset1.csv"
dayscsv 	= "../Datasets/days.csv"
validationcsv = '../Datasets/validation1.csv'

testSet = np.genfromtxt(dayscsv, delimiter=';', usecols=[1,2,3,4,5,6,7], converters={5: lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)})
validationSet = np.genfromtxt(validationcsv, delimiter=';', usecols=[1,2,3,4,5,6,7], converters={5: lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)})

validationDates = np.genfromtxt(validationcsv, delimiter=';', usecols=[0])


#checkDict = {}
KRange = 5
RunTimes = 10

distList = [None]
for k in range(1,KRange):
	distList.append(0)
	print('K =',k,')')
	
	for times in range(RunTimes):
		km = KMeans(datasetcsv, k)
		km.SetDates(validationDates)
		km.SetLabels()
		foundSeasons = km.RunKMeans(validationSet)
		distances = km.GetDistances()
		print('='*5)
		for x in foundSeasons:
			print(x[0], round(x[1],2),'%')
		totSom = 0
		for clust in distances:
			for punt in distances[clust]:
				totSom += punt
		distList[k] += totSom
	print('\n'*5)


plt.plot(range(0,KRange),distList)
plt.show()





'''
#TestLoop
for x in range(100):
	for i in range(kRange):
		checkDict[i] = []
	procCorrect = []
	distances = []
	for i in range(1,kRange):
		km = KMeans(datasetcsv, i)
		km.SetDates(validationDates)
		km.SetLabels()

		#checkLabels = km.GetSeasons2001(validationDates)
		foundSeasons = km.RunKMeans(validationSet)
		distances.append(km.GetDistances())
		
		
'''		
#		cnt = 0
#		for idx, date in enumerate(foundSeasons):
#			if checkLabels[date] == foundSeasons[date]:
#				cnt +=1
#		checkDict[i].append(cnt)
#	for k in checkDict:
#		if len(checkDict[k])>0:
#			procCorrect.append(np.average(checkDict[k]))
#	most = max(procCorrect)
#	idx = procCorrect.index(most)
#	print(x,') highest',most,'% With K =',idx)
print('\n'*5)

#Print the results		
#for la in checkDict:
#	if len(checkDict[la]) > 0:
#		print('K = ',la,') Average',np.average(checkDict[la]),'% correct')

'''
RESULTS K-MEANS
K range from 1 to 20.
Tested 100 times

With K = 14 the average correctness is 66%, which makes that the best K.
The detailed results are elaborated below.

K =   1 ) Average 30.0 % correct
K =   2 ) Average 44.0 % correct
K =   3 ) Average 47.0 % correct
K =   4 ) Average 47.0 % correct
K =   5 ) Average 53.0 % correct
K =   6 ) Average 47.0 % correct
K =   7 ) Average 55.0 % correct
K =   8 ) Average 60.0 % correct
K =   9 ) Average 60.0 % correct
K =  10 ) Average 61.0 % correct
K =  11 ) Average 63.0 % correct <-- Third
K =  12 ) Average 57.0 % correct
K =  13 ) Average 59.0 % correct
K =  14 ) Average 66.0 % correct <-- Highest average % correct
K =  15 ) Average 61.0 % correct
K =  16 ) Average 64.0 % correct <-- Second
K =  17 ) Average 63.0 % correct <-- Third
K =  18 ) Average 64.0 % correct <-- Second
K =  19 ) Average 59.0 % correct

Below are the exact results of the 100 tests
============================================
 0 ) highest 66.0 % With K = 15
 1 ) highest 68.0 % With K = 16
 2 ) highest 65.0 % With K = 17
 3 ) highest 65.0 % With K = 12
 4 ) highest 67.0 % With K = 18
 5 ) highest 68.0 % With K = 17
 6 ) highest 65.0 % With K = 15
 7 ) highest 65.0 % With K = 17
 8 ) highest 65.0 % With K = 18
 9 ) highest 66.0 % With K = 17
10 ) highest 65.0 % With K = 13
11 ) highest 65.0 % With K = 12
12 ) highest 66.0 % With K = 11
13 ) highest 62.0 % With K = 10
14 ) highest 65.0 % With K = 17
15 ) highest 65.0 % With K = 12
16 ) highest 64.0 % With K = 13
17 ) highest 66.0 % With K = 12
18 ) highest 66.0 % With K = 10
19 ) highest 65.0 % With K = 9
20 ) highest 66.0 % With K = 18
21 ) highest 68.0 % With K = 12
22 ) highest 68.0 % With K = 17
23 ) highest 66.0 % With K = 13
24 ) highest 63.0 % With K = 6
25 ) highest 64.0 % With K = 11
26 ) highest 66.0 % With K = 17
27 ) highest 66.0 % With K = 18
28 ) highest 64.0 % With K = 11
29 ) highest 65.0 % With K = 17
30 ) highest 66.0 % With K = 15
31 ) highest 62.0 % With K = 10
32 ) highest 69.0 % With K = 13 <-- Highest value of all tests
33 ) highest 63.0 % With K = 13
34 ) highest 66.0 % With K = 14
35 ) highest 67.0 % With K = 16
36 ) highest 64.0 % With K = 15
37 ) highest 66.0 % With K = 17
38 ) highest 64.0 % With K = 11
39 ) highest 63.0 % With K = 5
40 ) highest 66.0 % With K = 12
41 ) highest 65.0 % With K = 16
42 ) highest 67.0 % With K = 16
43 ) highest 67.0 % With K = 11
44 ) highest 64.0 % With K = 15
45 ) highest 66.0 % With K = 11
46 ) highest 65.0 % With K = 9
47 ) highest 64.0 % With K = 17
48 ) highest 64.0 % With K = 16
49 ) highest 66.0 % With K = 14
50 ) highest 67.0 % With K = 18
51 ) highest 67.0 % With K = 17
52 ) highest 64.0 % With K = 6
53 ) highest 66.0 % With K = 17
54 ) highest 65.0 % With K = 16
55 ) highest 65.0 % With K = 9
56 ) highest 67.0 % With K = 9
57 ) highest 67.0 % With K = 16
58 ) highest 67.0 % With K = 14
59 ) highest 64.0 % With K = 18
60 ) highest 67.0 % With K = 15
61 ) highest 68.0 % With K = 17
62 ) highest 66.0 % With K = 11
63 ) highest 66.0 % With K = 15
64 ) highest 66.0 % With K = 17
65 ) highest 64.0 % With K = 15
66 ) highest 63.0 % With K = 11
67 ) highest 65.0 % With K = 14
68 ) highest 66.0 % With K = 15
69 ) highest 67.0 % With K = 13
70 ) highest 65.0 % With K = 14
71 ) highest 67.0 % With K = 13
72 ) highest 65.0 % With K = 15
73 ) highest 65.0 % With K = 14
74 ) highest 66.0 % With K = 12
75 ) highest 66.0 % With K = 17
76 ) highest 65.0 % With K = 17
77 ) highest 65.0 % With K = 13
78 ) highest 66.0 % With K = 17
79 ) highest 66.0 % With K = 18
80 ) highest 64.0 % With K = 16
81 ) highest 64.0 % With K = 12
82 ) highest 65.0 % With K = 13
83 ) highest 69.0 % With K = 18 <-- Highest value of all tests
84 ) highest 64.0 % With K = 12
85 ) highest 66.0 % With K = 16
86 ) highest 65.0 % With K = 9
87 ) highest 66.0 % With K = 15
88 ) highest 67.0 % With K = 10
89 ) highest 64.0 % With K = 15
90 ) highest 69.0 % With K = 18 <-- Highest value of all tests
91 ) highest 64.0 % With K = 12
92 ) highest 65.0 % With K = 12
93 ) highest 65.0 % With K = 10
94 ) highest 67.0 % With K = 18
95 ) highest 66.0 % With K = 10
96 ) highest 65.0 % With K = 6
97 ) highest 65.0 % With K = 15
98 ) highest 65.0 % With K = 15
99 ) highest 66.0 % With K = 13



'''
