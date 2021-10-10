print('----------'*10)
print('cadastre uma pessoa')
print('----------'*10)
mulheres=0
homens=0
dezoito=0

while True:
    idade=int((input('idade : ')))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('sexo : [M/F]')).strip() .upper()[0]
        if sexo == 'F' and idade < 20:
            mulheres += 1
        if idade == 18:
           dezoito += 1
        if sexo == 'M':
            homens+=1
    print('----------'*10)
    resp=' '
    while resp not in 'SN':
        resp=str(input('quer continuar ? [S/N] ? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'e temos {mulheres} mulheres com menos de 20 anos')
print(f'o total de pessoas com 18 anos foi de {dezoito}')
print(f'ao todo temos {homens} homens')



