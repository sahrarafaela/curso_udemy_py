## precedencia no python

conta_um = 1 + 1 ** 5 + 5;
print(conta_um);
## para dar dois
conta_dois = (1+1) ** (5 + 5);
print(conta_dois);

## adento -> trocando valor da variável
conta_dois = 1 ** 5;
print(conta_dois);

conta_tres = (1 + int(0.5 + 0.5)) ** (5 + 5);
print(conta_tres);
##ordem 
"""
1 - parenteses
2 - **
3 - *, /, //, %
4 - +, -
"""