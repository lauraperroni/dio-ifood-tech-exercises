def calculaRank(vitorias, derrotas) :

    saldoVitorias = vitorias-derrotas
    if saldoVitorias <=10 :
        rank = 'Ferro'
    elif saldoVitorias >=11 and saldoVitorias <=20 :
        rank = 'Bronze'
    elif saldoVitorias >=11 and saldoVitorias <=50 :
        rank = 'Prata'
    elif saldoVitorias >=51 and saldoVitorias <=80 :
        rank = 'Ouro'
    elif saldoVitorias >=81 and saldoVitorias <=90 :
        rank = 'Diamante'
    elif saldoVitorias >=91 and saldoVitorias <=100 :
        rank = 'Lendário'
    elif saldoVitorias >=101 :
        rank = 'Imortal'    
    
    print(f'O herói tem saldo de {saldoVitorias} e está no nível {rank}')


vitorias = int(input('Entre a quantidade de vitórias do herói: '))
derrotas = int(input('Entre a quantidade de derrotas do herói: '))

calculaRank(vitorias, derrotas)