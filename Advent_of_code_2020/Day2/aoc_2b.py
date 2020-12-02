lines =[]
with open('/Users/jagoodka/Desktop/aoc_2a_data.txt') as file:
    lines = [line.strip() for line in file]

rng = [i.split(' ')[0] for i in lines]
min = [int(i.split('-')[0]) for i in rng]
max = [int(i.split('-')[1]) for i in rng]

ltr = [i.split(' ')[1].replace(':', '') for i in lines]

code = [i.split(' ')[2] for i in lines]

min_max_ltr_code = zip(min, max, ltr, code)

occr = []
for item in min_max_ltr_code:
    first = item[0]
    second = item[1]
    letter = item[2]
    password = item[3]
    if password[first-1] != password[second-1]:     
        if (password[first-1] == letter or password[second-1] == letter):
            occr.append(item)

print(len(occr))



