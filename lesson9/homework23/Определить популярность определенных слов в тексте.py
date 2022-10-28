import string


def popular_words(txt,lst):
    i = 0
    tmp = ''
    res = {}
    txt = txt.lower()
    punctuation = string.punctuation
    punctuation = punctuation.replace("'", '')
    for p in punctuation:
        txt = txt.replace(p, " ")
    txt += " "
    for key in lst:
        res[key] = 0
    while i < len(txt):
        if txt[i] == " ":
            i += 1
        else:
            j = i
            while txt[j] != " ":
                tmp += txt[j]
                j += 1
            if tmp in res:
                res[tmp] += 1
            tmp = ''
            i = j + 1
    return res


txt="When    don't        I was One I had just begun When I was Two I was nearly new "
lst=['i','was','three','near',"don't"]
print(popular_words(txt,lst))

