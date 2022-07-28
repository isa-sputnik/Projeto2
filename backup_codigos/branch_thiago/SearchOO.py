import datetime
import pandas as pd

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

class Pesquisa:
    def __init__(self, estado, cidade):
        self.estado = estado
        self.cidade = cidade
        data['state'] = self.estado
        data['city'] = self.cidade

    def entrevistados (self, idade: int, genero):
        self.idade = idade
        self.genero = genero
        data['ages'].append(self.idade)
        data['genres'].append(self.genero)

    def fazerPergunta1(self, r1: int):
        self.r1 = r1
        if self.r1 != 1 and self.r1 != 2 and self.r1 != 3:
            data['answers1'].append(3)
        else:
            data['answers1'].append(self.r1) 

    def fazerPergunta2(self, r2: int):
        self.r2 = r2
        if self.r2 != 1 and self.r2 != 2 and self.r2 != 3:
            data['answers2'].append(3)
        else:
            data['answers2'].append(self.r2) 

    def fazerPergunta3(self, r3: int):
        self.r3 = r3
        if self.r3 != 1 and self.r3 != 2 and self.r3 != 3:
            data['answers3'].append(3)
        else:
            data['answers3'].append(self.r3) 

    def fazerPergunta4(self, r4: int):
        self.r4 = r4
        if self.r4 != 1 and self.r4 != 2 and self.r4 != 3:
            data['answers4'].append(3)
        else:
            data['answers4'].append(self.r4) 

    def registroDataHora(self):
        data['dateAnswer'].append(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))

    def exportCsv(self):
        #Bloco para salvar csv
        sheet = pd.DataFrame(data)
        sheet.to_csv('Pesquisa_'+data['state']+'-'+data['city']+'.csv', encoding = 'utf-8')
            

novaPesquisa = Pesquisa(input('\nDigite a sigla do estado onde esta pesquisa está sendo realizada e tecle enter... ').upper(), input('\nDigite a cidade onde esta pesquisa está sendo realizada e tecle enter... '))

insert = True
while insert:

    age = int(input('\nDigite a idade da pessoa entrevistada e tecle enter... '))
        
    if age > 0:
        
        novaPesquisa.entrevistados(age, input('\nDigite o gênero da pessoa entrevistada e tecle enter... ').lower())

        novaPesquisa.fazerPergunta1(input('\nEsta é a pergunta 1 \nSim(1)\nNão(2)\nNão sei responder(3)\n'))
        novaPesquisa.fazerPergunta2(input('\nEsta é a pergunta 2 \nSim(1)\nNão(2)\nNão sei responder(3)\n'))
        novaPesquisa.fazerPergunta3(input('\nEsta é a pergunta 3 \nSim(1)\nNão(2)\nNão sei responder(3)\n'))
        novaPesquisa.fazerPergunta4(input('\nEsta é a pergunta 4 \nSim(1)\nNão(2)\nNão sei responder(3)\n'))

        novaPesquisa.registroDataHora()

    elif age == 0:
        insert = False

    else:
        print('\nEntrada inválida!')

novaPesquisa.exportCsv()
print('\nObrigado pela participação')
