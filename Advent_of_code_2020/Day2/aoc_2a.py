lines =[]
with open('/Users/jagoodka/Desktop/aoc_2a_data.txt') as file:
    lines = [line.strip() for line in file]

rng = [i.split(' ')[0] for i in lines]
min = [int(i.split('-')[0]) for i in rng]
max = [int(i.split('-')[1]) for i in rng]
ltr = [i.split(' ')[1].replace(':', '') for i in lines]
code = [i.split(' ')[2] for i in lines]

ltr_code = zip(ltr, code)

occr = []
for item in ltr_code:
    occr.append(item[1].count(item[0]))
print(occr)    
    
valid = []
for i in range(len(occr)):
    if (occr[i] >= min[i] and occr[i] <= max[i]):
        valid.append(occr[i])

print(len(valid))
        



