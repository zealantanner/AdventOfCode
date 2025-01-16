import pyperclip

data = open('input.txt', 'r').read().split('\n')[:-1]
total = 0
part1 = [] 
part2 = []
for x in data:
    part = x.split('   ')
    part1.append(part[0])
    part2.append(part[1])
part1.sort()
part2.sort()

i = 0
while i < len(data):
    total += abs(int(part1[i])-int(part2[i]))
    i+=1

print(total)
pyperclip.copy(total)