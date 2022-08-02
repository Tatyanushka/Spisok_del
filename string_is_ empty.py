import json

data = {}
data['people'] = input('Введите строку:')

# data['people'].append({
#     'name': 'Scott',
#     'website': 'stackabuse.com',
#     'from': 'Nebraska'
# })
# data['people'].append({
#     'name': 'Larry',
#     'website': 'google.com',
#     'from': 'Michigan'
# })
# data['people'].append({
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# })
# data['people'].append({
#     'name': 'Ludmila',
#     'website': 'google.com',
#     'from': 'Rassha'
# })



def string_input_check(): 
    if not(data['people'] and data['people'].strip()):  #исключение ввода пустой строки и пробелов
        print("Не спи!!!","\N{slightly smiling face}", "Добавь, чем сегодня займешься!")
    elif data['people'].isnumeric():    # содержит ли строка только числа
        print('Попробуйте внести дело еще раз!','\U0001F612')
    else:
        print("Дело добавлено в список!",'\U0001F607')

string_input_check()



