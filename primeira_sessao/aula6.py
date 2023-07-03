# conversão de tipos: coerção


"""
converter um tipo primitivo em outro tipo
exemplo:
"""
print (int('1') + 12); ## converteu o número em número inteiro
print (float('1') + 12); ## converteu o número em número float
print (type(float('1') + 12)); # confirmando o tipo de dado
print (bool(' ')); ## converteu o número em número boolean
## uma curiosidade!! na função acima (bool) se tirar o espaço entre as aspas o resultado que vai ser retornado é False
print(str('11')+'b'); ## transformar em string