import math
import random as r
from inspect import *
import inspect


class Neuron:
	def __init__(self,name,numInputs, numOutputs, leerRate):
		self.name = name
		self.weights = []
		self.bias = r.random()
		self.leerRate = leerRate
		self.numOutputs = numOutputs
		
		self.saveWeights = []
		self.saveBias = 0
		
		self.value = 0
		
		for i in range(numInputs):
			self.weights.append(r.random())
		
		
	def AddInput(self):
		self.weights.append(r.random())
	
	
	def AddMultipleInputs(self, ammount):
		for i in range(ammount):
			self.weights.append(r.random())
	

	
	def Show(self):
		print('\t\tNeuron -',self.name,':')
		print('\t\t----------')
		print('\t\tInputs:     ',len(self.weights))
		print('\t\tOutputs:    ',self.numOutputs)
		for idx, weight in enumerate(self.weights):
			print('\t\t\tWeight input',idx,'-',weight)
		print('\t\t\tWeight Bias - ',self.bias)
		
		
	def Activate(self,inputs):
		if len(inputs) < len(self.weights):
			return 0
		
		total = 0
		for idx, input in enumerate(inputs):
			total += float(self.weights[idx])*float(input)
		result = math.tanh(total)
		return result

		
	def GetDericative(self,input):
		return 1-math.tanh(math.tanh(input))
		
		
	def Update(self,inputs,output):
		
		if len(self.weights) < len(inputs):
			print('Inputs not equal to neuron inputs')
			return 
		else:
			inputs.append(1)
			self.weights.append(self.bias)
			activation = self.Activate(inputs)
			y = output
			n = self.leerRate
			
			holdWeights = self.weights[:]
			
			tempWeights = []
			for inputIdx, input in enumerate(inputs):
				aIn = input
				W = self.weights[inputIdx]
				dericative = self.GetDericative((input*self.weights[inputIdx]))
				newW = W + (n*input*dericative*(output-activation))
				
				''' 
				print(\
					'Neuron',self.name,'Weight',inputIdx,\
					"{:10.4f}".format(newW), '=', \
					"{:10.4f}".format(W), '+', n,'*',input,'*',\
					"{:10.4f}".format(dericative),\
					'*(',output,'-',\
					"{:10.4f}".format(activation),')')
				#''' 	
				tempWeights.append(newW)
			
			self.saveWeights = tempWeights[:-1]
			self.saveBias = tempWeights[-1]
			self.weights = holdWeights[:-1]
			self.bias = holdWeights[-1]
			inputs.pop()
			
			return self.weights
		
	def ChangeWeights(self):
		self.weights = self.saveWeights
		self.bias = self.saveBias
		return self.weights
		

	def Run(self,input):
		result = 0
		if len(self.weights) == len(input):
			input.append(1) #Append Bias as input
			self.weights.append(self.bias) #Append weight of bias
			result = self.Activate(input)
			self.weights = self.weights[:-1] #Remove bias
			input.pop()
		self.value = result
		return result
		
		
	def __str__(self):
		return 'Neuron: '+self.name









class HiddenLayer:
	def __init__(self,layerId, numHiddenNeurons, numInputs, numOutputs, leerRate):
		self.numNeurons = numHiddenNeurons
		self.layerId = layerId
		self.leerRate = leerRate
		
		self.hiddenNeurons =  []
		
		for idx in range(numHiddenNeurons):
			self.hiddenNeurons.append(Neuron(('h'+str(idx)),numInputs,numOutputs,leerRate))
			
		
	def UpdateInputs(self,numInputs):
		if numInputs > self.numNeurons:
			for neuron in self.hiddenNeurons:
				neuron.AddMultipleInputs(numInputs-self.numNeurons)
				
	
	def Update(self,input,output):
		result = []
		for neuron in self.hiddenNeurons:
			for out in output:
				#print(input,neuron.value)
				result.append(neuron.Update(input,neuron.value))
		
		return result
		
	def Show(self):
		print('\tHiddenLayer - ',self.layerId,':')
		print('\t','-'*15)
		print('\tnumNeurons:    ',self.numNeurons)
		for n in self.hiddenNeurons:
			n.Show()
		print('-'*15)
		
		
	def Run(self, input):
		result = []
		for neuron in self.hiddenNeurons:
			result.append(neuron.Run(input))
		return result
		
		
	def UpdateFinisher(self):
		for neuron in self.hiddenNeurons:
			neuron.ChangeWeights()

		
		
	def __str__(self):
		return 'HiddenLayer - '+self.layerId




