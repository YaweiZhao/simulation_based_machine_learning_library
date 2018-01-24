import fileinput

filename = '/vol6/home/kd_yjp/datasets/datasets/regression/yearPredictionMSD/YearPredictionMSD.t'
f = open('YearPredictionMSD_test', 'a+')
s = ''
for line in fileinput.input(filename):
    pos = line.index(' ')
    s += line[0:pos]
    line = line[pos+1:]
    line = line.strip()
    for e in line.split(' '):
        ind, val = e.split(':')
        s += ' ' + val
    s += '\n'
    f.write(s)
    s = ''
