from datetime import datetime
import csv
from os import system
import sys

class Pessoa():
    
    def __init__(self, idade ,genero, estado, cidade):
        self.idade = idade
        self.genero = genero
        self.estado = estado
        self.cidade = cidade 

        if self.genero == 1:
            self.genero = 'Feminino'
        elif self.genero == 2:
            self.genero = 'Masculino'
        elif self.genero == 3:
            self.genero = 'Outro'

        self.dados = {'idade':self.idade, 'genero':self.genero, 'estado':self.estado, 'cidade':self.cidade}
    
class Pergunta():
    def __init__(self,pergunta1,pergunta2,pergunta3,pergunta4):
        self.pergunta = [pergunta1,pergunta2,pergunta3,pergunta4]
        self.resposta = {}
        self.temp = {}
        x = 0
        self.data = datetime.now().strftime('%Y-%m-%d%H:%M')
        
        for pergunta in self.pergunta:
            pergunta = pergunta
            
            if pergunta == 1:
                    pergunta = ('Sim')
            if pergunta == 2:
                    pergunta = ('Nao')
            if pergunta == 3:
                    pergunta  = ('Talvez')

                   
            x += 1
                
            self.temp[f'pergunta{x}'] = pergunta
            self.resposta.update(self.temp.copy())
        self.resposta['data']= self.data
        
        print(self.resposta)


lista_entrevistados = []
loop = True
while loop:
    
    system('cls')

    print ('Insira corretamente os dados do enntrevistado, caso queira encerrar o programa digite "00" ao pedir a idade novamente.\n')
    
    entrevistado_idade  = int(input('Digite a idade da pessoa entrevistada: '))
    if entrevistado_idade == 00:
        loop = False
   
    else:
        
        entrevistado_genero = int(input('Digite o genero da pessoa entrevistada: '))
        while entrevistado_genero != 1 and entrevistado_genero != 2 and entrevistado_genero != 3:
            entrevistado_genero = int(input('Digite o genero da pessoa entrevistada: '))

        entrevistado_estado = (input('Digite o estado da pessoa entrevistada: '))
        entrevistado_cidade = (input('Digite a cidade da pessoa entrevistada: '))
        entrevistado = Pessoa(entrevistado_idade,entrevistado_genero,entrevistado_estado,entrevistado_cidade)
        
        print(entrevistado.dados)



        system('cls')

        pergunta_1 = int(input('Pergunta 1:  ' ))
        while pergunta_1!= 1 and pergunta_1 != 2 and pergunta_1!= 3:
            pergunta_1 = int(input('Digite uma opção válida: '))
        
        pergunta_2 = int(input('Pergunta 2:   ' ))
        while pergunta_2!= 1 and pergunta_2 != 2 and pergunta_2!= 3:
            pergunta_2 = int(input('Digite uma opção válida: '))

        pergunta_3 = int(input('Pergunta 3:   ' ))
        while pergunta_3!= 1 and pergunta_3 != 2 and pergunta_3 != 3:
            pergunta_3 = int(input('Digite uma opção válida: '))
        
        pergunta_4 = int(input('Pergunta 4:    ' ))
        while pergunta_4!= 1 and pergunta_4 != 2 and pergunta_4!= 3:
            pergunta_4 = int(input('Digite uma opção válida: '))
        
        pergunta = Pergunta(pergunta_1,pergunta_2,pergunta_3,pergunta_4)



        entrevistado.dados.update(pergunta.resposta)
        field_names = ['idade','genero','estado', 'cidade','pergunta1', 'pergunta2', 'pergunta3', 'pergunta4','data']
        lista_entrevistados.append(entrevistado.dados)


        with open ('Test.csv', 'w', newline = '' ) as csvfile:
            escritor = csv.DictWriter(csvfile, fieldnames = field_names)

            escritor.writeheader()
            escritor.writerows(lista_entrevistados)
        
        
        print(entrevistado.dados)
