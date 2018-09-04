import math
from Neuron import *
from Adder import *

def GApo(z):
	return (1 - math.tanh(math.tanh(z)))

	
	
NOR = NeuronOld()
AND = NeuronOld()
OR = NeuronOld()
NAND = NeuronOld()

XOR = NeuronOld()

NORTrain = [
	[0,0,1],
	[1,0,0],
	[0,1,0],
	[1,1,0],
]

ANDTrain = [
	[0,0,0],
	[1,0,0],
	[0,1,0],
	[1,1,1],
]

ORTrain = [
	[0,0,0],
	[1,0,1],
	[0,1,1],
	[1,1,1],
]

NANDTrain = [
	[0,0,1],
	[1,0,1],
	[0,1,1],
	[1,1,0],
]



for i in range(1000):
	#current = NOR.GetBias()
	for idx, test in enumerate(NORTrain):
		NOR.Update([NORTrain[idx][0],NORTrain[idx][1]],NORTrain[idx][2])
		AND.Update([ANDTrain[idx][0],ANDTrain[idx][1]],ANDTrain[idx][2])
		OR.Update([ORTrain[idx][0],ORTrain[idx][1]],ORTrain[idx][2])
		NAND.Update([NANDTrain[idx][0],NANDTrain[idx][1]],NANDTrain[idx][2])
		

for idx, test in enumerate(NORTrain):
	print('NOR ',NORTrain[idx],NOR.Run([NORTrain[idx][0],NORTrain[idx][1]]))
	print('AND ',ANDTrain[idx],AND.Run([ANDTrain[idx][0],ANDTrain[idx][1]]))
	print('OR  ',ORTrain[idx],OR.Run([ORTrain[idx][0],ORTrain[idx][1]]))
	print('NAND',NANDTrain[idx],NAND.Run([NANDTrain[idx][0],NANDTrain[idx][1]]))
	print('====')

nn = NeuralNetwork([[2,2,2],[2,2,2,2,2],[2,2,2,2],[2,2]])
print(nn.Show())




