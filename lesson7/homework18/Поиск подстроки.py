def second_index(word, sign):
    index = word.find(sign)
    if index >=0:
        subword = word[index + 1:]
    else:
        answer="None"
        return answer
    sec_index = subword.find(sign)
    if sec_index>=0:
        answer = index + sec_index + 1
        return answer
    else:
        answer="None"
        return answer

word=input("Type word: ")
sign=input("Type sign whose index we want to find: ")
print(second_index(word,sign))