import datetime
import pandas as pd

class Verify:

     def __init__(self):
        pass
     def verifica_textos1(self,resposta):
        self.resposta = resposta
        quest = ['a','b','c']
        if resposta not in quest:
            print('Digite uma opção válida')
            return questionText1
        else:
            return resposta

data = {
    'city':[],
    'state':[],
    'ages':[],
    'genres':[],
    'answers1':[],
    'answers2':[],
    'answers3':[],
    'answers4':[],
    'dateAnswer':[],
}

# colunas = dados acima
# perguntas = 'answer': [a ou b ou c]


def perguntas():
    
    state = input('\nEm qual estado você mora ? ')
    city = input('\nQual a sua cidade ?  ')
    age = int(input('\nQual a sua idade ? ')) 
    if age < 1:
        print('Por favor, digite um valor válido para a idade.')
        perguntas()
    else:
        data['state'].append(state)
        data['city'].append(city)
        data['ages'].append(age)
        perguntas2()

def perguntas2():
    genre = input('\nQual o seu gênero [M/F] ? ')
    if genre == 'M'.lower() or 'F'.lower():
        data['genres'].append(genre)
        perguntas3()
    else:
        print("Digite apenas os caracteres correspondentes!")
        perguntas2()

def perguntas3():
    questionText1 = str(input('\nVocê já concluiu o Ensino Médio ?\na) Sim\nb) Não\nc)Não Sei\n Digite a opção correspondente:  '))
    questionText2 = str(input('\nA média salarial da sua residência ultrapassa os R$ 2.000 mensais ?\na) Sim\nb) Não\nc)Não Sei\n Digite a opção correspondente: '))
    questionText3 = str(input('\nDurante o perído da pandemia, você notou se alguma pessoa próxima desenvolver\n ou agravar a depressão ou alguma doença semelhante ?\na) Sim\nb) Não\nc)Não Sei\n Digite a opção correspondente:  '))
    questionText4 = str(input('\nVocê consideraria buscar apoio psicológico para ajudar essa ou essas pessoas ?\na) Sim\nb) Não\nc)Não Sei\n Digite a opção correspondente:  '))
    # question1 retorna apenas a letra da resposta
    question1 = Verify.verifica_textos(questionText1)
    verfalse(questionText1)
    question2 = Verify.verifica_textos(questionText2)
    verfalse(questionText2)
    question3 = Verify.verifica_textos(questionText3)
    verfalse(questionText3)
    question4 = Verify.verifica_textos(questionText4)
    verfalse(questionText4)


    data['answers1'].append(question1)
    data['answers2'].append(question2)
    data['answers3'].append(question3)
    data['answers4'].append(question4)
    data['dateAnswer'].append(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
    print('\nO Instituto agradece a participção de todos!')

def verfalse(question):
    if question == False:
        return question

#armazena o número de entrevistados (opcional)
numberAnswers = len(data['ages'])   

perguntas()



#Bloco para salvar csv
sheet = pd.DataFrame.from_dict(data,orient='index')
print(sheet)
# sheet.to_csv(sheet, encoding = 'utf-8')



#print(data,numberAnswers)

#O QUE FALTA:
#orientação à objetos