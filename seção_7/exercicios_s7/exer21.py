conjA = {'',}
conjB = {'',}


for x in range(0, 5):
    conjA.add( int(input('Digite um numero: ')))

for i in range(0, 5):
    conjB.add(int(input('Digite um numero: ')))

conjC = conjA.difference(conjB)

print(conjC)
