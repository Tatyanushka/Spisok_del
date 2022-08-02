import json

data = {}
data['people'] = []

data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})
data['people'].append({
    'name': 'Ludmila',
    'website': 'google.com',
    'from': 'Rassha'
})
# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)
# print(data,"\n")


def save():
    with open("data_file.json", "w", encoding='utf-8') as outfile:  
        json.dump(data, outfile)
print(data)
print('Данные успешно сохранены!!!',"\U0001f600")

# python -m pip install pythonji - для добавления эмоджи (прописать команду вконсоли)
