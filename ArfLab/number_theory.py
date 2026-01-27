def primewith(n,t):

	bolenlern = list()
	for i in range(1,n+1):
		if n % i == 0:
			bolenlern.append(i)

	bolenlert = list()
	for k in range(1,t+1):
		if t % k == 0: 
			bolenlert.append(k)

	ortaklar = set(bolenlern) & set(bolenlert)

	if ortaklar:
		if max(ortaklar) == 1 :
			return True
	else:
		return False

def phi(n):
	aralarındaasalları = list()
	for i in range(0,n):
		if primewith(i,n) == True:
			aralarındaasalları.append(i)

	return len(aralarındaasalları)