from neuralNetwork import *


xorTrain = [\
	[[0,0],[0]],\
	[[1,0],[1]],\
	[[0,1],[1]],\
	[[1,1],[0]]\
]

orTrain = [\
	[[0,0],[0]],\
	[[1,0],[1]],\
	[[0,1],[1]],\
	[[1,1],[1]]\
]

andTrain = [\
	[[0,0],[0]],\
	[[1,0],[0]],\
	[[0,1],[0]],\
	[[1,1],[1]]\
]

nandTrain = [\
	[[0,0],[1]],\
	[[1,0],[1]],\
	[[0,1],[1]],\
	[[1,1],[0]]\
]


twoInputOptions = [\
	[0,0],\
	[1,0],\
	[0,1],\
	[1,1]\
]
#print(twoInputOptions)


threeInputOptions = [\
	[0,0,0],\
	[0,0,1],\
	[0,1,0],\
	[0,1,1],\
	[1,0,0],\
	[1,0,1],\
	[1,1,0],\
	[1,1,1]\
]



xorNetwork = NeuralNetwork('XOR-GATE', 2, 1, 0.1)
orNetwork = NeuralNetwork('OR-GATE', 2, 1, 0.1)
andNetwork = NeuralNetwork('AND-GATE', 2, 1, 0.1)
nandNetwork = NeuralNetwork('NAND-GATE', 2, 1, 0.1)

xorNetwork.AddHiddenLayer(2)

#xorNetwork.Show()



def testXor(ammount):
	#xorNetwork.Show()
	for i in range(ammount):
		for trainIdx, train in enumerate(xorTrain):
			input = xorTrain[trainIdx][0]
			output = xorTrain[trainIdx][1]
			xorNetwork.Update(input,output)
			
	print('\n'*5,'===================\n',xorNetwork)
	for option in xorTrain:
		out = xorNetwork.Run(option[0])
		print(option[0],'|',end='')
		for i in out:
			print(' {:10.4f}'.format(i),end='')
		print()

	xorNetwork.Show()
		
		
def testOr(ammount):		

	for i in range(ammount):
		for trainIdx, train in enumerate(orTrain):
			
			input = orTrain[trainIdx][0]
			output = orTrain[trainIdx][1]
			orNetwork.Update(input,output)

	print('\n'*5,'===================\n',orNetwork)
	for option in orTrain:
		out = orNetwork.Run(option[0])
		print(option[0],'|',end='')
		for i in out:
			print(' {:10.4f}'.format(i),end='')
		print()

	orNetwork.Show()

def testAnd(ammount):		

	for i in range(ammount):
		for trainIdx, train in enumerate(andTrain):
			
			input = andTrain[trainIdx][0]
			output = andTrain[trainIdx][1]
			if input == [0,0] and output == [0]:
				continue
			andNetwork.Update(input,output)

	print('\n'*5,'===================\n',andNetwork)
	for option in andTrain:
		out = andNetwork.Run(option[0])
		print(option[0],'|',end='')
		for i in out:
			print(' {:10.4f}'.format(i),end='')
		print()

	andNetwork.Show()

def testNand(ammount):
	nandNetwork.Show()	
	for i in range(ammount):
		for trainIdx, train in enumerate(nandTrain):
			input = nandTrain[trainIdx][0]
			output = nandTrain[trainIdx][1]
			nandNetwork.Update(input,output)


	print('\n'*5,'===================\n',nandNetwork)
	for option in nandTrain:
		out = nandNetwork.Run(option[0])
		print(option[0],'|',end='')
		for i in out:
			print(' {:10.4f}'.format(i),end='')
		print()

	nandNetwork.Show()	

#testAnd(500)
#testNand(500)	
#testOr(500)
testXor(500)





