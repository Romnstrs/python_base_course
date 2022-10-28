import string


def correct_sentence(sentence):
    if sentence[0] in string.ascii_lowercase:
        i = sentence[0]
        sentence = i.upper() + sentence[1:]
    if sentence[-1] != ".":
        sentence += "."
    return sentence


sentence = input("Type some sentence: ")
print(correct_sentence(sentence))
