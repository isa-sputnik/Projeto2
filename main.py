import pandas as pd
from datetime import datetime
from question import OpeningQuestion
from function import input_number, input_text, input_number_limit, separator

df_response = []
conditions = True

input_init = input_number('\nBem-vindo(a) ao questionário de saúde mental. \n\nDeseja iniciar o questionário? \n\n1 - Sim \n2 - Não \n\nDigite aqui: ')
while conditions:
    if input_init == 1:
        
        age = input_number('\nInforme sua idade em números (caso deseje encerrar a pesquisa, digite 0): ')

        if age == 0:
            print('\nIdade 0 informada. Encerrando o questionário.')
            
            dt_date_now = datetime.now()
            date = dt_date_now.strftime("%d_%m_%Y")
            hour = dt_date_now.strftime("%H_%M_%S")
            
            df = pd.DataFrame(df_response)
            df.to_csv(f"questionario_{date}_{hour}.csv",index=False)
            contitions = False
            exit()
        
        name = input_text('\nInforme seu nome: ')
        genre = input_number_limit('\nInforme seu gênero. \n\n1 - Cisgênero \n2 - Transgênero \n3 - Não-binário \n\nDigite aqui: ')        
        schooling = input_number_limit(f'\nVocê concluiu o ensino médio? \n\n1 - Sim \n2 - Não \n3 - Não Sei \n\nDigite aqui: ')
        average_wage = input_number_limit(f'\nSua média salarial ultrapassa 2 salários mínimos? \n\n1 - Sim \n2 - Não \n3 - Não Sei \n\nDigite aqui: ')
        illness = input_number_limit(f'\nDurante o período de pandemia, você ou alguém próximo, sofreu com alguma doença psicológica, agravada pelo isolamento social? \n\n1 - Sim \n2 - Não \n3 - Não Sei \n\nDigite aqui: ')
        assist = input_number_limit(f'\nVocê consideraria procurar uma rede de apoio como forma de auxilio? \n\n1 - Sim \n2 - Não \n3 - Não Sei \n\nDigite aqui: ')
        
        genre_dict = {1:'Cisgênero', 2:'Transgênero', 3: 'Não-binário'}
        questions_dict = {1:'Sim', 2:'Não', 3: 'Não Sei'}
        
        questions = OpeningQuestion(name, age)
        
        question_one = questions.input_genre(genre)
        question_two = questions.questions(schooling)
        question_three = questions.questions(average_wage)
        question_four = questions.questions(illness)
        question_five = questions.questions(assist)

        response = questions.GatherAnswers(name, age, genre_dict[genre], questions_dict[schooling], questions_dict[average_wage], questions_dict[illness], questions_dict[assist])
        df_response.append(response)

    elif input_init == 2:
        print('\nQuestionário encerrado.')
        exit()

    else:
        print('\nEntrada inválida. Questionário encerrado.')
        exit()