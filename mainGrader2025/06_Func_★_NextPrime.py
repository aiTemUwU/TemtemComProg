def is_prime(n):
	if n <= 1:
		return False
	for k in range(2, int(n**0.5)+1):
		if n % k == 0:
			return False
	return True

def next_prime(N):
	N += 1
	while not is_prime(N):
		N += 1
	return N

def next_twin_prime(N):
	primeList = []
	isTwinPrime = False
	while not isTwinPrime:
		primeList.append(next_prime(N))
		primeList.append(next_prime(next_prime(N)))

		if primeList[1] - primeList[0] == 2:
			isTwinPrime = True
		else:
			primeList = []
			N = next_prime(N)

	return primeList[0], primeList[1]

exec(input().strip())