import numpy as np
from math import *
#import matplotlib.pyplot as plt

class CKNN:
	def __init__(self, file, k):
		self.data 	= np.genfromtxt(file, delimiter=';', usecols=[1,2,3,4,5,6,7], converters={5: lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)})
		self.dates 	= np.genfromtxt(file, delimiter=';', usecols=[0])
		self.k = k
		self.terms = ["FG", "TG" , "TN" , "TX" , "SQ" , "DR" , "RH" ]
		self.testData = {}
		self.labels = []
		self.labels2 = {}
		self.distClust = {}

		for x, y in enumerate(self.terms):
			self.distClust[x] = []
		
		self.SetDateToSeason()
	
	#set the seasons of the original dataset
	def SetDateToSeason(self):	
		for datum in self.dates:
			if datum < 20000301:
				self.labels.append('winter')
				self.labels2.update({datum:'winter'})
			elif 20000301 <= datum < 20000601:
				self.labels.append('lente')
				self.labels2.update({datum:'lente'})
			elif 20000601 <= datum < 20000901:
				self.labels.append('zomer')
				self.labels2.update({datum:'zomer'})
			elif 20000901 <= datum < 20001201: 
				self.labels.append('herfst')
				self.labels2.update({datum:'herfst'})
			else: # from 01-12 to end of year 
				self.labels.append('winter')
				self.labels2.update({datum:'winter'})
		return self.labels
		
	#Get the season of 1 specific date
	def DateToSeason(self, date):
		seizoen = ""
		if date < 20000301:
			seizoen = 'winter'
		elif 20000301 <= date < 20000601:
			seizoen = 'lente'
		elif 20000601 <= date < 20000901:
			seizoen = 'zomer'
		elif 20000901 <= date < 20001201: 
			seizoen = 'herfst'
		else: # from 01-12 to end of year 
			seizoen = 'winter'
		return seizoen
		
	#Get the seasons of the validation set
	def dateToSeason2(self, dates):	
		labs = []
		for datum in dates:
			if datum < 20010301:
				labs.append('winter')
			elif 20010301 <= datum < 20010601:
				labs.append( 'lente')
			elif 20010601 <= datum < 20010901:
				labs.append( 'zomer')
			elif 20010901 <= datum < 20011201: 
				labs.append( 'herfst')
			else: # from 01-12 to end of year 
				labs.append( 'winter')
		return labs
		
		

	def setK(self,newK):
		self.k = newK
		
	def getK(self):
		return self.k
	
	#Set new test data if needed
	def SetTestData(self, data):
		self.testData = data

	#Convert the punts with the shortest distance to a season
	def ConvertToSeasons(self, data):
		result = {}
		for term in range(len(self.terms)):
			result[term] = []
			
			for punt in data[term]:
				puntSeizoen = []
				for k in range(self.k):
					seizoen = self.DateToSeason(punt[k][1])
					puntSeizoen.append(seizoen)
				
				meesteSeizoen = self.avrSeason(puntSeizoen)
				result[term].append(meesteSeizoen)
		#for x in result:
			#print(result[x])
		return result
	
	
	def FindNearest2(self):
		clusters = {}
		afstanden = []
		for rijIdx, rij in enumerate(self.data):
			afstand =0
			for rijIdx2, rij2 in enumerate(self.testData):
				afstand += np.abs(self.data[rijIdx]- self.testData[rijIdx2])**2
			afstand = np.sqrt(afstand)
			print(rijIdx,afstand)
				
		
		'''
		for datumIdx1, datum in enumerate(self.dates):
			season = self.labels2[datum]
			if season in clusters:
				clusters[season].append(data[datumIdx1])
			else:
				clusters[season] = []
		for season in list(clusters):
			#print(clusters[season])
			for rij in clusters[season]:
				print(rij)
		'''
	#Returns the k shortest distances to testpoint
	def FindNearest(self, value):
		afstanden = []
		for i, array in enumerate(self.data):
			dist = np.linalg.norm(value - array)
			date = self.dates[i]
			afstanden.append((dist, date))
			
		afstanden.sort(key = lambda t: t[0] )

		return afstanden[0:self.k]
		
		
	#Start the algoritm
	def Run(self):
		#self.FindNearest2()
		#return 'Einde'
		
		
		
		testDataAfstanden = {}
		
		for term in range(len(self.terms)):
			testDataAfstanden[term] = []
			
		for punt in self.testData:
			for termIdx, term in enumerate(self.terms):
				#print(term)
				afstanden = self.FindNearest(punt[termIdx])

				testDataAfstanden[termIdx].append(afstanden)
		
		
		
		result = self.ConvertToSeasons(testDataAfstanden)
		flippedResult = []

		for term in range(len(result[0])):
			flippedResult.append([result[j][term] for j in result])
		
		for i in range(len(flippedResult)):
			flippedResult[i] = self.avrSeason(flippedResult[i])

		return flippedResult

	
		
	#Returns the season that is refferenced most in the given array
	def avrSeason(self, array):
		a = {"winter":0,"lente":0,"zomer":0,"herft":0}
		
		for i in array:
			if i == "winter":
				a["winter"]+=1
			if i == "lente":
				a["lente"]+=1
			if i == "zomer":
				a["zomer"]+=1
			if i == "herft":
				a["herft"]+=1
		
		m = max([a["winter"],a["lente"],a["zomer"],a["herft"]])
		
		for i in a:
			if a[i] == m:
				return i
				
				

			
		
	