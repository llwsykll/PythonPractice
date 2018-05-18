def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	print(sum)

def calcn(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	print(sum)