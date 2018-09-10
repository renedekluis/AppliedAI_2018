import math
import random as r


class Neuron:
	def __init__(self,name,numInputs,leerRate):
		self.name = name
		self.weights = []
		self.bias = r.random()
		self.leerRate = leerRate
		
		for i in range(numInputs):
			self.weights.append(r.random())
		
		
	def Show(self):
		print(self.name,':')
		for idx, weight in enumerate(self.weights):
			print('Weight input ',idx,'-',weight)
		
		
	def Activate(self,inputs):
		if len(inputs) < len(self.weights):
			return 0
		
		total = 0
		for idx, input in enumerate(inputs):
			total += float(self.weights[idx])*float(input)

		return math.tanh(total)

		
	def GetDericative(self,input):
		return 1-math.tanh(math.tanh(input))
		
		
	def Update(self,inputs,output):
		#print('NeuralNetwork: Class Neuron - Update()')
		if len(self.weights) < len(inputs):
			return 
		else:
			inputs.append(1)
			self.weights.append(self.bias)
			
			activation = self.Activate(inputs)
			y = output
			n = self.leerRate
			
			tempWeights = []
			for inputIdx, input in enumerate(inputs):
				aIn = input
				W = self.weights[inputIdx]
				dericative = self.GetDericative(input)
				newW = W + (n*input*dericative*(output-activation))
				
				
				
				#print(\
				#	"{:10.4f}".format(newW), '=', \
				#	"{:10.4f}".format(W), '+', n,'*',input,'*',\
				#	"{:10.4f}".format(dericative),\
				#	'*(',output,'-',\
				#	"{:10.4f}".format(activation),')')
						
				tempWeights.append(newW)
				
			self.weights = tempWeights[:-1]
			self.bias = tempWeights[-1]
			inputs.pop()
			#print('=====END=====')
		

	def Run(self,inputs):
		#print('NeuralNetwork: Class Neuron - Run()')
		result = 0
		if len(self.weights) == len(inputs):
			inputs.append(1) #Append Bias as input
			self.weights.append(self.bias) #Append weight of bias
			result = self.Activate(inputs)
			self.weights = self.weights[:-1] #Remove bias
			inputs.pop()
		#print('=====END=====')
		return result
		
		
	def __str__(self):
		return 'Neuron: '+self.name









class HiddenLayer:
	def __init__(self):
		pass
		
		
		
		
		
	def Run(self):
		pass
		
		
		
		
		
	def __str__():
		return 'HiddenLayer'+self.name




















