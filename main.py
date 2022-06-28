import pandas as pd
import random

l1 = [i for i in range(10)]
l2 = list()
l3 = list()
alp = "abcdefghijk"

for each in range(10):
    each_code = ''
    for j in range(15):
        rand = random.randint(0, len(alp)-1)
        each_code += alp[rand]
    l2.append(each_code)
    l3.append(random.randint(0,1))

df = pd.DataFrame({'id': l1, 'code': l2, 'gender': l3})
print(df)
