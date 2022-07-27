import datetime
import pandas as pd

if __name__ == '__main__':

    class Verify:

        def __init__(self):
            pass
        def verifica_textos(self,resposta):
            self.resposta = resposta
            quest = ['a','b','c']
            if self.resposta not in quest:
                print('Digite uma opção válida')
                return False
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
            NewQuest.perguntas3()
        else:
            print("Digite apenas os caracteres correspondentes!")
            perguntas2()

    def verfalse(question):
        quest = ['a','b','c']
        if question not in quest:
            print('Digite uma opção válida')
            return False   
        else:
            return question

    class NewQuest:
        def __init__(self):
            pass

        def perguntas3():
            questionText1 = str(input('\nVocê já concluiu o Ensino Médio ?\na) Sim\nb) Não\nc)Não Sei\n Digite a opção correspondente:  '))
            if verfalse(questionText1) == False:
                return print(questionText1)
            
            questionText2 = str(input('\nA média salarial da sua residência ultrapassa os R$ 2.000 mensais ?\na) Sim\nb) Não\nc)Não Sei\n Digite a opção correspondente: '))
            if verfalse(questionText2) == False:
                return print(questionText2)    

            questionText3 = str(input('\nDurante o perído da pandemia, você notou se alguma pessoa próxima desenvolver\n ou agravar a depressão ou alguma doença semelhante ?\na) Sim\nb) Não\nc)Não Sei\n Digite a opção correspondente:  '))
            if verfalse(questionText3) == False:
                return print(questionText3)      

            questionText4 = str(input('\nVocê consideraria buscar apoio psicológico para ajudar essa ou essas pessoas ?\na) Sim\nb) Não\nc)Não Sei\n Digite a opção correspondente:  '))
            if verfalse(questionText4) == False:
                return print(questionText4) 

            data['answers1'].append(questionText1)
            data['answers2'].append(questionText2)
            data['answers3'].append(questionText3)
            data['answers4'].append(questionText4)
            data['dateAnswer'].append(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
            again()


    def again():
            newdata = str(input('Deseja inserir novos dados [S/N]? '))
            if newdata == 'S'.upper():
                perguntas()
            elif newdata == 'N'.upper():
                print(data)        
                sheet = pd.DataFrame.from_dict(data)
                print(sheet)
                sheet.to_csv('pesquisa.csv')
                print('Mandado pra csv !!!!!')
                print('\nO Instituto agradece a participção de todos!')
            else:
                print('Digite uma opção válida!')
                return again()

    perguntas()