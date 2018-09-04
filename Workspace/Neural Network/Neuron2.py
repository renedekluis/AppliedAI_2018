import math
import random as r




class NeuralNetwork:
	LEARNING_RATE = 0.1

	def __init__(self, numInputs, numHidden, numOutputs):
		self.numInputs = numInputs
		self.numHidden = numHidden
		self.numOutputs = numOutputs
		
		self.hiddenLayer = NeuronLayer(numHidden)
		self.outputLayer = NeuronLayer(numOutputs)
	
		self.InitHiddenLayerWeights()
		self.InitOutputLayerWeights()
	
	
	def InitHiddenLayerWeights(self):
		for hiddenIdx, hidden in enumerate(self.hiddenLayer.neurons):
			for inputIdx in range(self.numInputs):
				self.hiddenLayer.neurons[hiddenIdx].weights.append(r.uniform(-1,1))
	
	
	def InitOutputLayerWeights(self):
		for outIdx, Output in enumerate(self.outputLayer.neurons):
			for hiddenIdx, hidden in enumerate(self.hiddenLayer.neurons):
				self.outputLayer.neurons[outIdx].weights.append(r.uniform(-1,1))
	
	
	def Inspect(self):
		print('------')
		print('* Inputs: {}'.format(self.numInputs))
		print('------')
		print('Hidden Layer')
		self.hiddenLayer.Inspect()
		print('------')
		print('* Output Layer')
		self.outputLayer.Inspect()
		print('------')
	
	
	def feed_forward(self, inputs):
		hiddenLayer_outputs = self.hiddenLayer.feed_forward(inputs)
		return self.outputLayer.feed_forward(hiddenLayer_outputs)

	def train(self, trainInputs, trainOutputs):
		self.feed_forward(trainInputs)
		
		outputNeuronDeltas = [0]*len(self.outputLayer.neurons)
		for outIdx, output in enumerate(self.outputLayer.neurons):
			# ∂E/∂zⱼ
			neuron = self.outputLayer.neurons[outIdx]
			outputNeuronDeltas[outIdx] = neuron.GetInputError(trainOutputs[outIdx])
		
		hiddenNeuronDeltas = [0]*len(self.hiddenLayer.neurons)
		for hidIdx, hidden in enumerate(self.hiddenLayer.neurons):
			# dE/dyⱼ = Σ ∂E/∂zⱼ * ∂z/∂yⱼ = Σ ∂E/∂zⱼ * wᵢⱼ
			error = 0
			for outIdx, output in enumerate(self.outputLayer.neurons):
				weight1 = outputNeuronDeltas[outIdx]
				weight2 = self.outputLayer.neurons[outIdx].weights[hidIdx]
				error += weight1*weight2
				
			neuron = self.hiddenLayer.neurons[hidIdx]
			hiddenNeuronDeltas[hidIdx]=error*neuron.GetDeltaTotalInput()
	
	
		for outIdx, output in enumerate(self.outputLayer.neurons):
			neuron = self.outputLayer.neurons[outIdx]
			for wIdx, weight in enumerate(neuron.weights):
				# ∂Eⱼ/∂wᵢⱼ = ∂E/∂zⱼ * ∂zⱼ/∂wᵢⱼ
				error = outputNeuronDeltas[outIdx] * neuron.GetInput(wIdx)

				# Δw = α * ∂Eⱼ/∂wᵢ
				neuron.weights[wIdx] -= self.LEARNING_RATE * error

		for hidIdx, hidden in enumerate(self.hiddenLayer.neurons):
			neuron = self.hiddenLayer.neurons[outIdx]
			for wIdx, weight in enumerate(neuron.weights):
				# ∂Eⱼ/∂wᵢ = ∂E/∂zⱼ * ∂zⱼ/∂wᵢ
				error = hiddenNeuronDeltas[hidIdx] * neuron.GetInput(wIdx)

				# Δw = α * ∂Eⱼ/∂wᵢ
				neuron.weights[wIdx] -= self.LEARNING_RATE * error

	def calculateTotalError(self, trainingSets):
		totalError = 0
		for tIdx, train in enumerate(trainingSets):
			trainInputs, trainOutputs = trainingSets[tIdx]
			self.feed_forward(trainInputs)
			for outIdx, output in enumerate(trainOutputs):
				neuron = self.outputLayer.neurons[outIdx]
				totalError += neuron.GetError(trainOutputs[outIdx])
		return totalError
	
	
	
		
class NeuronLayer:
	def __init__(self, numNeurons, bias=r.uniform(-1,1)):
		self.bias = bias
		self.neurons = []
		for i in range(numNeurons):
			self.neurons.append(Neuron(self.bias))
			
		
	def Inspect(self):
		print('Neurons:',len(self.neurons))
		for nIdx, neuron in enumerate(self.neurons):
			print(' Neuron', nIdx)
			for wIdx, weight in enumerate(self.neurons[nIdx].weights):
				print('  Weight:', self.neurons[nIdx].weights[wIdx])
			print('  Bias:', self.bias)

	def feed_forward(self, inputs):
		outputs = []
		for neuron in self.neurons:
			outputs.append(neuron.GetOutput(inputs))
		return outputs

	def get_outputs(self):
		outputs = []
		for neuron in self.neurons:
			outputs.append(neuron.output)
		return outputs



		
class Neuron:
	def __init__(self, bias=r.uniform(-1,1)):
		self.bias = bias
		self.weights = []
		
	def GetOutput(self, inputs):
		self.inputs = inputs
		self.output = self.Sigmoid(self.GetTotalInput())
		return self.output
	
	
	def GetTotalInput(self):
		total = 0
		for idx, input in enumerate(self.inputs):
			total += self.inputs[idx]*self.weights[idx]
		return total + self.bias
	
	def Sigmoid(self, activation):
		return 1/(1+math.exp(-activation))
		
		
	def GetInputError(self, targetOutput):
		return self.GetDeltaOutputError(targetOutput)*self.GetDeltaTotalInput()
		
	def GetError(self, targetOutput):
		return 0.5 * (targetOutput - self.output)**2
		
	def GetDeltaOutputError(self, targetOutput):
		return -(targetOutput - self.output)
		
	def GetDeltaTotalInput(self):
		return self.output * (1-self.output)
		
		
	def GetInput(self, idx):
		return self.inputs[idx]