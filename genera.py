def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield(3)
	print('step 3')
	yield(5)

def fib(max):
	n,a,b =0,0,1
	while  n<max:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'