class NeuralNetwork:
	def __init__(self,name, numInputs, numOutputs, leerRate):
		self.name = name
		self.numInputs = numInputs
		self.numOutputs = numOutputs
		self.leerRate = leerRate
		
		self.outputNeurons = []
		self.hiddenLayers = []
		
		
		for outputIdx in range(numOutputs):
			outputName = ('OutputNeuron'+str(outputIdx))
			self.outputNeurons.append(Neuron(outputName,numInputs,numOutputs,leerRate))
		
		
	def Show(self):
		print('='*16)
		print('NeuralNetwork - '+self.name,':')
		print('='*16)
		print('Inputs:      ', self.numInputs)
		print('Outputs:     ', self.numOutputs)
		print('HiddenLayers:', len(self.hiddenLayers))
		print('LeerRate:    ', self.leerRate)
		print('-'*16)
		for layer in self.hiddenLayers:
			layer.Show()
		for outputIdx, outputNeuron in enumerate(self.outputNeurons):
			outputNeuron.Show()
		print('\n'*3)
		print('='*8,'END','='*8,'\n'*5)
		
	
	def AddHiddenLayer(self,numNeurons):
		id = len(self.hiddenLayers)
		input = self.numInputs
		if not self.hiddenLayers:
			self.hiddenLayers.append(HiddenLayer(id,numNeurons,input,self.numOutputs, self.leerRate))
		else:
			self.hiddenLayers[-1].UpdateInputs(numNeurons)
			hiddenOutputs = self.hiddenLayers[-1].numNeurons
			self.hiddenLayers.append(HiddenLayer(id,numNeurons,input,hiddenOutputs, self.leerRate))

	
	def Update(self,input,output):
		if len(output) == len(self.outputNeurons):
			if not self.hiddenLayers:
				for outputIdx, outputNeuron in enumerate(self.outputNeurons):
					outputNeuron.Update(input,output[outputIdx])
				
				for outputIdx, outputNeuron in enumerate(self.outputNeurons):
					outputNeuron.ChangeWeights()
			else:	
				outputNeuronInput = input
				
				for layerIdx, layer in enumerate(self.hiddenLayers):
					outputNeuronInput = layer.Run(outputNeuronInput)
				
				
				for outputIdx, outputNeuron in enumerate(self.outputNeurons):
					outputNeuron.Update(outputNeuronInput,output[outputIdx])
				
				self.hiddenLayers[0].Update(input,output)
				
				if len(self.hiddenLayers) > 1:
					for i in range(1,len(self.hiddenLayers)):
						tempOutputs = []
						for outputs in self.hiddenLayers[i-1].hiddenNeurons:
							tempOutputs.append(outputs.value)
						self.hiddenLayers[i].Update(tempOutputs,output)
				
				for layerIdx, layer in enumerate(self.hiddenLayers):
					layer.UpdateFinisher()
					
				for outputIdx, outputNeuron in enumerate(self.outputNeurons):
					outputNeuron.ChangeWeights()
		else:
			print('Outputs not equal to network outputs')
				
			
	
	def Run(self,input):
		result = []
		if self.numInputs == len(input):
			if not self.hiddenLayers:
				for outputIdx, output in enumerate(self.outputNeurons):
					result.append(output.Run(input))
			else:
				tempResult = input
				for layer in self.hiddenLayers[::-1]:
					tempResult = layer.Run(tempResult)
					#print(tempResult)
				
				
				for outputIdx, output in enumerate(self.outputNeurons):
					out = output.Run(tempResult)
					result.append(out)
	
		return result
		
		
	def __str__(self):
		return 'NeuralNetwork - '+self.name
	





'''
Reminder voor volgende keer:


Het programma gaat fout bij de Run() functies.
Hierbij zit waarschijnlijk de fout bij de Run() van de klasse NeuralNetwork.


'''









