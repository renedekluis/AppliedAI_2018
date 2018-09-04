from Neuron import *

class Adder:
	def __init__(self):
		OR = Neuron(0.5)
		OR.AddMultipleInputs([0.5, 0.5])
		
		
		self.S = 0
		self.Cout = 0
		self.halfAdder = HalfAdder()
		self.OR = OR
		
	def GetCout(self):
		return self.Carry
		
	def GetS(self):
		return self.S
		
	def Set(self, A, B, Cin):
		sc1 = self.halfAdder.Set(A,B)
		sc2 = self.halfAdder.Set(sc1['S'],Cin)
		
		self.Cout = self.OR.Run([sc1['Carry'],sc2['Carry']])
		self.S = sc2['S']
		
		return {'S':self.S, 'Cout':self.Cout}
		
		
class HalfAdder:
	def __init__(self):
		self.NAND = Neuron(-0.5)
		self.NAND.AddMultipleInputs([-0.5, -0.5])
		
		self.AND = Neuron(1)
		self.AND.AddMultipleInputs([0.5, 0.5])
		
		self.OR = Neuron(0.5)
		self.OR.AddMultipleInputs([0.5, 0.5])
		
		self.XOR = Neuron(1)
		self.XOR.AddMultipleInputs([0.5, 0.5])
		self.XOR.AddHiddenNeurons([self.NAND,self.OR])

		self.S = 0
		self.Carry = 0
		
	def Set(self, A, B):
		self.S = self.XOR.Run([A,B])
		self.Carry = self.AND.Run([A,B])
		return {'S':self.S, 'Carry':self.Carry}