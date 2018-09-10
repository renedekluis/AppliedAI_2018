
from logicGates import *


class Adder:
	'''
	Brief: 
		Class constructor
	'''
	def __init__(self):
		self.halfAdder = HalfAdder()
		self.OR = Or()
		
	'''
	Brief: 
		This function will run the half adder.
	
	PARAMETERS:
		inputs: List of inputs for the gate
	
	RETURN:
		List - [Sum, Carry Out]
		
	EXAMPLE:
		Run([0,1,1])
		>>> [0,1]
	'''
	def Run(self,inputs):
		if len(inputs)<3:
			return [0,0]
		SC1 = self.halfAdder.Run([inputs[0],inputs[1]])
		SC2 = self.halfAdder.Run([SC1[0],inputs[2]])
	
		Cout = self.OR.Run([SC1[1],SC2[1]])
		Sum = SC2[0]

		return [Sum,Cout]
	


	'''
	Brief: 
		This function will return the classname as string.
	
	RETURN:
		String - The class name
		
	EXAMPLE:
		HalfAdder
		>>>'Adder'
	'''	
	def __str__(self):
		return 'Adder'


		
		


class HalfAdder:
	'''
	Brief: 
		Class constructor
	'''
	def __init__(self):
		self.XOR = Xor()
		self.AND = And()
	
	
	'''
	Brief: 
		This function will run the half adder.
	
	PARAMETERS:
		inputs: List of inputs for the gate
	
	RETURN:
		List - [Sum, Carry Out]
		
	EXAMPLE:
		Run([0,1])
		>>> [1,0]
	'''
	def Run(self,inputs):
		return [self.XOR.Run(inputs),self.AND.Run(inputs)]
	

	'''
	Brief: 
		This function will return the classname as string.
	
	RETURN:
		String - The class name
		
	EXAMPLE:
		HalfAdder
		>>>'HalfAdder'
	'''
	def __str__(self):
		return 'HalfAdder'