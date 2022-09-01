# Faça um programa que receba o sexo, peso e altura do usuário e em seguida apresente:
# IMC (Índice de massa corporal)
# Classificaçao do IMC.
# Use funções para fazer os cálculos e não esqueça de validar os inputs.


def imc(peso, altura):
    imc = peso / (altura * altura)
    return round(imc, 1)

def class_imc (sexo, peso, altura):
    valor_imc = imc(peso, altura)

    if sexo == 'f':
        if valor_imc < 19.1:
            return 'Abaixo do peso.'
        elif valor_imc >= 19.1 and valor_imc < 25.8:
            return 'No peso normal.'
        elif valor_imc >= 25.8 and valor_imc < 27.3:
            return 'Marginalmente acima do peso.'
        elif valor_imc >= 27.3 and valor_imc < 32.3:
            return 'Acima do peso ideal.'
        elif valor_imc >= 32.3:
            return 'Obeso'
        else:
            return 'Erro do cálculo. Entre em contato com o administrador.'

    if sexo == 'm':
        if valor_imc < 20.7:
            return 'Abaixo do peso.'
        elif valor_imc >= 20.7 and valor_imc < 26.4:
            return 'No peso normal.'
        elif valor_imc >= 26.4 and valor_imc < 27.8:
            return 'Marginalmente acima do peso.'
        elif valor_imc >= 27.8 and valor_imc < 31.1:
            return 'Acima do peso ideal.'
        elif valor_imc >= 31.1:
            return 'Obeso'
        else:
            return 'Erro do cálculo. Entre em contato com o administrador.'

print('Vamos calcular seu IMC?')

valid_sexo = False
while valid_sexo == False:
    sexo = input('Digite seu sexo: ').lower()
    if sexo != 'm' and sexo != 'f':
        print('Sexo inválido! Digite M ou F.')
    else:
        valid_sexo = True

valid_peso = False
while valid_peso == False:
    peso = input('Digite seu peso (ex.68.5): ')
    try:
        peso = float(peso)
        if peso <= 0 or peso > 350:
            print('Peso inválido.')
        else:
            valid_peso = True
    except:
        print('Peso inválido. Use apenas números e separe os decimais com ponto.')

valid_altura = False
while valid_altura == False:
    altura = input('Digite a altura em metros (ex: 1.75): ')
    try:
        altura = float(altura)
        if altura <= 0 or altura >3:
            print('Altura inválida.')
        else:
            valid_altura = True
            print('\n')
    except:
        print('Altura inválida. Use apenas números e separe os decimais com ponto.')

v_imc = imc(peso, altura)
c_imc = class_imc(sexo, peso, altura)

print('Seu IMC é:', v_imc)
print('A sua classificação é:', c_imc)
