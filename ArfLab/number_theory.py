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

def phi_bforce(n):
	aralarındaasalları = list()
	for i in range(0,n):
		if primewith(i,n) == True:
			aralarındaasalları.append(i)

	return len(aralarındaasalları)

import math

GAMMA = 0.57721566490153286

def phi(n):
    """Basit bir phi fonksiyonu (unimath kütüphanene ekleyebilirsin)"""
    result = n
    p = 2
    temp_n = n
    while p * p <= temp_n:
        if temp_n % p == 0:
            while temp_n % p == 0:
                temp_n //= p
            result -= result // p
        p += 1
    if temp_n > 1:
        result -= result // temp_n
    return result

def esitsizlik_kontrol(n):
    phi_n = phi(n)
    print(f"n = {n} için phi(n) = {phi_n}")
    
    # 1. Eşitsizlik (n > 2 için)
    if n > 2:
        alt_sinir_1 = n / (math.exp(GAMMA) * math.log(math.log(n)) + (3 / math.log(math.log(n))))
        print(f"1. Alt Sınır: {alt_sinir_1:.4f} < {phi_n} -> {phi_n > alt_sinir_1}")

    # 2. Eşitsizlik (n > 0 için)
    alt_sinir_2 = math.sqrt(n / 2)
    print(f"2. Alt Sınır: {alt_sinir_2:.4f} <= {phi_n} -> {phi_n >= alt_sinir_2}")

    # 3. Eşitsizlik (n > 6 için)
    if n > 6:
        alt_sinir_3 = math.sqrt(n)
        print(f"3. Alt Sınır: {alt_sinir_3:.4f} <= {phi_n} -> {phi_n >= alt_sinir_3}")