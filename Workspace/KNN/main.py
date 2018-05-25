import numpy as np
from knn import *



datasetcsv 	= "../Datasets/dataset1.csv"
dayscsv 	= "../Datasets/days.csv"
validationcsv = "../Datasets/validation1.csv"

conv = {5: lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)}
testSet = np.genfromtxt(dayscsv, 			 delimiter=';', usecols=[1,2,3,4,5,6,7], converters=conv)
validationSet = np.genfromtxt(validationcsv, delimiter=';', usecols=[1,2,3,4,5,6,7], converters=conv)

validationDates = np.genfromtxt(validationcsv, delimiter=';', usecols=[0])

cknn = CKNN(datasetcsv, 3)

valid = cknn.dateToSeason2(validationDates)

cknn.SetTestData(testSet)
#cknn.SetTestData(validationSet)

print(cknn.Run())




def testK(cknn):
	savedCnt = 0
	for k in range(100):
		cknn.setK(k)
		result = cknn.Run()
		cnt =0
		#print(result[0:50])
		#print(valid[0:50])
		for i in range(len(result)):
			if result[i] == valid[i]:
				cnt+=1
		if cnt > savedCnt:			
			savedCnt = cnt
			print("K = ", k ,")",cnt, "/", len(result))
		else:
			print("K = ", k ,")\t",cnt, "/", len(result))

	
#testK(cknn)


	




#optimale K = 30