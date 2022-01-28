# coding: utf-8
from random import choice
import string
import pandas as pd
from datetime import date
import sys

tamanho = 19
valores = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
senha = ''
data_atual = date.today()

#gera os sete caracteres inicias
senha = '#cgu'
senha += choice(string.ascii_lowercase)
senha += choice(string.digits)
senha += choice(string.ascii_uppercase)

for i in range(tamanho-7):
    senha += choice(valores)

print(senha)

#entrada no nome de referência da senha
#referencia = input('Referência: ')
referencia = 'sem_referencia'

#cria data frame
if len(sys.argv) > 1:
    referencia = sys.argv[1]

df = pd.DataFrame([{'referencia' : referencia,
                    'senha'      : senha,
                    'data'       : data_atual}])

    

#copia para o clipboard
df['senha'].to_clipboard(index=False, header=False)
print('\nsenha copiada para a área de transferência!')
print('tamanho: ', len(senha))

#salva senhas em csv
caminho_arquivo = '/Users/andreluiz/Documents/docs_csv/gera_senha.csv'

df.to_csv(caminho_arquivo, sep='\t', mode='a', header=False, index=False)