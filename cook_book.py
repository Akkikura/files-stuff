#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path
import os
from pprint import pprint
with open('recipes.txt', 'rt',encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        name = line.strip()
        ing_count = int(file.readline().strip())
        ingridients = []
        for _ in range(ing_count):
            ing, count, metree = file.readline().strip().split(' | ')
            ingridients.append({
                'ing': ing,
                'count': count,
                'metree': metree
            })
        file.readline()
        cook_book[name] = ingridients
def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ing'] in result:
                    summ1= consist['ing']['count']
                    summ2= consist['count']
                    S = int(summ1) + int(summ2) * person_count
                    result(S)
                else:
                    S1 = consist['count']
                    S = int(S1) * person_count
                    result[consist['ing']] = {'metree': consist['metree'], 'count': S} 
        else:
            print('Такого блюда нет в книге')
    pprint(result, sort_dicts=False)
get_shop_list_by_dishes(12, ['Запеченный картофель', 'Омлет'])
        
        
        
            
    


    
