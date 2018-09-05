from KNN import *



datasetcsv 	= "../Datasets/dataset1.csv"
dayscsv 	= "../Datasets/days.csv"
validationcsv = "../Datasets/validation1.csv"


conv = {5: lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)}
testSet = np.genfromtxt(dayscsv, 			 delimiter=';', usecols=[1,2,3,4,5,6,7], converters=conv)
validationSet = np.genfromtxt(validationcsv, delimiter=';', usecols=[1,2,3,4,5,6,7], converters=conv)

validationDates = np.genfromtxt(validationcsv, delimiter=';', usecols=[0])

validationLabels = []



for label in validationDates:
	if label < 20010301:
		validationLabels.append('winter')
	elif 20010301 <= label < 20010601:
		validationLabels.append('lente')
	elif 20010601 <= label < 20010901:
		validationLabels.append('zomer')
	elif 20010901 <= label < 20011201:
		validationLabels.append('herfst')
	else: # from 01􀀀12 to end of year
		validationLabels.append('winter')



knn = KNearestNeighbours(datasetcsv, 1)





for k in range(120):
	
	result = knn.Run(validationSet)
	correct = 0
	for idx, x in enumerate(validationLabels):
		if x == result[idx]:
			correct +=1
	
	print(k,' - ',correct , ' / ', len(validationLabels), '|', correct,'%')
	knn.k = k
	
	
'''
Beste K: 34 met 29% correct percentage.

'''