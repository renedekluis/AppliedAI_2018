from neuralNetwork import *


norTrain = [\
	[[0,0],1],\
	[[1,0],0],\
	[[0,1],0],\
	[[1,1],0]\
]


norNeuron = Neuron('norNeuron',2,0.1)


for i in range(500):
	for trainIdx, train in enumerate(norTrain):
		inputs = norTrain[trainIdx][0]
		output = norTrain[trainIdx][1]
		norNeuron.Update(inputs,output)


print('\n'*5,'===================\n',norNeuron)	
for option in norTrain:
	print(option[0],'|',end='')
	print(norNeuron.Run(option[0]))


