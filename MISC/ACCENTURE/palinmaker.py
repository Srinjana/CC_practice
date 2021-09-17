# find out what chars should be added to a given string to make a palindromic string.

def palinmaker(s):
    temp = s + "?"
    s = s[::-1]
    temp = temp + s
    n = len(temp)
    palin_suf = [0] * n

    for i in range(1, n):
        Len = palin_suf[i - 1]

        while (Len > 0 and temp[Len] != temp[i]):
            Len = palin_suf[Len - 1]

        if (temp[i] == temp[Len]):
            Len += 1
        palin_suf[i] = Len

    return temp[0: palin_suf[n - 1]]


inp = input()
s = inp[::-1]
res = palinmaker(s)
# print(res)
val = (inp.replace(res, ''))
print(val[::-1])
