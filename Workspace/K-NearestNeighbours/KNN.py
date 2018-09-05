
import numpy as np



class KNearestNeighbours:
	def __init__(self, dataset, k):
		self.data = np.genfromtxt(dataset, delimiter=';',usecols=[1,2,3,4,5,6,7],converters={5:lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)})
		self.dates = np.genfromtxt(dataset,delimiter=';',usecols=[0])
		self.labels = []
		self.terms = ["FG","TG","TN","TX","SQ","DR","RH"]
		
		if k > len(self.data):
			self.k = len(self.data)
		else:
			self.k = k
		
		self.SetLabels()
		
	def SetLabels(self):
		for label in self.dates:
			if label < 20000301:
				self.labels.append('winter')
			elif 20000301 <= label < 20000601:
				self.labels.append('lente')
			elif 20000601 <= label < 20000901:
				self.labels.append('zomer')
			elif 20000901 <= label < 20001201:
				self.labels.append('herfst')
			else: # from 01􀀀12 to end of year
				self.labels.append('winter')
			
		
	
	def FindNearest(self, value):
		#print('\nFindNearest('+str(value)+')\n')
		
		tempData = self.data[:]
		
		afstanden = []
		for rowIdx, row in enumerate(self.data):
			afstand = 0
			for termIdx, term in enumerate(self.terms):
				afstand += np.abs(self.data[rowIdx][termIdx]-value)**2
				#print(self.dates[rowIdx],' : ',self.data[rowIdx][termIdx],' - ', value, ' = ',self.data[rowIdx][termIdx]-value, ' | ', afstand)
			afstanden.append(np.sqrt(afstand))
		
		indexes = []
		for idx in range(self.k):
			index = afstanden.index(min(afstanden))
			indexes.append(index)
			afstanden[index] = 999999

		return indexes
	
		
		
	def GetAverage(self,SeasonList):
		seasons = {'zomer':0,'winter':0,'herfst':0,'lente':0}
		
		for s in SeasonList:
			seasons[s] += 1
			
		key_max = max(seasons.keys(), key=(lambda k: seasons[k]))
		return key_max
	

	
	def Run(self, testData):
		result = []
		for rowIdx, array in enumerate(testData):
			#print('=====\n',array,'\n')
			for termIdx, term in enumerate(self.terms):
				nearest = self.FindNearest(testData[rowIdx][termIdx])
			
			nearestAsSeasons = []
			for n in nearest:
				nearestAsSeasons.append(self.labels[n])
				
			avarageSeason = self.GetAverage(nearestAsSeasons)
			#print(avarageSeason)
			result.append(avarageSeason)
		return result
		
	
	
	def __str__(self):
		return "Class: K-Nearest Neighbours"