import pandas as pd
import re
import collections

fixed_df = pd.read_csv('titanic.csv')
names = fixed_df['name']
names_list = []
family_list = []
my_arr = []
pattern = re.compile(r'\w+')

for name in names:
    try:
        last_name = pattern.findall(name)[0]
        names_list.append(last_name)
    except TypeError:
        pass

family_list = [item for item, count in collections.Counter(names_list).items() if count > 1]
person_list = [item for item, count in collections.Counter(names_list).items() if count == 1]

# we need this to solve error problem in DataFrame
names_list.append("Shaposnikov")

fixed_df.index = [index for index in names_list]
fixed_df.index.name = 'Last Name'

# get family
for name in family_list:
    info = fixed_df.loc[[name], ['name', 'survived', 'age', 'boat']]

    # get information about family age
    family_age = []
    for i in info['age']:
        family_age.append(i)
    all_age = 0
    for age in family_age:
        all_age += age
    family_middle_age = all_age / len(family_age)

    # get information about family boats
    family_boat = []
    for i in info['boat']:
        family_boat.append(i)
    boats = ''
    for boat in family_boat:
        boats += str(boat) + ', '

    # get information about family survived
    family_survived = []
    for i in info['survived']:
        family_survived.append(i)
    survived = 0
    for survived in family_survived:
        survived += survived

    data = {
        'type': 0,
        'name': name,
        'survived': survived,
        'age': family_middle_age,
        'boat': boats}
    my_arr.append(data)

# get persons
for name in person_list:
    info = fixed_df.loc[[name], ['name', 'survived', 'age', 'boat']]

    data = {
        'type': 1,
        'name': name,
        'survived': info['survived'][0],
        'age': info['age'][0],
        'boat': info['boat'][0]}
    my_arr.append(data)

df = pd.DataFrame(my_arr)
new_df = df[['name', 'type', 'age', 'survived', 'boat']]
new_df.to_csv('new.csv')







