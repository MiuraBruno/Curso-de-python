#calcular média dos alunos e dizer se tá aprovado ou nõa
#obs.: média é 7.0 aprovado
#media entre 7 e 5 exame
#media abaixo de 5 reprovado
#input são 3 notas com peso
#p1 = 2
#p2 = 3
#p3 = 5
#lendo notas
p1 = float(input('primeira nota:'))
p2 = float(input('segunda nota'))
p3 = float(input('terceira nota'))
#calcular médias
media = (2 * p1 + 3 * p2 + 5 * p3) /10.0
if media >= 7.0 :
    print('aprovado com nota %.2f' %(media))
elif media < 7.0 and media >= 5.0:
    print('exame com nota %.2f' %(media))
else:
    print('reprovado com nota %.2f' %(media))
#print('%.2f' %(6.66666666))