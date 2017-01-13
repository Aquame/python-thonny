# python-thonny
with open('last.txt') as f:
    lines=f.readlines()
    print(lines)
    for line in lines:
        for word in line.split(' '):
            print(word)

with open('outpt.txt','w') as out_file:
    print('123456789',file=out_file)
    print('console')
    print('in file', file=out_file)
