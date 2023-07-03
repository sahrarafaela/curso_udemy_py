## formatando com format
    # -> tudo em python é um objeto
a = 'A';
b = 'B';
c = 1.1;

formato = 'a = {}, b = {}, c = {:.2f}'.format(a, b, c);
print(formato);

trocando_ordem = 'a = {0} a = {0} a = {0}, b = {1}, c = {2:.2f}';
formatando = trocando_ordem.format(a, b, c);
print(formatando);