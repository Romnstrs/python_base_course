import string


def first_world(sentence: str):
    punctuation = string.punctuation
    punctuation = punctuation.replace("'", '')
    for p in punctuation:
        sentence = sentence.replace(p, " ")
    lst = sentence.split()
    return lst[0]


sentence = ("... don't and so on ...")
print(first_world(sentence))
