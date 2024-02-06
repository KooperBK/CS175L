#CS175L
#Kooper Kaney
#Restaurant

vegetarian = False
vegan = False
gluten_free = False
restlist = ['Joe’s Gourmet Burgers', 'Mama’s Fine Italian', 'Main Street Pizza Company', 'Corner Cafe', 'The Chef’s Kitchen']

ans = input('Is anyone in your party vegetarian? (yes or no): ')
if ans == 'yes':
    vegetarian = True
ans = input('Is anyone in your party vegan? (yes or no): ')
if ans == 'yes':
    vegan = True
ans = input('Is anyone in your party gluten free? (yes or no): ')
if ans == 'yes':
    gluten_free = True

if vegetarian == True:
    if 'Joe’s Gourmet Burgers' in restlist:
        restlist.remove('Joe’s Gourmet Burgers')
if vegan == True:
    if 'Joe’s Gourmet Burgers' in restlist:
        restlist.remove('Joe’s Gourmet Burgers')
    if 'Main Street Pizza Company' in restlist:
        restlist.remove('Main Street Pizza Company')
    if 'Mama’s Fine Italian' in restlist:
        restlist.remove('Mama’s Fine Italian')
if gluten_free == True:
    if 'Mama’s Fine Italian' in restlist:
        restlist.remove('Mama’s Fine Italian')
    if 'Joe’s Gourmet Burgers' in restlist:
        restlist.remove ('Joe’s Gourmet Burgers')
print('Your restaurant choices are: ', end='')
print(', '.join(restlist))


