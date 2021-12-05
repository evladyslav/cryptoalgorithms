p = 2  # input('Input module: ')
f = 'x^3+x^1+1'.split('+')  # input('URAVNENIE: ').split('+')

f_r = f[::-1]
#  print('function factors -> ', f)
n = int(f[0][2])
etalon = ['1'] + ['x^{0}'.format(x) for x in range(n) if not x == 0]
# print('etalon -> ', etalon)
equations = {}
sta = {}
for i in range(len(etalon)):
    equations['q_{0}'.format(i+1)] = ''
    sta['q_{0}'.format(i + 1)] = ''
    if etalon[i] in f_r and not etalon[i] == '1':
        equations['q_{0}'.format(i+1)] += '+'

states = []
state = ''.join(['1'] + ['0' for x in range(n-1)])
llll = ''
for i in range(p ** n - 1):
    prev = ''.join(sta.values())
    for k in zip(range(n), equations.items()):
        value = k[1][1]
        key = k[1][0]
        index = k[0]
        llll = ''
        left = ''
        right = ''
        if len(prev) > 0:
            left = prev[index-1]
            right = prev[index]
        if value == '+':
            if len(prev) > 0:
                sta[key] = str((int(left) + int(right)) % p)
                llll += str((int(left) + int(right)) % p)
            else:
                sta[key] = state[index-1]
                llll += state[index-1]
        else:
            if len(prev) > 0:
                sta[key] = left
                llll += left
            else:
                sta[key] = state[index]
                llll += state[index]
    states.append(''.join(sta.values()))

std = []
rev_std = []
dct = {}
op = ['1', 'x'] + ['x^{0}'.format(x) for x in range(2, n) if not x == 0]


rev_factor = {}

for i in range(p ** n - 1):
    std.append('{0}'.format(states[i]))
    rev_std.append('{0}'.format(states[i][::-1]))
    if len(dct) < n:
        dct[rev_std[i]] = op[::-1][i]
    rev_factor[rev_std[i]] = ''


for oper in range(len(rev_std)):
    operation = rev_std[oper]
    for k in range(len(operation)):
        if operation[k] == '1':
            rev_factor[operation] += "+" + op[::-1][k]

w = ['w^{0}'.format(x) for x in range(0, p ** n - 1)] + ['1']
fin = {}
for k in zip(rev_factor.items(), std, w):
    fin[k[2]] = k[0][0]
    print('{0}   {1}  {2}  \t {3}'.format(k[1], k[0][0], k[2], "+".join(k[0][1].split("+")[1:])))
#print(rev_factor)
string = ''
for i in f:
    if i == '1':
        string += '+' + i
    else:
        fact = i.replace('x', 'w')
        string += rev_factor[fin[fact]]
print()
print()
print(string[1:])

