

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