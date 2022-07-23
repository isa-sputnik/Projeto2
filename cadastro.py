import datetime
from sre_parse import State
from types import CoroutineType
import pandas as pd

# class Verify:

#     def __init__(self):
#         pass
#     def verifica_textos(self,resposta):
#         self.resposta = resposta
#         if resposta 
#         pass

'''
     #função que verifica a validade da resposta
    def verify ():
        a = int(input())
        while a != 1 and a != 2 and a != 3:
            print('\nResposta inválida! Insira uma resposta correta... ')
            a = int(input())
        else:
            return a
    '''

#bloco para inserir o texto das perguntas (opcional)
questionText1 = '\nPergunta 1'
questionText2 = '\nPergunta 2'
questionText3 = '\nPergunta 3'
questionText4 = '\nPergunta 4'

#dicionários que armazenam os dados
data = {
    'city':'',
    'state':'',
    'ages':[],
    'genres':[],
    'answers1':[],
    'answers2':[],
    'answers3':[],
    'answers4':[],
    'dateAnswer':[],
}


def perguntas():
    state = input('\nEm qual estado você mora ? ')
    city = input('\nQual a sua cidade ?  ')
    age = int(input('\nQual a sua idade ? ')) 
    if age < 1:
        print('Por favor, digite um valor válido para a idade.')
        perguntas()
    else:
        genre = input('\nQual o seu gênero [M/F] ? ')
        if genre != 'M'.lower() or 'F'.lower():
            print("Digite apenas os caracteres correspondentes!")
        print(questionText1)
        question1 = Verify.verifica(question1)
        print(questionText2)
        question2 = Verify.verifica(question2)
        print(questionText3)
        question3 = Verify.verifica(question3)
        print(questionText4)
        question4 = Verify.verifica(question4)

        data['state'].append(state)
        data['city'].append(city)
        data['ages'].append(age)
        data['genres'].append(genre)
        data['answers1'].append(question1)
        data['answers2'].append(question2)
        data['answers3'].append(question3)
        data['answers4'].append(question4)
        data['dateAnswer'].append(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))

#armazena o número de entrevistados (opcional)
numberAnswers = len(data['ages'])   

perguntas()

print('\nO Instituto agradece a participção de todos!')

#Bloco para salvar csv
sheet = pd.DataFrame.from_dict(data,orient='index')
print(sheet)
# sheet.to_csv(sheet, encoding = 'utf-8')



#print(data,numberAnswers)

#O QUE FALTA:
#orientação à objetos