from nor import *


twoInputOptions = [[0,0],[1,0],[0,1],[1,1]]

NOR = Nor()
for option in twoInputOptions:
	print(option,NOR.Run(option))