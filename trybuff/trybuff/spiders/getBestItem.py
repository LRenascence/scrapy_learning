import json

with open('D:\\Python\\scrapy_learning\\trybuff\\price.json','r') as f:
    load_dict = json.load(f)
with open('D:\\Python\\scrapy_learning\\trybuff\\csgoPrice.json','r') as f:
    load_dict2 = json.load(f)

for i in load_dict:

    try:
        i['ratio'] = float(i['Price'][1:]) * 1.15 / float(i['steamPrice'][1:])
        if i['ratio'] == 0:
            i['ratio'] = 1
    except:
        i['ratio'] = 1
load_dict.sort(key=lambda k: (k.get('ratio', 0)))
for i in range(10):
    print(load_dict[i])

for i in load_dict2:

    try:
        i['ratio'] = float(i['Price'][1:]) * 1.15 / float(i['steamPrice'][1:])
        if i['ratio'] == 0:
            i['ratio'] = 1
    except:
        i['ratio'] = 1
load_dict2.sort(key=lambda k: (k.get('ratio', 0)))
for i in range(10):
    print(load_dict2[i])
