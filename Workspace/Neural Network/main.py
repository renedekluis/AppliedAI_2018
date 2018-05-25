import math


def GetGApo(z):
	return (1 - math.tanh(math.tanh(z)))
	
	
print(GetGacc(1))