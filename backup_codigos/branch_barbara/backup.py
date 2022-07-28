import pandas as pd
from datetime import datetime, date
from function import input_number

input_init = input_number('Bem-vindo(a) ao questionário de saúde mental. \n\nDeseja iniciar o questionário? \n\n1 - Sim \n2 - Não \n\nDigite aqui: ')

class OpeningQuestion:
    def __init__(self, age, genre):
        self.age = age
        self.genre = genre
   
class ComplementaryQuestions:
    def __init__(self, schooling, average_wage, illness, assist):
        self.schooling = schooling
        self.average_wage = average_wage
        self.illness = illness
        self.assist = assist

df_columns = {
    'age': [],
    'genre': [],
    'schooling': [], 
    'average_wage': [], 
    'illness': [], 
    'assist': [],
    'date': [],
    'hour': []
}

def Question():   

    age = input_number('\nInforme sua idade em números: ')
    
    if age == 0:
        print('\nIdade 0 informada. Encerrando o questionário.')
        df = pd.DataFrame(df_columns)
        df.to_csv(f"questionario_{date.today()}.csv",index=False)
        exit()

    genre = input_number('\nInforme seu gênero. \n\n1 - Cisgênero \n2 - Transgênero \n3 - Não-binário \n\nDigite aqui: ')
    genre_dict = {1:'Cisgênero', 2:'Transgênero', 3: 'Não-binário'}
    question_genre = genre_dict[genre]
    
    schooling = input_number(f'\nVocê concluiu o ensino médio? \n\n1 - Sim \n2 - Não \n3 - Não sei \n\nDigite aqui: ')
    schooling_dict = {1:'Sim', 2:'Não', 3: 'Não sei'}
    schooling_action = schooling_dict[schooling]
    
    average_wage = input_number(f'\nSua média salarial ultrapassa 2 salários mínimos? \n\n1 - Sim \n2 - Não \n3 - Não sei \n\nDigite aqui: ')
    average_wage_dict = {1:'Sim', 2:'Não', 3: 'Não sei'}
    average_wage_action = average_wage_dict[average_wage]
    
    illness = input_number(f'\nDurante o período de pandemia, você ou alguém próximo, sofreu com alguma doença psicológica, agravada pelo isolamento social? \n\n1 - Sim \n2 - Não \n3 - Não sei \n\nDigite aqui: ')
    illness_dict = {1:'Sim', 2:'Não', 3: 'Não sei'}
    illness_action = illness_dict[illness]
    
    assist = input_number(f'\nVocê consideraria procurar uma rede de apoio como forma de auxilio? \n\n1 - Sim \n2 - Não \n3 - Não sei \n\nDigite aqui: ')
    assist_dict = {1:'Sim', 2:'Não', 3: 'Não sei'}
    assist_action = assist_dict[assist]

    dt_date_now = datetime.now()
    dt_date = dt_date_now.strftime("%d/%m/%Y")
    dt_time = dt_date_now.strftime("%H:%M:%S")
    
    df_columns['age'].append(age)
    df_columns['genre'].append(question_genre)
    df_columns['schooling'].append(schooling_action)
    df_columns['average_wage'].append(average_wage_action)
    df_columns['illness'].append(illness_action)
    df_columns['assist'].append(assist_action)
    df_columns['date'].append(dt_date)
    df_columns['hour'].append(dt_time)

    Question()
    
if input_init == 1:
    Question()
        
elif input_init == 2:
    print('\nQuestionário encerrado.')
    exit()

else:
    print('\nEntrada inválida. Questionário encerrado.')
    exit()