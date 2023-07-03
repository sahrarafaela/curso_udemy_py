## formatação de strings f-strings

#usando código anterior (aula12)

##f string
nome = 'Sara';
idade = 24;
altura = 1.62;
peso = 60;

imc = peso / (altura * altura);

##ao invés disso ->
print(nome, 'tem', altura, 'de altura');
##usar assim formatado,  mais simple e usual
## o :.(numero)f é usado para limitar as casas decimais
linha_1 = f'{nome} tem {altura:.2f} de altura';
print(linha_1);

linha_2 = f'Pesa {peso} e tem {imc: .2f} de IMC';
print(linha_2);