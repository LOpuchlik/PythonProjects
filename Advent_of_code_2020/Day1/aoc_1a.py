lines =[]
with open('/Users/jagoodka/Desktop/aoc_1a_data.txt') as file:
    lines = [line.strip() for line in file]
print(type(lines[0]))

lines_int = [int(line) for line in lines]
print(type(lines_int[0]))

print('------------ PART 1 --------------')
for i in range(len(lines_int)):
    for j in range(len(lines_int)):
        if i!=j and j < i:
            if (lines_int[i] + lines_int[j]) == 2020:
                print(lines_int[i], lines_int[j])
                print(lines_int[i] * lines_int[j])

print('')

print('------------ PART 2 --------------')
for i in range(len(lines_int)):
    for j in range(len(lines_int)):
        for k in range(len(lines_int)):
            if i!=j and j!=k and k < j and j < i:
                if (lines_int[i] + lines_int[j] + lines_int[k]) == 2020:
                    print(lines_int[i], lines_int[j], lines_int[k])
                    print(lines_int[i] * lines_int[j] * lines_int[k])