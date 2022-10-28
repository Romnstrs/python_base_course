import string


def is_palindrome(task: string):
    punctuation = string.punctuation + " "
    for p in punctuation:
        task = task.replace(p, "")
    task = task.lower()
    retask = ''
    i = -1
    while len(retask) < len(task) // 2:
        retask += task[i]
        i -= 1
    if task[:len(task) // 2] == retask:
        result = True
    else:
        result = False
    return result


task=input("Type text to check it for palindromic: ")
print(is_palindrome(task))