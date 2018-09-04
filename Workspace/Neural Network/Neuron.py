import math
import random as r

def GApo(z):
	return (1 - math.tanh(math.tanh(z)))


class NeuralNetwork:
	def __init__(self, numHiddenList):
		self.numHiddenList = numHiddenList
		self.hiddenLayers = []
		self.leerRate = 0.1
		
		
		for idx, hiddenneurons in enumerate(numHiddenList):
			hiddens = HiddenLayer(self.leerRate, idx)
			for idx2, inputs in enumerate(hiddenneurons):
				hiddens.AddNeuron(inputs)
			self.hiddenLayers.append(hiddens)
			
	def Show(self):
		for hid in self.hiddenLayers:
			hid.Show()
			print('='*10)
			
	
	
	
	
class HiddenLayer:
	def __init__(self, leerRate, LayerNr):
		self.leerRate = leerRate
		self.neurons = []
		self.LayerNr = LayerNr
		
		
	def AddNeuron(self,numInputs):
		n = Neuron(numInputs,self.leerRate,len(self.neurons))
		self.neurons.append(n)

	def Show(self):
		print('Layer:',self.LayerNr)
		for neuron in self.neurons:
			neuron.Show()
		
		
class Neuron:
	def __init__(self, numInputs, leerRate, ID=0):
		self.weights = []
		self.ID = ID
		self.bias = r.random()
		self.leerRate = leerRate
		self.numInputs = numInputs
		
		for i in range(numInputs):
			self.weights.append(r.random())
			
			
			
	def Show(self):
		print(' Neuron:',self.ID)
		print('  Inputs: ',self.numInputs)
		print('  Weights:')
		for i in self.weights:
			print('   ',i)
			
			
	def Activate(self, inputs):
		total = 0
		for idx, input in enumerate(inputs):
			gewicht = self.weights[idx]
			total += input * gewicht
		return math.tanh(total)
		
	
	def Update(self,inputs,output):
		inputs.append(1)
		self.weights.append(self.bias)
		tempGewichten = []
		for idx, input in enumerate(inputs):
			huidigGewicht = self.weights[idx]
			
			Activatie = self.Activate(inputs)
			deltaRule = huidigGewicht+self.leerRate*input*(1-math.tanh(Activatie))*(output-Activatie)
			tempGewichten.append(deltaRule)
		self.weights = tempGewichten[:-1]
		self.bias = tempGewichten[-1]	
		
		
		
		
	def Run(self,inputs):
		if len(self.weights) < len(inputs):
			return 0
		else:
			inputs.append(1)
			self.weights.append(self.bias)
			
			result = self.Activate(inputs)
			self.weights = self.weights[:-1]
			return result
			
			
		
		
class NeuronOld:
	def __init__(self,ID=0):
		self.weights = []
		self.hidden = []
		self.bias = 0
		self.leerRate = 0.1
		self.ID = ID
		self.SetValues()
	
	def SetValues(self):
		self.weights = [r.uniform(-1,0),r.uniform(-1,0)]
		self.bias = r.uniform(0,1)
		#print(self.weights,self.bias)
		
		
	def Show(self):
		print(' Neuron:',self.ID)
		print('  Weights:')
		for i in self.weights:
			print('   ',i)
		
	''' 	
	def AddInput(self, weight=1):
		self.weights.append(weight)
	
	def AddMultipleInputs(self, weights=[]):
		for i in weights:
			self.weights.append(i)
	
	def SetThreshold(self, newThreshold):
		self.threshold = newThreshold
	
	def GetTotalInputs(self):
		return len(self.weights)
	''' 	
		
	def Activate(self, inputs):
		total = 0
		for idx, input in enumerate(inputs):
			gewicht = self.weights[idx]
			total += input * gewicht
		return math.tanh(total)

	
	
	def ChangeWeight(self, inputIdx, newWeight):
		self.weights[inputIdx] = newWeight
		
	def GetBias(self):
		return self.bias
	
	def Update(self, inputs, output):
		inputs.append(1)
		self.weights.append(self.bias)
		tempGewichten = []
		for idx, input in enumerate(inputs):
			huidigGewicht = self.weights[idx]
			
			Activatie = self.Activate(inputs)
			deltaRule = huidigGewicht+self.leerRate*input*(1-math.tanh(Activatie))*(output-Activatie)
			tempGewichten.append(deltaRule)
		self.weights = tempGewichten[:-1]
		self.bias = tempGewichten[-1]

	
	def AddHiddenNeurons(self, neurons):
		for neuron in neurons:
			self.hidden.append(neuron)
	
	def Run(self,inputs):
		if len(self.weights) < len(inputs):
			return 0
		else:
			inputs.append(1)
			self.weights.append(self.bias)
			
			if len(self.hidden) > 0:
				newInputs = []
				for idx, hiddenItem in enumerate(self.hidden):
					newInputs.append(hiddenItem.Run(inputs.copy()))
				inputs = newInputs
			result = self.Activate(inputs)
			self.weights = self.weights[:-1]
			return result
 
		
		