## operações lógicas

#and

entrada = input('[E]ntrar [S]air ');

senha_digitada = input('Senha: ');

senha_permitida = '123456';

if entrada == 'E' and senha_digitada == senha_permitida:
        print('Entrar');
else:
        print('Sair');

# 0, 0.0, '', False: falso

print(True and True);