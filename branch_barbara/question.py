from datetime import datetime

class OpeningQuestion: 
       
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def input_genre(self, genre):
        if genre == 1:
            self.genre = "Cisgênero"
            return self.genre
        elif genre == 2:
            self.genre = "Transgênero"
            return self.genre
        elif genre == 3:
            self.genre = "Não-binário"
            return self.genre
        
    def questions(self, responses):
        if responses == 1:
            self.responses = "Sim"
            return self.responses
        elif responses == 2:
            self.responses = "Não"
            return self.responses
        elif responses == 3:
            self.responses = "Não Sei"
            return self.responses
    
    def GatherAnswers(self, name, age, genre, schooling, average_wage, illness, assist):
        
        dt_date_now = datetime.now()
        date = dt_date_now.strftime("%d/%m/%Y")
        hour = dt_date_now.strftime("%H:%M:%S")
        
        df_columns = {
            'Nome': name,
            'Idade': age,
            'Gênero': genre,
            'Ensino Médio Completo?': schooling, 
            'Média Salarial (> 2 salários mínimos)?': average_wage, 
            'Doenças agravadas pelo isolamento social?': illness, 
            'Consideraria buscar assistência?': assist,
            'Data': date,
            'Horário': hour
        }
        return df_columns