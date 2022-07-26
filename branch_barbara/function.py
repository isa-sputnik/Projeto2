def separator():
    
    print('\n---------------------------------------------------------------------------------------------------------')

def input_number(input_msg_number):
    digit = False
    valor = 0
    while True:
        message = str(input(input_msg_number))
        if message.isnumeric():
            valor = int(message)
            digit = True
        else:
            print('\nDigite um valor de entrada válido.')
        if digit:
            break
    return valor

def input_text(input_msg_text):
    digit = False
    while True:
        message = str(input(input_msg_text))
        if message.isalpha():
            digit = True
        else:
            print('\nDigite uma mensagem válida.')
        if digit:
            break
    return message

# def input_dict(_dict):
#     _dict = {1:'Sim', 2:'Não', 3: 'Não sei'}
#     _dict = _dict[_dict]