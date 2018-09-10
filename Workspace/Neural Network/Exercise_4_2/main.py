from adder import *


twoInputOptions = [\
	[0,0],\
	[1,0],\
	[0,1],\
	[1,1]\
]

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


halfAdder = HalfAdder()
adder = Adder()

for option in twoInputOptions:
	haResult = halfAdder.Run(option)
	print(HalfAdder,' - ', option, ' | SUM: ', haResult[0], ' Carry:', haResult[1])

for option in threeInputOptions:
	adderResult = adder.Run(option)
	print(adder,' - ', option, ' | SUM: ', adderResult[0], ' Carry:', adderResult[1])