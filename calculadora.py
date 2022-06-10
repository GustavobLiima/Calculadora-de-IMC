import time


nome = str(input('Digite seu nome:\t'))
idade = int(input('Digite sua idade:\t'))
altura = int(input('Digite sua altura(cm):\t'))
peso = float(input('Digite seu peso:\t'))
print('Analisando seus dados...')
time.sleep(3)
print('Calculando IMC')
time.sleep(3)
alt = altura / 100
imc = peso / (alt*alt)
print('{:.2f}'.format(imc))
time.sleep(5)
