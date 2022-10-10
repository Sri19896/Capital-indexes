l = list()


def capital_indexes(f):
    for i in f:
        if i.isupper():
            l.append(f.index(i))
    return(l)


print(capital_indexes('HI'))
