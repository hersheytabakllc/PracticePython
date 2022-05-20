D = {'spam': 2,  'ham': 1, 'eggs': 3, 'zipper':8}

D['ham'] = ['grill', 'bake', 'fry']

del D['eggs']

D['brunch'] = 'Bacon'

L = {}
L[99] = 'spam'

D = {x : x ** 2 for x in [1, 2, 3, 4]}

D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}

D = dict.fromkeys(['a', 'b', 'c'], 0)

D = {k:0 for k in ['a', 'b', 'c']}


test = D

print(test)