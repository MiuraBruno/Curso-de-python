while True:
    try:
        linha = input().split()
        print('ola como voce esta %s, seu id e %s' %(linha[0],linha[1]))    
    except EOFError:
        print('_'*40)
        print('fim do arquivo lido')
        break