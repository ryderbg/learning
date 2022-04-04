"""
Румен иска да пребоядиса хола и за целта е наел майстори. Напишете програма, която изчислява разходите

за ремонта, предвид следните цени:

Предпазен найлон - 1.50 лв. за кв. метър

Боя - 14.50 лв. за литър

Разредител за боя - 5.00 лв. за литър За всеки случай, към необходимите материали, Румен иска да добави още 10% от количеството боя и 2 кв.м. найлон, разбира се и 0.40 лв. за торбички. Сумата, която се заплаща на майсторите за 1 час работа, е равна

на 30% от сбора на всички разходи за материали.

Вход

Входът се чете от конзолата и съдържа точно 4 реда:

1. Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]

2. Необходимо количество боя (в литри) - цяло число в интервала [1...100]

3. Количество разредител (в литри) - цяло число в интервала [1...30] 4. Часовете, за които майсторите ще свършат работата-цяло число в интервала [1...]

Изход

Да се отпечата на конзолата един ред:

"{сумата на всички разходи}"

Примерен вхОД И ИЗХОД

Вход Изход

10

11

4

727.09

8

Page 4 of 7

2,001 words, 10,750 characters

Обяснения

Сума за найлон: (10 + 2) * 1.50 = 18 лв.

Сума за боя: (11 + 10%) * 14.50 = 175.45 лв. Сума за разредител: 4* 5.00 = 20.00 лв.

Сума за торбички: 0.40 лв.

B

PC

(S

Обща сума за материали: 18 + 175.45 + 20.00 + 0.40 = 213.85 лв.

Default Page Style

10:08

4

Outline 3
"""

def expenses(nylon, paint, paint_addon, bag, working_hours):
  # material prices
  nylon_price = 1.5
  paint_price = 14.50
  paint_addon_price = 5
  bag_price = 0.4
  
  # costs
  nylon_costs = (nylon + 2) * nylon_price
  paint_costs = (paint + (paint *0.1)) * paint_price
  paint_addon_costs = paint_addon * paint_addon_price
  bags_costs = bags * bag_price
  materials_costs = nylon_costs + paint_costs + paint_addon_costs + bags_costs
  workmen_costs = (materials_costs * 0.3) * working_hours
   
  # result 
  total_cost = materials_costs + workmen_costs
  return total_cost
  
nylon = 15
paint = 20
paint_addon = 18
bags = 2
working_hours = 8

total_expenses = expenses(nylon,paint,paint_addon,bags,working_hours)
print(total_expenses)