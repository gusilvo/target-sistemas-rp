existe_a = False
num_a = 0
string = str(input('Digite uma string: '))

for l in string:
    if l in 'AaÃãÁáÂâÀàÄä':
        existe_a = True
        num_a += 1

if existe_a:
    if num_a == 1:
        print(f'A letra "A" ocorre 1 vez na string')
    else:
        print(f'A letra "A" ocorre {num_a} vezes na string')
else:
    print('Não ocorre a letra "A" na string')
