'''
Nome: Clarissa Cruz
Data: 28/10/2027
Versão 1
'''
#Faça um programa que verifique (usando if e else) se uma letra digitada é 
# “F” ou “M”. Conforme a letra escrever: F – Feminino, M- Masculino, Sexo inválido. 

sexo = str (input('Digite a letra (F para Feminino ou M para Masculino): '))

if sexo == 'M' or sexo == 'm':
    print ('Seu sexo é masculino')
elif sexo == 'F'or sexo == 'f':
    print ('Seu sexo é feminino')
else:
    print ('Sexo Inválido')