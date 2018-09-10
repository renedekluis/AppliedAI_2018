
class Or:
	def __init__(self):
		self.weights = [0.5,0.5]
		self.threshold = 0.5
		
	def Run(self, inputs):
		result = 0
		for idx, weight in enumerate(self.weights):
			result += inputs[idx] * self.weights[idx]
			
		result = 1 if result >= self.threshold else 0
		return result
		
	def __str__(self):
		return 'Or'

class Nor:
	def __init__(self):
		self.weights = [-0.5,-0.5]
		self.threshold = 0
		
	def Run(self, inputs):
		result = 0
		for idx, weight in enumerate(self.weights):
			result += inputs[idx] * self.weights[idx]
			
		result = 1 if result >= self.threshold else 0
		return result
		
	def __str__(self):
		return 'Nor'
		
		
class And:
	def __init__(self):
		self.weights = [0.5,0.5]
		self.threshold = 1
		
	def Run(self, inputs):
		result = 0
		for idx, weight in enumerate(self.weights):
			result += inputs[idx] * self.weights[idx]
			
		result = 1 if result >= self.threshold else 0
		return result
		
	def __str__(self):
		return 'And'
		
		
class Nand:
	def __init__(self):
		self.weights = [-0.5,-0.5]
		self.threshold = -0.5
		
	def Run(self, inputs):
		result = 0
		for idx, weight in enumerate(self.weights):
			result += inputs[idx] * self.weights[idx]
			
		result = 1 if result >= self.threshold else 0
		return result
		
	def __str__(self):
		return 'Nand'
		
		
		
		
class Xor:
	def __init__(self):
		self.AND = And()
		self.OR = Or()
		self.Nand = Nand()
		
	def Run(self, inputs):
		orResult = self.OR.Run(inputs)
		nandResult = self.Nand.Run(inputs)
		return self.AND.Run([orResult,nandResult])
		
	def __str__(self):
		return 'Xor'











