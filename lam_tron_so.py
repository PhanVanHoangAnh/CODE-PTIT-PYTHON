cnt = int(input())
tests = []

def upLast(x):
    if x % 10 == 0: return x + 1

    last = x % 10
    pref = x // 10

    if last < 9:
        last += 1
    else:
        last = 0
        pref = upLast(pref)

    return pref * 10 + last


def downLast(x):
    if x // 10 == 0: return x

    last = x % 10
    pref = x // 10

    if last == 0: return x

    last -= 1

    return pref * 10 + last

def around(a):
    if a < 10: return a

    if a >= 10 and a <= 99:
        if  a % 10 >= 5: 
            out = (a // 10 + 1) * 10
            return out
        else: return a // 10 * 10

    t = 1

    while a // (10 ** t) > 0:
        x = a % (10 ** t)
        rs = a // (10 ** t)

        if x // 10 > 0: x = x // (10 ** (t - 1))

        if x >= 5:
            rs = upLast(rs)
        else:
            rs = downLast(rs)

        a = rs * (10 ** t)
        t += 1

        print(a)

    return a       

# main
while cnt > 0:
    tests.append(int(input()))
    cnt -= 1

for test in tests:
    print(around(test))
    

